import os
import requests
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Fetch the credentials from Render's environment variables
ABSTRACT_API_KEY = os.environ.get("ABSTRACT_API_KEY")
GHL_API_TOKEN = os.environ.get("GHL_API_TOKEN")

# --- ROOT HEALTH CHECK ROUTE (FOR UPTIMEROBOT) ---
@app.route('/', methods=['GET'])
def health_check():
    """
    Returns a 200 OK status to keep Render awake and satisfy UptimeRobot pings.
    """
    return jsonify({
        "status": "online",
        "message": "Render service is awake and active"
    }), 200

# --- GOHIGHLEVEL WEBHOOK ROUTE ---
@app.route('/webhook', methods=['POST'])
def handle_webhook():
    # 1. Catch the incoming JSON payload from GoHighLevel
    data = request.json
    
    # Extract both the phone number and the unique contact ID
    phone = data.get('phone')
    contact_id = data.get('contact_id')
    
    # Fail-safe if GHL sends empty data
    if not phone or not contact_id:
        return jsonify(error="Missing phone or contact_id"), 400
        
    # 2. Execute the GET request to Abstract API
    # Abstract API Phone Validation - Live HLR Ping
    abstract_url = f"https://phonevalidation.abstractapi.com/v1/?api_key={ABSTRACT_API_KEY}&phone={phone}"
    
    try:
        # 3. Execute the GET request to Abstract API
        abstract_response = requests.get(abstract_url)
        abstract_data = abstract_response.json()
        
        # 4. Extract connectivity status and line type
        is_valid = abstract_data.get('valid')
        phone_type = abstract_data.get('type', '').lower()
        
        # 5. Logic to determine the correct GoHighLevel tag
        if is_valid is False:
            # The line is disconnected entirely
            tag_to_apply = "dead-number"
        elif phone_type == "landline" or phone_type == "voip":
            # The line is active, but cannot receive standard SMS
            tag_to_apply = "invalid-landline"
        else:
            # The line is active and is a mobile device
            tag_to_apply = "clean-mobile"
            
        # 6. PUSH THE TAG BACK TO GOHIGHLEVEL VIA API
        # Target the specific contact using their contact ID
        ghl_url = f"https://services.leadconnectorhq.com/contacts/{contact_id}/tags"
        
        ghl_headers = {
            "Authorization": f"Bearer {GHL_API_TOKEN}",
            "Version": "2021-07-28",
            "Content-Type": "application/json"
        }
        
        ghl_payload = {
            "tags": [tag_to_apply]
        }
        
        # Execute the tag addition
        ghl_response = requests.post(ghl_url, headers=ghl_headers, json=ghl_payload)
        
        # 7. Return success log to the Render terminal
        return jsonify({
            "phone": phone,
            "assigned_tag": tag_to_apply,
            "ghl_response_status": ghl_response.status_code
        }), 200

    except Exception as e:
        return jsonify(error=f"{str(e)}"), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
