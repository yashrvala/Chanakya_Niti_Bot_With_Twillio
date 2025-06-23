from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from agent import agent  # from your LangChain setup
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route("/bot", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').strip()
    print(f"User asked: {incoming_msg}")
    
    response = agent.run(incoming_msg)
    
    twilio_response = MessagingResponse()
    msg = twilio_response.message()
    msg.body(f"🧠 Chanakya says:\n{response}")
    return str(twilio_response)

if __name__ == "__main__":
    app.run(debug=True)
