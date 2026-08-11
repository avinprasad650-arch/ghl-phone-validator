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

        // Abstract API Phone Intelligence Endpoint
        const lookupUrl = `https://phoneintelligence.abstractapi.com/v1/?api_key=${ABSTRACT_API_KEY}&phone=${phone}`;
        const lookupResponse = await axios.get(lookupUrl);
        
        // Safely extract the nested carrier line type from the Phone Intelligence payload
        const carrierData = lookupResponse.data.phone_carrier || {};
        const rawType = carrierData.line_type || lookupResponse.data.line_type || 'unknown';
        const lineType = rawType.toLowerCase();

        // Conditional Logic: Uses .includes() to catch variations like "non-fixed voip"
        if (lineType.includes('landline') || lineType.includes('voip')) {
            
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
            console.log(`Successfully tagged ${contactId} as invalid-landline (Carrier Type: ${lineType}).`);
        } else {
            console.log(`Contact ${contactId} is a valid mobile number (Carrier Type: ${lineType}). No tags applied.`);
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
app.listen(PORT, () => console.log(`Phone Validation Engine running on port ${PORT}`));
