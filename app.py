from flask import Flask, request, jsonify

app = Flask(__name__)

# Home route returns student number as JSON
@app.route('/', methods=['GET'])
def home():
    # Replace with your actual student number
    return jsonify({"student_number": "200612909"})

# Webhook route for Dialogflow fulfillment
@app.route('/webhook', methods=['POST'])
def webhook():
    # Parse the incoming JSON from Dialogflow
    req = request.get_json(force=True)
    print("Request received:", req)  # For debugging purposes
    
    # You can process the request as needed. Here we provide a fixed response.
    fulfillment_text = "This is the response from your webhook fulfillment!"
    
    # Build and return the response payload in Dialogflow's expected format.
    return jsonify({
        "fulfillmentText": fulfillment_text
    })

if __name__ == '__main__':
    app.run(debug=True)
