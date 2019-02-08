import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configurations
API_TOKEN = os.environ["API_TOKEN"]
DEFAULT_REPLY = "This is the default reply!"
ERRORS_TO = 'boterrors'

# Direct slack messages
CHANNEL_ID = os.environ["CHANNEL_ID"]

PLUGINS = [
    'slackbot.plugins',
    'plugins.status.plugin'
]
