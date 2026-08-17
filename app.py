import os
import requests
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Securely pull your Abstract API key from Render's environment variables
ABSTRACT_API_KEY = os.environ.get("ABSTRACT_API_KEY", "YOUR_ABSTRACT_KEY_HERE")

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    # 1. Catch the incoming JSON payload from GoHighLevel
    data = request.json
    
    # Extract the phone number (Ensure your GHL webhook maps the number to 'phone')
    phone = data.get('phone') 
    
    if not phone:
        return jsonify({"error": "No phone number provided"}), 400

    # 2. Format the URL for the Abstract API Phone Validation endpoint
    url = f"https://phonevalidation.abstractapi.com/v1/?api_key={ABSTRACT_API_KEY}&phone={phone}"
    
    try:
        # 3. Execute the GET request to Abstract API (The HLR Ping)
        response = requests.get(url)
        abstract_data = response.json()
        
        # 4. Extract the critical data points from the Abstract response
        # 'valid' is a true/false boolean representing network connectivity
        is_valid = abstract_data.get("valid") 
        # 'type' is the line classification (e.g., 'Landline', 'Mobile')
        phone_type = abstract_data.get("type", "").lower()

        # 5. Execute the tagging logic based on the HLR response
        if is_valid == False:
            # The line is disconnected or entirely invalid
            tag_to_apply = "invalid-landline" 
        elif phone_type == "landline" or phone_type == "voip":
            # The line is active, but cannot receive standard SMS
            tag_to_apply = "invalid-landline"
        else:
            # The line is active and is a mobile device
            tag_to_apply = "clean-mobile"

        # 6. Return the finalized JSON package back to GoHighLevel
        return jsonify({
            "phone": phone,
            "is_network_active": is_valid,
            "line_type": phone_type,
            "assigned_tag": tag_to_apply
        }), 200

    except Exception as e:
        # Failsafe error handling
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Bind the server to Render's required port
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
