from aqeapis.ver1 import BaseLoginV1
from aqeapis.ver1 import BaseIdsV1
from aqeconfigs.dataclasses import UserInfo


def get_user(email: str, password: str) -> UserInfo:
    """
    Returns logged in / experiment-ed user

    :param email:
    :param password:
    :return:
    """
    # Create my user
    user = UserInfo(name="Ivan Lee",
                       email=email,
                       password=password)

    # Create API objects
    login_api = BaseLoginV1(user)
    ids_api = BaseIdsV1(user)

    # Login
    login_request = login_api.generate_login_request()
    login_api.post_login(login_request)
    ids_api.set_user_xs_info(user)

    return user
