import json
from slackclient import SlackClient


def send_slack_msg(slack_token: str,
                   slack_channel: str,
                   message: str = '',
                   attachments: list = None) -> None:
    """
    General purpose function to send one-off Slack messages.

    :param slack_token: Slack token for bot user
    :param slack_channel: Slack channel for message
    :param message: Message to send to Slack
    :param attachments: Attachments (if desired)
    :return:
    """
    client = SlackClient(slack_token)

    client.api_call(
        "chat.postMessage",
        channel=slack_channel,
        text=message,
        attachments=json.dumps(attachments)
    )
