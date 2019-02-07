from app.helpers.slack import send_slack_msg
from tests.utilities.fixtures import configs   # noqa: F401


MESSAGE = "Hello world!"
ATTACHMENT_DICT = [{"pretext": "pre-hello",
                    "color": "#448aff",
                    "text": "text-world"}]


def test_send_slack_msg_only_message(configs):  # noqa: F811
    send_slack_msg(configs['SLACK_TOKEN'], configs['CHANNEL_ID'], MESSAGE)


def test_send_slack_msg_only_attachment(configs):  # noqa: F811
    send_slack_msg(configs['SLACK_TOKEN'], configs['CHANNEL_ID'], attachments=ATTACHMENT_DICT)


def test_send_slack_msg_both(configs):  # noqa: F811
    send_slack_msg(configs['SLACK_TOKEN'], configs['CHANNEL_ID'], message=MESSAGE, attachments=ATTACHMENT_DICT)
