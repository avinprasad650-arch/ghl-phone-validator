import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

ABSTRACT_API_KEY = os.environ.get("ABSTRACT_API_KEY", "")
GHL_API_KEY = os.environ.get("GHL_API_KEY", "")
GHL_API_URL = "https://services.leadconnectorhq.com"

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({"status": "Server is awake!", "routes": ["/", "/validate-phone"]}), 200

@app.route('/validate-phone', methods=['POST'])
def validate_phone():
    try:
        data = request.get_json(force=True) or {}
        phone = data.get('phone') or data.get('contact.phone') or data.get('Phone') or ""
        contact_id = data.get('contact_id') or data.get('contactId') or data.get('id') or ""

        if not phone:
            return jsonify({"tag": "api-failure", "error": "No phone"}), 200

        if not ABSTRACT_API_KEY:
            return jsonify({"tag": "api-failure", "error": "ABSTRACT_API_KEY missing"}), 200

        abstract_url = f"https://phonevalidation.abstractapi.com/v1/?api_key={ABSTRACT_API_KEY}&phone={phone}"
        resp = requests.get(abstract_url, timeout=10)
        result = resp.json()

        # Handle Abstract errors
        if result.get('error'):
            print(f"Abstract error: {result}")
            return jsonify({"tag": "api-failure", "error": result, "phone": phone}), 200

        is_valid = result.get('valid')
        line_type = str(result.get('type') or result.get('line_type') or "").lower()

        if not is_valid:
            tag = "dead-number"
        elif "landline" in line_type:
            tag = "invalid-landline"
        elif "mobile" in line_type:
            tag = "clean-mobile"
        else:
            tag = "dead-number"

        if contact_id and GHL_API_KEY:
            try:
                headers = {
                    "Authorization": f"Bearer {GHL_API_KEY}",
                    "Version": "2021-07-28",
                    "Content-Type": "application/json"
                }
                url = f"{GHL_API_URL}/contacts/{contact_id}/tags"
                requests.post(url, headers=headers, json={"tags": [tag]}, timeout=10)
            except Exception as e:
                print(f"GHL update failed: {e}")

        return jsonify({"phone": phone, "tag": tag, "abstract": result}), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"tag": "api-failure", "error": str(e)}), 200
