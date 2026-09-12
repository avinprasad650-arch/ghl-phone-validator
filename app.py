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
