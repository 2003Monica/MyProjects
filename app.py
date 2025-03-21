import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Home route returns your student number in JSON format
@app.route('/', methods=['GET'])
def home():
    return jsonify({"student_number": "200612909"})

# Webhook route for Dialogflow fulfillment
@app.route('/webhook', methods=['POST'])
def webhook():
    # Optionally, process the request from Dialogflow here
    req = request.get_json(force=True)
    fulfillment_text = "This is the response from your webhook fulfillment!"
    return jsonify({"fulfillmentText": "This is the response from your webhook fulfillment!"})

if __name__ == '__main__':
    # Bind to the port provided by the environment, default to 5000
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=True)
