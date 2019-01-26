import re
from app.constants import VERSION
from slackbot.bot import respond_to


@respond_to('status', re.IGNORECASE)
def status(message):
    message.reply(f"Hello!  I am a slackbot, version {VERSION}")
