import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Fetch the credentials from Render's environment variables
ABSTRACT_API_KEY = os.environ.get("ABSTRACT_API_KEY")
GHL_API_TOKEN = os.environ.get("GHL_API_TOKEN")

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({
        "status": "active",
        "message": "Render service is awake and active"
    }), 200

# --- GOHIGHLEVEL WEBHOOK ROUTE ---
@app.route('/webhook', methods=['POST'])
def handle_webhook():
    try:
        # Parse the incoming JSON payload from GHL
        data = request.json

        # Extract both the phone number and the unique contact ID
        phone = data.get('phone', '')
        contact_id = data.get('contact_id', '')

        # Fail-safe if GHL sends empty data
        if not phone or not contact_id:
            return jsonify({"error": "Missing phone or contact_id"}), 400

        # Execute the GET request to Abstract API
        abstract_url = f"https://phonevalidation.abstractapi.com/v1/?api_key={ABSTRACT_API_KEY}&phone={phone}"
        abstract_response = requests.get(abstract_url)
        abstract_data = abstract_response.json()

        # Isolate the line type (e.g. Mobile, Landline, VOIP)
        line_type = abstract_data.get("type", "Unknown")

        # --- SEND DATA BACK TO GOHIGHLEVEL ---
        ghl_url = f"https://services.leadconnectorhq.com/contacts/{contact_id}"
        
        headers = {
            "Authorization": f"Bearer {GHL_API_TOKEN}",
            "Version": "2021-07-28",
            "Content-Type": "application/json"
        }

        payload = {
            "customFields": [
                {
                    "key": "line_type",
                    "field_value": line_type
                }
            ]
        }

        ghl_response = requests.put(ghl_url, json=payload, headers=headers)

        return jsonify({
            "status": "success",
            "line_type": line_type,
            "ghl_response": ghl_response.json()
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
