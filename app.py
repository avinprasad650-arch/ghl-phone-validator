import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# --- API KEYS ---
# Hardcoded Abstract API Key to bypass Render's Environment Variable UI
ABSTRACT_API_KEY = "87de4db2e9148a8971a9c6859a012ac"

# GoHighLevel API Key (Must be set in Render Environment Variables!)
GHL_API_KEY = os.environ.get("GHL_API_KEY", "")
GHL_API_URL = "https://services.leadconnectorhq.com"

# --- GHL CUSTOM FIELD KEYS ---
# Map exactly the text inside the 'Key' column in GoHighLevel
FIELD_KEYS = {
    "mobile": "contact.phone",
    "monthly_payment": "estimated_property_value", 
    "lender_name": "lender_name",
    "loan_balance": "loan_balance",
    "objection_text": "objection_text"
}

# ==========================================
# ROUTE 0: UPTIME ROBOT HEALTH CHECK
# ==========================================
@app.route('/', methods=['GET'])
def health_check():
    return "Server is awake!", 200

# ==========================================
# ROUTE 1: ABSTRACT API PHONE VALIDATION
# ==========================================
@app.route('/validate-phone', methods=['POST'])
def validate_phone():
    data = request.get_json(silent=True) or {}
    phone = data.get('phone')

    # Satisfies GHL's 'Test & Deploy' ping to unlock the Save button
    if not phone:
        return jsonify({"status": "test_ok", "message": "Test ping received successfully"}), 200

    # 1. Ping Abstract API (Using params dictionary to safely URL-encode formatting)
    abstract_url = "https://phonevalidation.abstractapi.com/v1/"
    payload = {
        "api_key": ABSTRACT_API_KEY.strip(),
        "phone": phone
    }
    
    response = requests.get(abstract_url, params=payload)
    
    if response.status_code != 200:
        # If it fails, send the exact error text back to GoHighLevel for easy debugging
        return jsonify({"error": f"Abstract API Error {response.status_code}: {response.text}"}), 500

    api_data = response.json()

    is_valid = api_data.get('valid')
    line_type = api_data.get('type', '').lower()

    status = "dead"
    if is_valid:
        if "mobile" in line_type:
            status = "valid-mobile"
        elif "landline" in line_type:
            status = "valid-landline"

    return jsonify({
        "phone": phone,
        "is_valid": is_valid,
        "status": status,
        "line_type": line_type
    }), 200

# ==========================================
# ROUTE 2: GHL LIVE CONTEXT UPDATE (AI SCREEN POP)
# ==========================================
@app.route('/update-ghl-context', methods=['GET', 'POST', 'OPTIONS'])
def update_ghl_context():
    if request.method == 'OPTIONS' or request.method == 'GET':
        # Auto-approve GHL's test pings (GET/OPTIONS) with CORS headers to unlock the Save button
        resp = jsonify({"status": "test_ok", "message": "Test ping received successfully"})
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = '*'
        return resp, 200

    data = request.get_json(silent=True) or {}
    contact_id = data.get("contact_id")

    if not contact_id:
        return jsonify({"error": "Missing contact_id"}), 400

    # Construct the custom fields update payload
    custom_fields = []
    
    for key, val in data.items():
        if key in FIELD_KEYS.keys():
            custom_fields.append({
                "id": FIELD_KEYS[key],
                "key": FIELD_KEYS[key],
                "field_value": str(val).strip()
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
    objection_text = data.get('objection_text', '')
    if objection_text:
        note_body = f"AI LIVE NOTE - Objection: {objection_text} | Balance: {data.get('loan_balance', '')}"
        requests.post(
            f"{GHL_API_URL}/contacts/{contact_id}/notes",
            json={"body": note_body},
            headers=headers
        )

    return jsonify({"success": True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
