import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Fetch the credentials from Render's environment variables
ABSTRACT_API_KEY = os.environ.get("ABSTRACT_API_KEY")
GHL_API_TOKEN = os.environ.get("GHL_API_TOKEN")

@app.route("/", methods=["GET"])
def health_check():
    return jsonify({
        "status": "success",
        "message": "Render service is awake and active"
    }), 200

@app.route("/webhook", methods=["POST"])
def handle_webhook():
    try:
        # Parse the incoming JSON payload from GHL
        data = request.json
        
        # Extract both the phone number and the unique contact ID
        phone = data.get('phone', '')
        contact_id = data.get('contact_id', '')

        # Fail-safe: if GHL sends empty data
        if not phone or not contact_id:
            return {"error": "Missing phone or contact_id"}, 400

        # Execute the GET request to Abstract API
        abstract_url = f"https://phonevalidation.abstractapi.com/v1/?api_key={ABSTRACT_API_KEY}&phone={phone}"
        abstract_response = requests.get(abstract_url)
        abstract_data = abstract_response.json()

        # 1. Isolate the line validity and type
        is_valid = abstract_data.get("valid")
        line_type = abstract_data.get("type", "Unknown").lower()

        # 2. Map the data to your exact GoHighLevel Workflow Tags
        # FIXED: "mobile" is now lowercase to properly match the line_type format
        if is_valid == False:
            tag_to_apply = "dead-number"
        elif line_type == "mobile":
            tag_to_apply = "clean-mobile"
        else:
            tag_to_apply = "invalid-landline"

        # 3. SEND TAG BACK TO GOHIGHLEVEL
        ghl_url = f"https://services.leadconnectorhq.com/contacts/{contact_id}/tags"

        headers = {
            "Authorization": f"Bearer {GHL_API_TOKEN}",
            "Version": "2021-07-28",
            "Content-Type": "application/json"
        }

        payload = {
            "tags": [tag_to_apply]
        }

        # Issue POST to append the tag to the contact
        ghl_response = requests.post(ghl_url, json=payload, headers=headers)

        return jsonify({
            "status": "success",
            "tag_applied": tag_to_apply,
            "ghl_response": ghl_response.json()
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
import os
import requests
from flask import request, jsonify

# Make sure you set GHL_API_KEY in your Render Environment Variables!
GHL_API_KEY = os.environ.get("GHL_API_KEY") 
GHL_API_URL = "https://services.leadconnectorhq.com"

# You MUST replace these placeholder strings with your actual GHL Custom Field IDs
FIELD_IDS = {
    "mortgage_balance": "YOUR_MORTGAGE_BALANCE_FIELD_ID",
    "monthly_payment": "YOUR_MONTHLY_PAYMENT_FIELD_ID",
    "lender_name": "YOUR_LENDER_FIELD_ID",
    "last_objection": "YOUR_LAST_OBJECTION_FIELD_ID",
    "objection_text": "YOUR_OBJECTION_TEXT_FIELD_ID"
}

@app.route("/update-ghl-context", methods=["POST"])
def update_ghl_context():
    data = request.json
    contact_id = data.get("contactId")
    
    if not contact_id:
        return jsonify({"error": "contactId required"}), 400

    # Build customFields payload for GHL v2 API
    custom_fields = []
    for key, field_id in FIELD_IDS.items():
        if data.get(key):
            custom_fields.append({
                "id": field_id,
                "field_value": str(data.get(key))
            })

    # Payload for updating the custom fields
    payload = {
        "customFields": custom_fields
    }

    headers = {
        "Authorization": f"Bearer {GHL_API_KEY}",
        "Version": "2021-07-28",
        "Content-Type": "application/json"
    }

    # 1. Update the contact's custom fields
    resp = requests.put(
        f"{GHL_API_URL}/contacts/{contact_id}",
        json=payload,
        headers=headers
    )

    # 2. Add a note to the contact timeline so you see the live transcript
    if data.get("objection_text"):
        note_payload = {
            "body": f"LIVE AI NOTE - Objection: {data.get('last_objection')} | Verbatim: {data.get('objection_text')} | Balance: {data.get('mortgage_balance')}",
            "contactId": contact_id
        }
        requests.post(f"{GHL_API_URL}/contacts/{contact_id}/notes", json=note_payload, headers=headers)

    return jsonify({"success": True, "ghl_status": resp.status_code})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
