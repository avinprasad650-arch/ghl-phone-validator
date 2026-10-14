
Gemini

Plan steps

New chat
Library
Images
Scheduled
Daily brief

More
New notebook
GHL INSURANCE
4.7L TEARDOWN
GoHighLevel Pipeline Hygiene Audit
Recent Gemini Ecosystem Updates
AI Versus Human Intelligence
Types and Benchmarks of Crude Oil
Top Chinese Military Weapons
Understanding Argon 4 AI Model
Daily Oil Price Analysis
Signal Jammer Request Denied
Identifying Carbureted Engine Type
Toyota's Most Globally Available Parts
Current U.S. Economic State
1999 Land Cruiser Bushing Replacement
LC500 Long-Term Storage Best Practices
Most Comfortable Men's Sneakers
1999 Land Cruiser Antenna Button
Best Post-2000 Toyota Tacomas
Painting a 1999 Land Cruiser Grille
Yota Nation Reviews and Feedback
Recent Gemini Updates and Changes
Skill Creation Assistance
Understanding POSS CS PG 2 Charges
Most Available Car Parts Worldwide
Jeep Versus Toyota Part Costs
Uses of Super Lithium EP Moly Grease
Custom Instructions Expansion Directives
South 2nd and William Streets
89 Octane for 1999 Land Cruiser
LC500 Trade-In Equity and Purchase Budget
Understanding Engine Blow-by and Diagnostics
Conversation with Gemini
Gemini Spark Skill & Schedule Directive: GHL Pipeline Hygiene Audit

Skill Name: GHL-CRM-Pipeline-Audit

Schedule: Every Monday at 6:00 AM PST (Recurring background trigger)

Execution Instructions for Spark:

Access the connected GoHighLevel account via the integration connector. Perform a comprehensive pipeline and contact database audit across all active sales pipelines using the following parameters:

Stale Lead Detection: Identify all contacts sitting in active pipeline stages (New Lead, Attempted Contact, Appointment Booked) with zero activity, task updates, or communication logs recorded in the last 7 days.
Data Hygiene & Missing Fields: Flag any contact records missing critical required data parameters (e.g., missing valid phone number formatting, missing email addresses, or unpopulated lead source tags).
Unassigned Follow-Up Flags: Check for opportunities or contacts that have active inbound text or email replies in the last 48 hours but remain unassigned or lack an active upcoming task reminder.
Reporting & Action:
Generate a clean, consolidated summary table in a dedicated Google Sheet titled GHL Weekly Pipeline Audit - [Current Date] categorized by issue type (Stale, Incomplete Data, Unassigned).
Apply internal maintenance tags (e.g., audit-flagged-stale or audit-missing-data) directly to the affected GHL contact records via the API connector.
Send a concise executive summary notification to my primary email highlighting the total count of flagged records and primary pipeline bottlenecks.
The skill and recurring schedule have been created.

1. Skill Created
Skill Name: ghl-crm-pipeline-audit

Status: Saved and active.

Scope: Encapsulates the logic for stale lead identification across active pipeline stages, missing contact parameter detection, unassigned inbound follow-up flagging, maintenance tagging, Google Sheet audit generation, and executive email notifications.

2. Schedule Configured
Title: Audit GHL pipeline hygiene

Cadence: Weekly on Mondays around 6:00 AM PST (0 6 * * 1)

Execution Plan: Calls @ghl-crm-pipeline-audit to audit active pipelines, apply maintenance tags, generate a dated Google Sheet report, and deliver an executive email summary.

Note on Integration: Full execution of the audit steps requires active API credentials or connector access to your GoHighLevel account.

You can test the skill manually at any time with a prompt such as:

"Run a pipeline hygiene audit on my GoHighLevel account."

ghl-crm-pipeline-audit
Audit GoHighLevel (GHL) CRM sales pipelines and contact databases for stale leads, missing contact data fields, and unassigned follow-ups. Generates audit Google Sheets and emails summary reports. Use when asked to audit GHL pipelines, check CRM lead hygiene, or run pipeline hygiene checks.

