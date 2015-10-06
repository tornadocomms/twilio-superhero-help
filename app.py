# Title: Twilio SuperHero Helper
# Author: Mick Stevens
# Contact: +44 20 3095 6505 / mickstevens@yahoo.com
# Version: Eternal Draft!
# Notes: Unofficial Marvel Universe chatbot, inspired by @rickyrobinett's 'I am Groot' chatbot.
# SMS a message, including your chosen/favourite Marvel character name, to your Twilio no.
# and (if listed below) your character will reply with suggested course of action!
# If your chosen character is unavailable (not listed) you can add them by cut'n'pasting any
# two line elif statement below, replacing character/text to your preference.
# finally point your Twilio Messaging App/URL to yourdomain.com/marvelhelp (see lines 21-22 below)
# All constructive feedback from the Pythonista community welcome (be nice! :)    )

from flask import Flask
from flask import request
from twilio import twiml
from twilio.rest import TwilioRestClient
import os

app = Flask(__name__)

@app.route('/marvelhelp', methods=['POST'])
def marvelhelp():
     # replace xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx with your Twilio account_sid
    account_sid = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    # replace yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy with your Twilio auth_token
    auth_token  = "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"
    body = request.form['Body']
    from_number = request.form['From']
    client = TwilioRestClient(account_sid, auth_token)
    resp = twiml.Response()
    # replace zzzzzzzzzzz with your Twilio No.
    twilio_no = "+zzzzzzzzzzz"

    if "SPIDE" in body.upper():
        message = client.messages.create(to=from_number, from_=twilio_no,body="Spidey says 'with Great Power comes Great Responsibility.'")
    elif "BANNER" in body.upper():
        message = client.messages.create(to=from_number, from_=twilio_no,body="Bruce Banner says 'don't make me angry, you wouldn't like me when I'm angry.'")
    elif "BEAST" in body.upper():
        message = client.messages.create(to=from_number, from_=twilio_no,body="The Beast says 'Oh my stars and garters.'")
    elif "CAPTAIN AMERICA" in body.upper():
        message = client.messages.create(to=from_number, from_=twilio_no,body="Cap says 'Believe in your country, but believe in yourself!'")
    elif "HAWKEYE" in body.upper():
        message = client.messages.create(to=from_number, from_=twilio_no,body="Hawkeye says 'I'm strictly a bow and arrow type.'")
    elif "HULK" in body.upper():
        message = client.messages.create(to=from_number, from_=twilio_no,body="Hulk says 'SMASH!'")
    elif "GROOT" in body.upper():
        message = client.messages.create(to=from_number, from_=twilio_no,body="Groot says 'I am Groot.'")
    elif "IRON" in body.upper():
        message = client.messages.create(to=from_number, from_=twilio_no,body="Iron-Man says'Patriotism doesn't automatically equal conservatism.'")
    elif "CAGE" in body.upper():
        message = client.messages.create(to=from_number, from_=twilio_no,body="Luke Cage says 'Sweet Christmas!'")
    elif "THING" in body.upper():
        message = client.messages.create(to=from_number, from_=twilio_no,body="The Thing says 'It's Clobberin' Time!'")
    elif "THOR" in body.upper():
        message = client.messages.create(to=from_number, from_=twilio_no,body="Thor says 'Stay thy hand! Tis the God of Thunder who doth command thee!'")
    elif "TORCH" in body.upper():
        message = client.messages.create(to=from_number, from_=twilio_no,body="The Human Torch says 'Flame On!'")
    elif "WIDOW" in body.upper():
        message = client.messages.create(to=from_number, from_=twilio_no,body="Black Widow says '...don't let the door hit you in the back on the way out!'")
    elif "WOLVERINE" in body.upper():
        message = client.messages.create(to=from_number, from_=twilio_no,body="Wolverine says 'I'm the best there is at what I do, but what I do best isn't very nice!'")
    else:
        message = client.messages.create(to=from_number, from_=twilio_no,body="Your chosen Hero is unavailable, please try again or visit https://github.com/mickstevens/twilio-superhero-help to add a Hero of your choice.")

    return str(resp)

if __name__ == "__main__":
    # Since this is a development project, we will keep debug on to make our
    # lives easier. We would want to configure our app more conservatively
    # in production.
    app.run("0.0.0.0", port = 3000)
    app.debug = False
    app.run()
