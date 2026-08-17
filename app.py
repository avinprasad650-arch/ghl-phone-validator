import os
import requests
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Securely pull BOTH API keys from Render's environment variables
ABSTRACT_API_KEY = os.environ.get("ABSTRACT_API_KEY")
GHL_API_TOKEN = os.environ.get("GHL_API_TOKEN")

# Route updated to match your GoHighLevel Webhook action
@app.route('/validate-phone', methods=['POST'])
def handle_webhook():
    # 1. Catch the incoming JSON payload from GoHighLevel
    data = request.json
    
    # Extract both the phone number and the unique contact ID
    phone = data.get('phone')
    contact_id = data.get('contact_id')
    
    # Failsafe if GHL sends empty data
    if not phone or not contact_id:
        return jsonify({"error": "Missing phone or contact_id"}), 400

    # 2. Format the URL for the Abstract API Live HLR Ping
    abstract_url = f"https://phonevalidation.abstractapi.com/v1/?api_key={ABSTRACT_API_KEY}&phone={phone}"
    
    try:
        # 3. Execute the GET request to Abstract API
        response = requests.get(abstract_url)
        abstract_data = response.json()
        
        # 4. Extract connectivity status and line type
        is_valid = abstract_data.get("valid") 
        phone_type = abstract_data.get("type", "").lower()

        # 5. Logic to determine the correct GoHighLevel tag
        if is_valid == False:
            tag_to_apply = "invalid-landline" 
        elif phone_type == "landline" or phone_type == "voip":
            tag_to_apply = "invalid-landline"
        else:
            tag_to_apply = "clean-mobile"

        # 6. PUSH THE TAG BACK TO GOHIGHLEVEL VIA API
        # Target the specific contact using their contact_id
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
            "ghl_api_status": ghl_response.status_code
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