Instructions
ghl-crm-pipeline-audit
Automates pipeline hygiene and contact database audits across GoHighLevel (GHL) sales pipelines. Identifies stale opportunities, flags missing contact attributes, highlights unassigned inbound communications, updates records with maintenance tags, logs findings to Google Sheets, and sends executive email summaries.

When to Use
When running scheduled or on-demand GoHighLevel (GHL) pipeline audits.
When detecting stale leads in active stages (New Lead, Attempted Contact, Appointment Booked) without recent updates.
When identifying missing contact data (invalid/missing phone numbers, missing emails, or missing lead sources).
When detecting unassigned contacts or opportunities with recent inbound customer activity.
When generating weekly CRM hygiene audit spreadsheets and sending executive email briefings.
Steps
Access GoHighLevel Pipeline Data

Connect to the GoHighLevel account through the available integration connector or API endpoints.
Fetch active contacts and opportunity records across all primary sales pipelines.
Pull recent communication logs, task reminders, assignment statuses, and pipeline stage metadata.
Audit Criteria Evaluation

Stale Lead Detection: Identify contacts in active pipeline stages ("New Lead", "Attempted Contact", "Appointment Booked") with zero logged activities, notes, tasks, or communications in the past 7 days.
Data Hygiene: Flag contacts missing valid phone numbers, missing email addresses, or unpopulated lead source attribution tags.
Unassigned Inbound Leads: Flag opportunities or contacts that received inbound SMS or email replies in the past 48 hours but remain unassigned or have no upcoming scheduled task reminder.
Tagging and CRM Updates

Apply standard maintenance tags directly to flagged contact records in GoHighLevel (e.g., audit-flagged-stale, audit-missing-data, audit-unassigned-followup).
Ensure existing contact tags and custom fields are preserved during tag updates.
Spreadsheet Generation

Create a Google Sheet titled GHL Weekly Pipeline Audit - [Current Date] (e.g., using format YYYY-MM-DD).
Categorize entries into dedicated sections or tabs by issue type: Stale Leads, Incomplete Data, and Unassigned Follow-ups.
Include contact identifiers, name, stage, days inactive, missing fields, and applied tags.
Executive Email Notification

Construct a concise executive summary highlighting total flagged records, breakdown by issue category, and primary pipeline bottlenecks.
Send the notification email to the primary user email address using Gmail.
Gotchas
Connector Availability: If the GoHighLevel API connector or credentials are not active or configured, notify the user immediately and request API connection setup.
Timezone Consistency: Evaluate 7-day inactivity and 48-hour inbound response windows relative to the account local timezone (America/Los_Angeles / PST).
Tag Idempotency: Verify existing tags before applying new audit tags to prevent duplicate tag additions.
Rate Limiting: Respect GHL API rate limits during bulk contact inspection and tagging.
See more
Audit GHL pipeline hygiene
When to run:
Weekly on Mon around 6:00 AM

What to do:
Perform a weekly GoHighLevel (GHL) pipeline and contact database audit using @ghl-crm-pipeline-audit:

Access my connected GoHighLevel account and audit all active sales pipelines across:
Stale leads: contacts in active stages (New Lead, Attempted Contact, Appointment Booked) with no activity or communication logs in the last 7 days.
Data hygiene issues: contact records missing valid phone numbers, email addresses, or lead source tags.
Unassigned follow-ups: contacts with active inbound SMS or email replies in the last 48 hours that remain unassigned or lack an active upcoming task reminder.
Apply internal maintenance tags (such as audit-flagged-stale, audit-missing-data, or audit-unassigned-followup) directly to the affected GoHighLevel contact records.
Generate a consolidated summary table in a dedicated Google Sheet titled "GHL Weekly Pipeline Audit - [Current Date]" categorized by issue type (Stale, Incomplete Data, Unassigned).
Send a concise executive summary notification to my primary email highlighting total flagged record counts, category breakdown, and primary pipeline bottlenecks.
See more
Schedules run at approximate times and use more of your limit at peak hours. They won't run if you reach your limit.

Audit GHL pipeline hygiene

ran on October 12, 6:24 AM
Here is the status report for the scheduled GHL Pipeline Hygiene Audit on Monday, October 12, 2026:

