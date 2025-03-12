import os
from flask import Flask, request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER")
FORWARD_TO = os.environ.get("FORWARD_TO")

client = Client(ACCOUNT_SID, AUTH_TOKEN)

@app.route("/sms", methods=['POST'])
def forward_sms():
    from_number = request.form.get('From')
    message_body = request.form.get('Body')

    # Forward to your number
    client.messages.create(
        body=f"From {from_number}: {message_body}",
        from_=TWILIO_NUMBER,
        to=FORWARD_TO
    )

    # Optional auto-reply to sender
    resp = MessagingResponse()
    resp.message("Thanks for messaging us. We'll get back to you shortly.")
    return str(resp)

@app.route("/", methods=["GET"])
def home():
    return "Twilio SMS forwarder running."

if __name__ == "__main__":
    app.run()
