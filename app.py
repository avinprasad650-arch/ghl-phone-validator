import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

ABSTRACT_API_KEY = os.environ.get("ABSTRACT_API_KEY", "")
GHL_API_KEY = os.environ.get("GHL_API_KEY", "")
GHL_API_URL = "https://services.leadconnectorhq.com"

@app.route("/", methods=["GET"])
def health_check():
    return jsonify({"status": "Server is awake!", "routes": ["/", "/validate-phone"]}), 200

@app.route("/validate-phone", methods=["POST"])
def validate_phone():
    data = request.get_json(force=True) or {}
    phone = data.get("phone") or data.get("contact.phone") or ""
    contact_id = data.get("contact_id") or data.get("contactId") or data.get("id")

    if not phone:
        return jsonify({"api-failure": "error", "message": "no phone provided"}), 200

    if not ABSTRACT_API_KEY:
        return jsonify({"api-failure": "error", "message": "ABSTRACT_API_KEY missing"}), 200

    # Phone Intelligence endpoint matching your paid subscription
    abstract_url = f"https://phoneintelligence.abstractapi.com/v1/?api_key={ABSTRACT_API_KEY}&phone={phone}"
    resp = requests.get(abstract_url, timeout=10)
    result = resp.json()

    # Handle Abstract errors
    if resp.status_code != 200 or "error" in result:
        return jsonify({
            "api-failure": "error",
            "error_details": result.get("error", "Abstract error"),
            "result": result,
            "phone": phone
        }), 200

    # Extract nested Phone Intelligence validation and carrier fields
    val_data = result.get("phone_validation") or {}
    carrier_data = result.get("phone_carrier") or {}

    is_valid = val_data.get("is_valid") if "is_valid" in val_data else result.get("valid")
    line_type = (carrier_data.get("line_type") or result.get("type") or result.get("line_type") or "").lower()

    if not is_valid:
        tag = "dead-number"
    elif "mobile" in line_type:
        tag = "clean-mobile"
    elif "landline" in line_type:
        tag = "invalid-landline"
    else:
        tag = "dead-number"

    # Push tag directly into GoHighLevel contact record
    if contact_id and GHL_API_KEY:
        try:
            headers = {
                "Authorization": f"Bearer {GHL_API_KEY}",
                "Version": "2021-07-28",
                "Content-Type": "application/json"
            }
            url = f"{GHL_API_URL}/contacts/{contact_id}/tags"
            requests.post(url, json={"tags": [tag]}, headers=headers, timeout=10)
        except Exception as e:
            print(f"GHL Update failed: {e}")

    return jsonify({"phone": phone, "tag": tag, "abstract": result}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
