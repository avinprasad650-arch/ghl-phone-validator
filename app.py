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

# --- GHL CUSTOM FIELD IDS ---
# Replace these strings with your actual GoHighLevel Custom Field IDs
FIELD_IDS = {
    "mortgage_balance": "YOUR_MORTGAGE_BALANCE_FIELD_ID",
    "monthly_payment": "YOUR_MONTHLY_PAYMENT_FIELD_ID",
    "lender_name": "YOUR_LENDER_FIELD_ID",
    "last_objection": "YOUR_LAST_OBJECTION_FIELD_ID",
    "objection_text": "YOUR_OBJECTION_TEXT_FIELD_ID"
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
    for key, field_id in FIELD_IDS.items():
        if data.get(key) and not field_id.startswith("YOUR_"):
            custom_fields.append({
                "id": field_id,
                "field_value": str(data.get(key))
            })

    headers = {
        "Authorization": f"Bearer {GHL_API_KEY}",
        "Version": "2021-07-28",
        "Content-Type": "application/json"
    }

    if custom_fields:
        requests.put(
            f"{GHL_API_URL}/contacts/{contact_id}",
            json={"customFields": custom_fields},
            headers=headers
        )

    if data.get("objection_text"):
        note_payload = {
            "body": f"LIVE AI NOTE - Objection: {data.get('last_objection')} | Verbatim: {data.get('objection_text')} | Balance: {data.get('mortgage_balance')}",
            "contactId": contact_id
        }
        requests.post(f"{GHL_API_URL}/contacts/{contact_id}/notes", json=note_payload, headers=headers)

    return jsonify({"success": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
