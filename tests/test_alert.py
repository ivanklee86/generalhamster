from app import alert
from app.helpers import constants
from tests.utilities.fixtures import generated_user   # noqa: F401


def test_alert(generated_user):  # noqa: F811
    alert.check_category(generated_user, constants.STRETCHING['id'])
