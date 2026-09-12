import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# --- KEEP YOUR EXISTING ABSTRACT API / PHONE VALIDATOR ROUTES HERE ---


# --- LIVE GHL CONTEXT UPDATE ROUTE ---
GHL_API_KEY = os.environ.get("GHL_API_KEY")
GHL_API_URL = "https://services.leadconnectorhq.com"

FIELD_IDS = {
    "mortgage_balance": "YOUR_MORTGAGE_BALANCE_FIELD_ID",
    "monthly_payment": "YOUR_MONTHLY_PAYMENT_FIELD_ID",
    "lender_name": "YOUR_LENDER_FIELD_ID",
    "last_objection": "YOUR_LAST_OBJECTION_FIELD_ID",
    "objection_text": "YOUR_OBJECTION_TEXT_FIELD_ID"
}

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
