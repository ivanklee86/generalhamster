from app.helpers.login import get_user
from tests.utilities.fixtures import configs   # noqa: F401


def test_login(configs):  # noqa: F811
    user = get_user(configs['USER_EMAIL'], configs['USER_PASSWORD'])

    assert user.secret
    assert user.visitor_id
