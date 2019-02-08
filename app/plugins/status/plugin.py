import re
from slackbot.bot import respond_to
from app.constants import VERSION


@respond_to('status', re.IGNORECASE)
def status(message):
    message.reply(f"Hello!  I am a slackbot, version {VERSION}")