Audit Status: Connection Required
The scheduled audit initiated at 6:00 AM PST, but could not complete the live scan or record tagging because an active integration connector or API connection to your GoHighLevel account is not currently configured.

Summary of Audit Scope & Status
Task / Parameter	Configured Criteria	Execution Status
Stale Lead Detection	Contacts in New Lead, Attempted Contact, or Appointment Booked with 0 updates in 7 days	Blocked (Requires live GHL pipeline access)
Data Hygiene Checks	Missing/invalid phone formatting, missing emails, unpopulated lead source tags	Blocked (Requires live GHL contact access)
Unassigned Follow-ups	Inbound SMS/email replies in last 48 hours unassigned or without upcoming task reminders	Blocked (Requires live GHL communication logs)
CRM Tagging	Apply audit-flagged-stale, audit-missing-data, etc. directly to records	Blocked (Requires GHL API write permissions)
Audit Spreadsheet	Create GHL Weekly Pipeline Audit - [Current Date] Google Sheet	Pending live pipeline data retrieval
Executive Notification	Email summary to primary address	Completed
Actions Taken
Email Notification Sent: An executive status update has been delivered to your primary email address (avinprasad650@gmail.com):

Email: GHL Weekly Pipeline Audit - Connection Required (Oct 12, 2026) (Subject: GHL Weekly Pipeline Audit - Connection Required (Oct 12, 2026), Date: October 12, 2026).

Existing Workspace Files: Your historical contact export from September 2026, Export_Contacts_All_Sep_2026_10_49_AM, remains accessible in Google Drive, but cannot reflect real-time pipeline stages, recent 48-hour inbound communications, or live CRM tagging.

Next Steps to Enable Automated Audits
To allow subsequent weekly runs to execute fully, please connect your GoHighLevel account or provide API access credentials. Once linked, the recurring schedule will automatically query active pipelines, log flagged records to your weekly audit sheet, and apply maintenance tags.

Here is my API key for GHL



pit-us-8de883e3-2077-443c-a521-17c7a2c1e4ef

I've saved your GoHighLevel Private Integration Token into a secure Google Keep note: GoHighLevel API Credentials.

How This Connects to Your Weekly Audit
Gemini's scheduled background runtime operates inside a secure environment that cannot make direct outbound HTTP calls to external third-party endpoints like services.leadconnectorhq.com.

To make your weekly 6:00 AM PST audit run end-to-end with this token, here are the two most seamless ways to bridge the connection:

1. Google Sheets + Apps Script (Recommended)
You can attach a lightweight Google Apps Script to your audit Google Sheet. Because Apps Script runs directly within Google Workspace and has outbound fetch access (UrlFetchApp):

A time-driven Apps Script trigger can fire every Monday at 5:45 AM PST using your token to pull contacts, opportunities, and communications from GoHighLevel directly into your sheet.

At 6:00 AM PST, your scheduled Gemini directive (@ghl-crm-pipeline-audit) analyzes the data, identifies pipeline bottlenecks, and delivers your executive email briefing.

2. Via Your Webhook / Render Middleware
Since you already maintain the ghl-abstract-webhook service on Render:

You can configure an automated endpoint to poll your GHL pipeline using this token and push the snapshot into Google Sheets or Google Drive each Monday morning.

Gemini will immediately consume the updated dataset for reporting, stale lead detection, and follow-up flags.

Let me know if you'd like me to draft the plug-and-play Apps Script code for your sheet or set up the template audit spreadsheet in Google Drive to receive the data.

Ok. lets do render. give me instructions

I've built the complete Python audit script for your GoHighLevel integration and saved it as a deliverable:

PY icon
ghl_audit
 PY 
You can deploy and run this on Render using either a dedicated Render Cron Job or by adding an audit route to your existing Render Web Service (ghl-abstract-webhook).

Option 1: Render Cron Job (Recommended)
This runs automatically every Monday morning without keeping a continuous server alive.

Add the Script to Your Repository:

Commit ghl_audit.py into your GitHub repository (avinprasad650-arch/ghl-phone-validator).

Ensure requests is listed in your requirements.txt.

Create a Cron Job in Render:

Navigate to your Render Dashboard and click New + > Cron Job.

