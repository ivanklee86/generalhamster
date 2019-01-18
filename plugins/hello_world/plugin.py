from slackbot.bot import respond_to

@respond_to('Hello slackbot!')
def hello_world(message):
    message.reply("Hello world!")
