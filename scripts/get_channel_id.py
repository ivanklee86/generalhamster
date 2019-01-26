import os
from dotenv import load_dotenv
from slackclient import SlackClient


load_dotenv()
slack_token = os.environ["API_TOKEN"]
sc = SlackClient(slack_token)
channels = sc.api_call("channels.list", exclude_archived=1)

for channel in channels['channels']:
    print(f"{channel['name']}: {channel['id']}")