Connect your ghl-phone-validator repository.

Set Command to: python ghl_audit.py.

Set Schedule to: 0 13 * * 1 (runs at 13:00 UTC / 6:00 AM PST every Monday).

Configure Environment Variables:

Add GHL_API_KEY: pit-us-8de883e3-2077-443c-a521-17c7a2c1e4ef (stored in your Keep note).

Add GHL_LOCATION_ID: your GoHighLevel Sub-Account Location ID.

Option 2: Endpoint in Your Existing Web Service
If you prefer triggering the audit via an HTTP request or webhook:

Import the Runner into app.py:

Python
from ghl_audit import run_pipeline_audit

@app.route("/audit", methods=["POST", "GET"])
def trigger_audit():
    summary = run_pipeline_audit()
    return summary, 200
Set the Environment Variables in ghl-abstract-webhook:

Open ghl-abstract-webhook Settings in Render.

Add GHL_API_KEY and GHL_LOCATION_ID under the Environment tab.

Trigger the Endpoint:

Call [https://ghl-abstract-webhook.onrender.com/audit](https://ghl-abstract-webhook.onrender.com/audit) via a scheduled webhook or cron ping.

What the Script Handles
Stale Lead Detection: Scans active pipeline stages (New Lead, Attempted Contact, Appointment Booked) for records inactive for 7+ days and applies the audit-flagged-stale tag.

Data Hygiene: Flags records missing phone numbers, emails, or lead source tags and applies audit-missing-data.

Unassigned Follow-Ups: Flags contacts with inbound replies in the last 48 hours lacking an assigned owner and applies audit-unassigned-followup.

Go ahead and review the instructions you gave me. Check if everthiing is ok

I reviewed the previous instructions and script against the GoHighLevel API v2 specification and your setup, and caught six issues that would have caused silent failures or missed records. I've updated the script with all fixes applied:

PY icon
ghl_audit
 PY 
Issues Found & Fixed
Issue Area	What Was Wrong in v1	Fix Applied in v2
Pipeline Stage Mapping	Checked opp.get("pipelineStage", {}).get("name"), which does not exist in GHL v2 /opportunities/search responses (only pipelineStageId UUIDs are returned), resulting in 0 stale leads detected.	Added get_pipeline_stage_map() to call GET /opportunities/pipelines first and map each pipelineStageId to its stage name (New Lead, Attempted Contact, Appointment Booked).
100-Record Pagination Cap	Used a single limit=100 request without pagination, which would skip over 80% of your contacts (your September export has 616 contacts).	Added cursor pagination loops using meta.startAfter and meta.startAfterId across both opportunities and contacts, plus 429 rate-limit backoff.
48h Inbound & Task Checks	Checked lastMessageDirection on the /contacts/ endpoint where that field isn't returned, and skipped checking for upcoming task reminders.	Switched to GET /conversations/search (filtering lastMessageDirection == "inbound" and epoch millisecond timestamps) and added GET /contacts/{id}/tasks to verify incomplete tasks.
Phone Formatting & Tag Idempotency	Only checked if phone was empty rather than validating formatting, and fired POST /contacts/{id}/tags even when the tag was already present.	Added E.164/10-digit regex validation (^\+?1?\d{10,14}$) and apply_tag_if_missing() to skip contacts that already have the maintenance tag.
Google Sheets Hand-off	Only printed results to Render's stdout console logs, which Gemini cannot access during its 6:00 AM run.	Added SHEETS_WEBHOOK_URL support to POST the structured JSON payload directly to your Google Sheet so it's ready for Gemini to read.
Cron Timing & Timezone	Scheduled Render at 0 13 * * 1 (6:00 AM PDT / 5:00 AM PST), creating a race condition with your 6:00 AM Gemini trigger.	Shifted the Render schedule 15 minutes earlier (45 12 * * 1 in PDT / 45 13 * * 1 in PST) so the data finishes syncing before Gemini runs at 6:00 AM.
Updated Render Setup Checklist
Commit the Updated ghl_audit.py:

Replace the file in your ghl-phone-validator repository with the updated ghl_audit.py above.

Protect the /audit Route (If Using Option 2 on ghl-abstract-webhook):

Require a secret header in app.py on ghl-abstract-webhook so external bots cannot trigger CRM tag writes:

Python
from flask import request, abort
import os
from ghl_audit import run_pipeline_audit

@app.route("/audit", methods=["POST"])
def trigger_audit():
    if request.headers.get("X-Audit-Secret") != os.getenv("AUDIT_SECRET"):
        abort(401)
    return run_pipeline_audit(), 200
Set Your Render Environment Variables:

Set GHL_API_KEY to the Private Integration Token stored in your GoHighLevel API Credentials note.

Set GHL_LOCATION_ID to your GHL Sub-Account Location ID (found in GHL under Settings > Business Profile).

Set SHEETS_WEBHOOK_URL to your Google Sheet's Apps Script Web App URL (if syncing to Sheets automatically).

Set AUDIT_SECRET to a random secret string (if triggering via the /audit endpoint).

Schedule for 5:45 AM Pacific:

Use 45 12 * * 1 (during PDT) or 45 13 * * 1 (starting November 1 when PST begins) so the audit completes 15 minutes ahead of your 6:00 AM Monday Gemini briefing.

Let me know if you'd like the 15-line Google Sheet doPost(e) snippet to generate your SHEETS_WEBHOOK_URL receiver.

ok so i am going to use the github and ghl route. How do that exactly. break it down

Here is the step-by-step breakdown to connect your ghl-phone-validator GitHub repository, your ghl-abstract-webhook Render service, and GoHighLevel.

Step 1: Grab Your GHL Location ID (1 Minute)
Open Sub-Account Settings: Log into GoHighLevel, switch into your sub-account, and click Settings (bottom-left gear icon) > Business Profile.

Copy the Location ID: Copy the alphanumeric Location ID displayed right under your business name in the General Information box.

Step 2: Add the Audit Code to GitHub (3 Minutes)
Upload ghl_audit.py: Download ghl_audit.py from the file card above, open your ghl-phone-validator repo on GitHub, click Add file > Upload files, drag in ghl_audit.py, and click Commit changes.

Edit app.py: Open app.py in your repository, click the pencil icon (Edit this file), and paste this route right above if __name__ == "__main__"::

Python
from flask import request, jsonify, abort
import os
from ghl_audit import run_pipeline_audit

@app.route("/audit", methods=["POST"])
def trigger_audit():
    if request.headers.get("X-Audit-Secret") != os.getenv("AUDIT_SECRET"):
        abort(401)
    summary = run_pipeline_audit()
    return jsonify(summary), 200
Check requirements.txt: Open requirements.txt in your repo and verify that flask, gunicorn, and requests are each listed on their own line, then commit your changes.

Step 3: Add Your Keys in Render (2 Minutes)
Open Environment Settings: Go to your ghl-abstract-webhook dashboard on Render and click Environment in the left sidebar.

Add Three Environment Variables: Click Add Environment Variable and enter:

Key: GHL_API_KEY → Value: Paste the pit-us-... token from your GoHighLevel API Credentials note.

Key: GHL_LOCATION_ID → Value: Paste your Location ID from Step 1.

Key: AUDIT_SECRET → Value: Pick a secret passcode (for example, avin-audit-2026).

Deploy and Copy URL: Click Save Changes (Render will automatically deploy your latest GitHub commit) and copy your service's .onrender.com URL at the top of the page.

Step 4: Trigger the Audit (Two Ways)
You can trigger the audit either from GoHighLevel (calling Render) or directly inside GitHub Actions (which runs ghl_audit.py on GitHub's servers for free without needing Render at all):

Trigger Method	How to Set It Up
Option A: GHL Workflow → Render	
1. In GHL, go to Automation > Workflows > + Create Workflow > Start from Scratch.


2. Add a recurring trigger or schedule window for Mondays at 5:45 AM.


3. Add the Custom Webhook action (POST method) pointing to https://<your-render-url>[.onrender.com/audit](https://.onrender.com/audit).


4. Under Headers, add key X-Audit-Secret with value avin-audit-2026, click Test Webhook, and click Publish.

Option B: Pure GitHub Actions (No Render Needed)	
1. In your GitHub repo, go to Settings > Secrets and variables > Actions > New repository secret, and add GHL_API_KEY and GHL_LOCATION_ID.


2. Click Add file > Create new file, name it .github/workflows/weekly_audit.yml, and paste the workflow below.


3. Click the Actions tab in GitHub and click Run workflow anytime to test on demand.

If you choose Option B (GitHub Actions), paste this into .github/workflows/weekly_audit.yml:

YAML
name: GHL Weekly Pipeline Audit

on:
  schedule:
    - cron: "45 12 * * 1" # Runs Mondays at 5:45 AM Pacific (PDT)
  workflow_dispatch:      # Adds a "Run workflow" button in GitHub

jobs:
  run-audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install requests
      - run: python ghl_audit.py
        env:
          GHL_API_KEY: ${{ secrets.GHL_API_KEY }}
          GHL_LOCATION_ID: ${{ secrets.GHL_LOCATION_ID }}
          SHEETS_WEBHOOK_URL: ${{ secrets.SHEETS_WEBHOOK_URL }}
Step 5: Sync Results to Google Sheets (Optional, 2 Minutes)
If you want the script to populate your Google Sheet automatically so Gemini can read the table and email your Monday executive summary:

Create the Sheet: Open a new Google Sheet titled GHL Weekly Pipeline Audit and click Extensions > Apps Script.

Paste the Receiver: Replace the code in Code.gs with:

JavaScript
function doPost(e) {
  const data = JSON.parse(e.postData.contents);
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  ["stale_leads", "incomplete_data", "unassigned_followups"].forEach(key => {
    let sheet = ss.getSheetByName(key) || ss.insertSheet(key);
    sheet.clear();
    const rows = data[key] || [];
    if (rows.length > 0) {
      const headers = Object.keys(rows[0]);
      sheet.appendRow(headers);
      rows.forEach(r => sheet.appendRow(headers.map(h => r[h])));
    }
  });
  return ContentService.createTextOutput("OK");
}
Deploy Web App: Click Deploy > New deployment > Select type: Web app > Set Who has access to Anyone > Click Deploy, copy the Web app URL, and add it as SHEETS_WEBHOOK_URL in Render (or GitHub Secrets).





Gemini is AI and can make mistakes.

"""
GoHighLevel (GHL) Pipeline Hygiene Audit Script (v2 - Corrected)
Author: Avin Prasad / Gemini Spark
Purpose:
  1. Map pipeline stage IDs via /opportunities/pipelines
  2. Paginate through all opportunities and contacts (600+ records)
  3. Detect stale leads (7+ days inactive in active stages)
  4. Validate phone formatting (E.164/10-digit), email, and lead source tags
  5. Check /conversations/search and /contacts/{id}/tasks for 48h inbound unassigned leads
  6. Apply maintenance tags idempotently in GHL
  7. Push results to Google Sheets webhook so Gemini Spark can read and email the summary
"""

import os
import re
import sys
import time
import datetime
import requests

GHL_API_KEY = os.getenv("GHL_API_KEY")
GHL_LOCATION_ID = os.getenv("GHL_LOCATION_ID")
SHEETS_WEBHOOK_URL = os.getenv("SHEETS_WEBHOOK_URL")  # Optional: Apps Script Web App URL to write sheet

BASE_URL = "https://services.leadconnectorhq.com"
HEADERS = {
    "Authorization": f"Bearer {GHL_API_KEY}",
    "Version": "2021-07-28",
    "Content-Type": "application/json",
    "Accept": "application/json",
}

ACTIVE_STAGE_NAMES = {"new lead", "attempted contact", "appointment booked"}
PHONE_REGEX = re.compile(r"^\+?1?\d{10,14}$")


def ghl_request(method, path, params=None, json_body=None):
    """Wrapper with basic rate-limit backoff (GHL v2 allows ~10 req/sec)."""
    url = f"{BASE_URL}{path}"
    for attempt in range(3):
        res = requests.request(method, url, headers=HEADERS, params=params, json=json_body, timeout=30)
        if res.status_code == 429:
            time.sleep(2 ** attempt)
            continue
        res.raise_for_status()
        return res.json()
    raise RuntimeError(f"Rate limit exceeded on {path}")


def get_pipeline_stage_map():
    """Fetch pipelines and return a dict mapping stage_id -> stage_name."""
    stage_map = {}
    try:
        data = ghl_request("GET", "/opportunities/pipelines", params={"locationId": GHL_LOCATION_ID})
        for pipeline in data.get("pipelines", []):
            for stage in pipeline.get("stages", []):
                stage_map[stage.get("id")] = stage.get("name", "")
    except Exception as e:
        print(f"Error fetching pipelines: {e}")
    return stage_map


def get_all_opportunities():
    """Paginate through all opportunities in the location."""
    opportunities = []
    params = {"location_id": GHL_LOCATION_ID, "limit": 100, "status": "open"}
    while True:
        try:
            data = ghl_request("GET", "/opportunities/search", params=params)
            batch = data.get("opportunities", [])
            opportunities.extend(batch)
            meta = data.get("meta", {})
            next_start_after = meta.get("startAfter")
            next_start_after_id = meta.get("startAfterId")
            if not batch or len(batch) < 100 or not (next_start_after and next_start_after_id):
                break
            params["startAfter"] = next_start_after
            params["startAfterId"] = next_start_after_id
        except Exception as e:
            print(f"Error paginating opportunities: {e}")
            break
    return opportunities


def get_all_contacts():
    """Paginate through all contacts in the location."""
    contacts = []
    params = {"locationId": GHL_LOCATION_ID, "limit": 100}
    while True:
        try:
            data = ghl_request("GET", "/contacts/", params=params)
            batch = data.get("contacts", [])
            contacts.extend(batch)
            meta = data.get("meta", {})
            start_after = meta.get("startAfter")
            start_after_id = meta.get("startAfterId")
            if not batch or len(batch) < 100 or not (start_after and start_after_id):
                break
            params["startAfter"] = start_after
            params["startAfterId"] = start_after_id
        except Exception as e:
            print(f"Error paginating contacts: {e}")
            break
    return contacts


def get_recent_inbound_conversations(forty_eight_hours_ago_ms):
    """Query conversations with recent inbound messages."""
    inbound_convos = []
    params = {"locationId": GHL_LOCATION_ID, "limit": 100}
    try:
        data = ghl_request("GET", "/conversations/search", params=params)
        for conv in data.get("conversations", []):
            direction = conv.get("lastMessageDirection")
            msg_date_ms = conv.get("lastMessageDate")  # Epoch ms in GHL v2
            if direction == "inbound" and msg_date_ms and msg_date_ms >= forty_eight_hours_ago_ms:
                inbound_convos.append(conv)
    except Exception as e:
        print(f"Error fetching conversations: {e}")
    return inbound_convos


def has_upcoming_task(contact_id):
    """Check if contact has at least one incomplete task reminder."""
    try:
        data = ghl_request("GET", f"/contacts/{contact_id}/tasks")
        for task in data.get("tasks", []):
            if not task.get("completed", False):
                return True
    except Exception as e:
        print(f"Error checking tasks for {contact_id}: {e}")
    return False


def apply_tag_if_missing(contact_id, existing_tags, new_tag):
    """Idempotently apply a maintenance tag only if not already present."""
    existing_lower = {t.lower() for t in (existing_tags or [])}
    if new_tag.lower() in existing_lower:
        return
    try:
        ghl_request("POST", f"/contacts/{contact_id}/tags", json_body={"tags": [new_tag]})
    except Exception as e:
        print(f"Error tagging contact {contact_id} with {new_tag}: {e}")


def is_valid_phone(phone_str):
    """Validate phone string formatting (strips punctuation and checks 10-14 digits)."""
    if not phone_str:
        return False
    cleaned = re.sub(r"[\s\-\(\)\.]", "", str(phone_str))
    return bool(PHONE_REGEX.match(cleaned))


def run_pipeline_audit():
    now = datetime.datetime.now(datetime.timezone.utc)
    seven_days_ago = now - datetime.timedelta(days=7)
    forty_eight_hours_ago_ms = int((now - datetime.timedelta(hours=48)).timestamp() * 1000)

    stage_map = get_pipeline_stage_map()
    opportunities = get_all_opportunities()
    contacts = get_all_contacts()
    contact_lookup = {c.get("id"): c for c in contacts if c.get("id")}

    stale_leads = []
    incomplete_data = []
    unassigned_followups = []

    # 1. Stale Lead Detection
    for opp in opportunities:
        stage_id = opp.get("pipelineStageId")
        stage_name = stage_map.get(stage_id, "")
        if stage_name.strip().lower() not in ACTIVE_STAGE_NAMES:
            continue

        updated_str = opp.get("lastStatusChangeAt") or opp.get("updatedAt") or opp.get("createdAt")
        contact_id = opp.get("contactId") or opp.get("contact", {}).get("id")
        if not updated_str:
            continue

        try:
            updated_at = datetime.datetime.fromisoformat(updated_str.replace("Z", "+00:00"))
            if updated_at < seven_days_ago:
                days_inactive = (now - updated_at).days
                stale_leads.append({
                    "contact_id": contact_id,
                    "name": opp.get("name"),
                    "stage": stage_name,
                    "days_inactive": days_inactive,
                    "last_activity": updated_str,
                })
                if contact_id:
                    existing_tags = contact_lookup.get(contact_id, {}).get("tags", [])
                    apply_tag_if_missing(contact_id, existing_tags, "audit-flagged-stale")
        except ValueError:
            pass

    # 2. Data Hygiene & Missing Fields
    for c in contacts:
        contact_id = c.get("id")
        phone = c.get("phone")
        email = c.get("email")
        source = c.get("source")
        tags = c.get("tags", [])

        issues = []
        if not is_valid_phone(phone):
            issues.append("invalid_or_missing_phone")
        if not email or "@" not in str(email):
            issues.append("missing_email")
        if not source and not tags:
            issues.append("missing_lead_source_or_tags")

        if issues:
            incomplete_data.append({
                "contact_id": contact_id,
                "name": f"{c.get('firstName', '')} {c.get('lastName', '')}".strip() or "Unnamed",
                "issues": ", ".join(issues),
            })
            if contact_id:
                apply_tag_if_missing(contact_id, tags, "audit-missing-data")

    # 3. Unassigned Follow-Up Flags (48h inbound without assignee or active task)
    inbound_convos = get_recent_inbound_conversations(forty_eight_hours_ago_ms)
    for conv in inbound_convos:
        contact_id = conv.get("contactId")
        assigned_to = conv.get("assignedTo")
        has_task = has_upcoming_task(contact_id) if contact_id else False

        if not assigned_to or not has_task:
            c = contact_lookup.get(contact_id, {})
            unassigned_followups.append({
                "contact_id": contact_id,
                "name": conv.get("contactName") or f"{c.get('firstName', '')} {c.get('lastName', '')}".strip(),
                "assigned_to": assigned_to or "Unassigned",
                "has_upcoming_task": has_task,
            })
            if contact_id:
                apply_tag_if_missing(contact_id, c.get("tags", []), "audit-unassigned-followup")

    summary = {
        "audit_date": now.strftime("%Y-%m-%d"),
        "counts": {
            "stale_leads": len(stale_leads),
            "incomplete_data": len(incomplete_data),
            "unassigned_followups": len(unassigned_followups),
        },
        "stale_leads": stale_leads,
        "incomplete_data": incomplete_data,
        "unassigned_followups": unassigned_followups,
    }

    # 4. Optional push to Google Sheets Webhook so Gemini Spark can access the sheet
    if SHEETS_WEBHOOK_URL:
        try:
            requests.post(SHEETS_WEBHOOK_URL, json=summary, timeout=30)
        except Exception as e:
            print(f"Error pushing to Google Sheets webhook: {e}")

    return summary


if __name__ == "__main__":
    if not GHL_API_KEY or not GHL_LOCATION_ID:
        print("ERROR: GHL_API_KEY and GHL_LOCATION_ID environment variables are required.")
        sys.exit(1)
    result = run_pipeline_audit()
    print(f"Audit Complete: {result['counts']}")
ghl_audit.py
Displaying ghl_audit.py.
