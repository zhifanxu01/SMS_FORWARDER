from flask import Flask, request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

# Read Twilio credentials and phone numbers from environment variables
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = os.environ.get('+61489088639')
FORWARD_TO = os.environ.get('+61422260365')  # Your personal number

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
