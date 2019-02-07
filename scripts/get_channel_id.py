import os
import aaptivsecrets
from slackclient import SlackClient


CONFIG = aaptivsecrets.get_env_var_dict_for_app('dev', "contentservicealert")
slack_token = CONFIG["SLACK_TOKEN"]
sc = SlackClient(slack_token)
channels = sc.api_call("channels.list", exclude_archived=1)

for channel in channels['channels']:
    print(f"{channel['name']}: {channel['id']}")
