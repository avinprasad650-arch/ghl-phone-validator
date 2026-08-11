const express = require('express');
const axios = require('axios');
const app = express();

// Middleware to parse JSON payloads from GoHighLevel
app.use(express.json());

// Secure environment variables
const ABSTRACT_API_KEY = process.env.ABSTRACT_API_KEY;
const GHL_API_TOKEN = process.env.GHL_API_TOKEN;

app.post('/validate-phone', async (req, res) => {
    try {
        const phone = req.body.phone;
        const contactId = req.body.contact_id;

        // Immediately acknowledge receipt to GHL to prevent webhook timeouts
        res.status(200).send('Webhook received and processing');

        // Abstract API Premium Phone Intelligence Endpoint
        const lookupUrl = `https://phoneintelligence.abstractapi.com/v1/?api_key=${ABSTRACT_API_KEY}&phone=${phone}`;
        const lookupResponse = await axios.get(lookupUrl);
        const data = lookupResponse.data;
        
        // 1. Extract Premium Data Points
        const lineType = data.phone_carrier?.line_type ? data.phone_carrier.line_type.toLowerCase() : 'unknown';
        const isVoip = data.phone_validation?.is_voip === true;
        const isValid = data.phone_validation?.is_valid === true;
        const lineStatus = data.phone_validation?.line_status ? data.phone_validation.line_status.toLowerCase() : 'unknown';

        // 2. Cross-Reference Logic (Validate data against multiple conditions)
        const isLandline = lineType.includes('landline');
        const isDeadNumber = !isValid || lineStatus !== 'active';

        // 3. The Ultimate Bad Number Trap
        if (isLandline || isVoip || isDeadNumber) {
            
            // Inject Tag via GoHighLevel API v2
            const ghlTagUrl = `https://services.leadconnectorhq.com/contacts/${contactId}/tags`;
            
            await axios.post(ghlTagUrl, 
                { 
                    tags: ["invalid-landline"] 
                }, 
                { 
                    headers: { 
                        'Authorization': `Bearer ${GHL_API_TOKEN}`, 
                        'Version': '2021-07-28',
                        'Content-Type': 'application/json'
                    } 
                }
            );
            console.log(`🚫 Tagged ${contactId} as invalid. (Type: ${lineType}, VoIP: ${isVoip}, Active: ${lineStatus})`);
        } else {
            console.log(`✅ Contact ${contactId} is a valid, active mobile number. No tags applied.`);
        }

    } catch (error) {
        if (error.response) {
            console.error(`🚨 FAILED API URL: ${error.config.url}`);
            console.error(`🚨 ERROR REASON: ${JSON.stringify(error.response.data)}`);
        } else {
            console.error('Error processing validation webhook:', error.message);
        }
    }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Premium Validation Engine running on port ${PORT}`));
