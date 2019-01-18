import re
from slackbot.bot import respond_to
from slackbot.bot import Bot

@respond_to('help', re.IGNORECASE)
def help(message):
    message.reply("Default help message")


def main():
    bot = Bot()
    bot.run()


if __name__ == "__main__":
    main()
