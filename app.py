import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# --- API KEYS ---
# Your provided Abstract API Key for phone validation
ABSTRACT_API_KEY = os.environ.get("ABSTRACT_API_KEY", "87def4db2e9149ad971a9c6859a012ac")

# GoHighLevel API Key (Must be set in Render Environment Variables!)
GHL_API_KEY = os.environ.get("GHL_API_KEY")
GHL_API_URL = "https://services.leadconnectorhq.com"

# --- GHL CUSTOM FIELD KEYS ---
# These match the exact text inside the 'Key' column in GoHighLevel
FIELD_KEYS = {
    "mortgage_balance": "estimated_mortgage_balance",
    "monthly_payment": "estimated_property_value", # Swap this key later if you make a dedicated monthly payment field
    "lender_name": "lender_name", 
    "last_objection": "last_objection",
    "objection_text": "objection_text"
}

# ==========================================
# ROUTE 1: ABSTRACT API PHONE VALIDATION
# ==========================================
@app.route("/validate-phone", methods=["POST"])
def validate_phone():
    data = request.get_json(silent=True) or {}
    phone = data.get("phone")

    # Satisfies GHL's "Test & deploy" ping to unlock the Save button
    if not phone:
        return jsonify({"status": "test_ok", "message": "Test ping received successfully"}), 200

    try:
        abstract_url = f"https://phonevalidation.abstractapi.com/v1/?api_key={ABSTRACT_API_KEY}&phone={phone}"
        response = requests.get(abstract_url)
        response.raise_for_status()
        api_data = response.json()

        is_valid = api_data.get("valid")
        line_type = api_data.get("type", "").lower()

        status = "dead"
        if is_valid:
            if "mobile" in line_type:
                status = "clean-mobile"
            elif "landline" in line_type:
                status = "invalid-landline"
            else:
                status = line_type

        return jsonify({
            "phone": phone,
            "line_type": line_type,
            "status": status,
            "is_valid": is_valid
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ==========================================
# ROUTE 2: GHL LIVE CONTEXT UPDATE (AI SCREEN POP)
# ==========================================
@app.route("/update-ghl-context", methods=["POST"])
def update_ghl_context():
    data = request.get_json(silent=True) or {}
    contact_id = data.get("contactId")

    # Satisfies GHL's "Test & deploy" ping to unlock the Save button
    if not contact_id:
        return jsonify({"status": "test_ok", "message": "Test ping received successfully"}), 200

    custom_fields = []
    for json_key, ghl_key in FIELD_KEYS.items():
        if data.get(json_key):
            custom_fields.append({
                "key": ghl_key,  # Uses the text Key instead of the alphanumeric ID
                "field_value": str(data.get(json_key))
            })

    headers = {
        "Authorization": f"Bearer {GHL_API_KEY}",
        "Version": "2021-07-28",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    # 1. Update the contact's custom fields
    if custom_fields:
        requests.put(
            f"{GHL_API_URL}/contacts/{contact_id}",
            json={"customFields": custom_fields},
            headers=headers
        )

    # 2. Add a note to the contact timeline so you see the live transcript
    if data.get("objection_text"):
        note_payload = {
            "body": f"LIVE AI NOTE - Objection: {data.get('last_objection')} | Verbatim: {data.get('objection_text')} | Balance: {data.get('mortgage_balance')}",
            "contactId": contact_id
        }
        requests.post(f"{GHL_API_URL}/contacts/{contact_id}/notes", json=note_payload, headers=headers)

    return jsonify({"success": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
