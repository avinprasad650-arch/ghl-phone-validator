import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# --- API KEYS FROM VERCEL ENV VARS (NOT hardcoded) ---
ABSTRACT_API_KEY = os.environ.get("ABSTRACT_API_KEY", "")
GHL_API_KEY = os.environ.get("GHL_API_KEY", "")
GHL_API_URL = "https://services.leadconnectorhq.com"
GHL_LOCATION_ID = os.environ.get("GHL_LOCATION_ID", "") # add this in Vercel

# --- ROUTE 0: UPTIME ROBOT HEALTH CHECK ---
# Uptime Robot should ping: https://ghl-phone-validator.vercel.app/  GET
@app.route('/', methods=['GET'])
def health_check():
    return jsonify({"status": "Server is awake!", "routes": ["/", "/validate-phone"]}), 200

# --- ROUTE 1: PHONE VALIDATION ---
# GHL Webhook should POST to: https://ghl-phone-validator.vercel.app/validate-phone
@app.route('/validate-phone', methods=['POST'])
def validate_phone():
    try:
        data = request.get_json(force=True)
        print(f"Incoming data: {data}")

        # GHL sends phone as {{contact.phone}} - handle both formats
        phone = data.get('phone') or data.get('contact.phone') or data.get('Phone')
        contact_id = data.get('contact_id') or data.get('contactId') or data.get('id')

        if not phone:
            return jsonify({"error": "No phone provided"}), 400

        # --- ABSTRACT API CALL ---
        if not ABSTRACT_API_KEY:
            return jsonify({"error": "ABSTRACT_API_KEY missing in env"}), 500

        abstract_url = f"https://phonevalidation.abstractapi.com/v1/?api_key={ABSTRACT_API_KEY}&phone={phone}"
        resp = requests.get(abstract_url
