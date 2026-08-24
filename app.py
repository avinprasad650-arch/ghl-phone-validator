import os
import requests
import threading
from flask import Flask, request, jsonify

app = Flask(__name__)

# --- ENVIRONMENT VARIABLES ---
ABSTRACT_API_KEY = os.environ.get("ABSTRACT_API_KEY")
GHL_API_TOKEN = os.environ.get("GHL_API_TOKEN")
PROPERTY_DATA_API_KEY = os.environ.get("PROPERTY_DATA_API_KEY") # You will need to add this to Render

@app.route('/', methods=['GET'])
def health_check():
    """Root route to keep Render awake and verify server status."""
    return jsonify({
        "status": "active",
        "message": "Enrichment microservice is awake and routing."
    }), 200

def process_and_update(data):
    """Background task that runs the API lookups and pushes to GHL."""
    contact_id = data.get('contact_id')
    phone = data.get('phone', '')
    address = data.get('address', '')
    city = data.get('city', '')
    state = data.get('state', '')
    postal_code = data.get('postal_code', '')

    if not contact_id:
        return

    # 1. ABSTRACT API: Phone Validation
    line_type = "Unknown"
    try:
        if phone:
            abs_url = f"https://phonevalidation.abstractapi.com/v1/?api_key={ABSTRACT_API_KEY}&phone={phone}"
            abs_res = requests.get(abs_url, timeout=5).json()
            # Abstract returns "Mobile", "Landline", "VOIP", etc.
            line_type = abs_res.get("type", "Unknown") 
    except Exception as e:
        print(f"Abstract API Error: {e}")

    # 2. PROPERTY API: Mortgage & Equity Data
    prop_val = 0
    mortgage = 0
    equity = 0
    year = 0
    enrich_status = "Enriched_Unverified"

    try:
        if address and PROPERTY_DATA_API_KEY:
            # Note: Swap this URL with your specific property data provider (Estated, ATTOM, etc.)
            prop_url = "https://api.estated.com/v4/property"
            params = {
                "token": PROPERTY_DATA_API_KEY,
                "combined_address": f"{address}, {city}, {state} {postal_code}"
            }
            prop_res = requests.get(prop_url, params=params, timeout=6)
            
            if prop_res.status_code == 200:
                res_data = prop_res.json().get("data", {})
                prop_val = res_data.get("valuation", {}).get("value", 0) or 0
                deeds = res_data.get("deeds", [])
                
                if deeds:
                    latest_deed = deeds[0]
                    mortgage = latest_deed.get("mortgage", {}).get("amount", 0) or 0
                    date_str = latest_deed.get("recording_date", "0000")
                    year = int(date_str[:4]) if date_str else 0
                
                # Calculate Equity
                if prop_val and mortgage:
                    equity = max(0, prop_val - mortgage)
                
                # Update status if we found hard mortgage data
                if mortgage > 0:
                    enrich_status = "Enriched_Valid"

    except Exception as e:
        print(f"Property API Error: {e}")
        enrich_status = "Enrichment_Failed"

    # 3. GOHIGHLEVEL: Unified Contact Update
    try:
        ghl_url = f"https://services.leadconnectorhq.com/contacts/{contact_id}"
        headers = {
            "Authorization": f"Bearer {GHL_API_TOKEN}",
            "Version": "2021-07-28",
            "Content-Type": "application/json"
        }
        
        # CRITICAL: Monetary and Number fields are sent as raw integers, NOT strings.
        payload = {
            "customFields": [
                {"key": "line_type", "field_value": line_type},
                {"key": "enrichment_status", "field_value": enrich_status},
                {"key": "estimated_property_value", "field_value": prop_val},
                {"key": "estimated_mortgage_balance", "field_value": mortgage},
                {"key": "estimated_home_equity", "field_value": equity},
                {"key": "property_purchase_year", "field_value": year}
            ]
        }
        
        requests.put(ghl_url, json=payload, headers=headers, timeout=10)
    except Exception as e:
        print(f"GHL API Update Error: {e}")

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    """Receives the payload from GHL and immediately triggers the background worker."""
    data = request.json
    if not data or "contact_id" not in data:
        return jsonify({"error": "Missing contact_id"}), 400
    
    # Fire the enrichment process in a separate thread to prevent GoHighLevel from timing out
    worker = threading.Thread(target=process_and_update, args=(data,))
    worker.start()
    
    return jsonify({
        "status": "processing", 
        "message": "Webhook received. Running enrichment in background.",
        "contact_id": data.get("contact_id")
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
