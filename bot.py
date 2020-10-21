from handlers.slack_commands import handle_command

from flask import Flask, Response, request
import json
import os
from threading import Thread
from slack import WebClient
from slackeventsapi import SlackEventAdapter


# Start Flask app that will be produce all the requests
app = Flask(__name__)

# Get venv variables
SLACK_BOT_SIGNIN_TOKEN = os.environ['SLACK_BOT_SIGNIN_TOKEN']
SLACK_BOT_ACCESS_TOKEN = os.environ['SLACK_BOT_ACCESS_TOKEN']
SLACK_BOT_VERIFICATION_TOKEN = os.environ['SLACK_BOT_VERIFICATION_TOKEN']

# Get slack api client
slack_client = WebClient(SLACK_BOT_ACCESS_TOKEN)

# Enable several routes to the server
@app.route("/")
def event_hook(request):
    """
    Main hook that checks all the request with Slack token.
    """
    json_dict = json.loads(request.body.decode("utf-8"))
    if json_dict["token"] != SLACK_BOT_VERIFICATION_TOKEN:
        return {"status": 403}

    if "type" in json_dict:
        if json_dict["type"] == "url_verification":
            response_dict = {"challenge": json_dict["challenge"]}
            return response_dict
    return {"status": 500}

@app.route('/slack/commands', methods=['POST'])
def command_hook():
    """
    Function to handle all the bots commands.
    """
    handle_command(slack_client, request.form)
    return Response(status=200)

@app.route('/slack/interactivity', methods=['POST'])
def interactivity_hook():
    """
    Function, that handles all the interactivity (buttons, checkboxes, slack shortcuts, etc.)
    """
    print(request.values)
    return Response(status=200)

# Get adabter to process slack events
slack_events_adapter = SlackEventAdapter(
    SLACK_BOT_SIGNIN_TOKEN, "/slack/events", app
)  

# If bot is mentioned event
@slack_events_adapter.on("app_mention")
def handle_message(event_data):
    def send_reply(value):
        event_data = value
        message = event_data["event"]

        if message.get("subtype") is None: # subtype is for bots.
            pass
    thread = Thread(target=send_reply, kwargs={"value": event_data})
    thread.start()
    return Response(status=200)


if __name__ == "__main__":
  app.run(port=3000)