from app.helpers.slack import send_slack_msg
from tests.utilities.fixtures import envconfigs   # noqa: F401


MESSAGE = "Hello world!"
ATTACHMENT_DICT = [{"pretext": "pre-hello",
                    "color": "#448aff",
                    "text": "text-world"}]


def test_send_slack_msg_only_message(envconfigs):  # noqa: F811
    send_slack_msg(envconfigs['API_TOKEN'], envconfigs['CHANNEL_ID'], MESSAGE)


def test_send_slack_msg_only_attachment(envconfigs):  # noqa: F811
    send_slack_msg(envconfigs['API_TOKEN'], envconfigs['CHANNEL_ID'], attachments=ATTACHMENT_DICT)


def test_send_slack_msg_both(envconfigs):  # noqa: F811
    send_slack_msg(envconfigs['API_TOKEN'], envconfigs['CHANNEL_ID'], message=MESSAGE, attachments=ATTACHMENT_DICT)
