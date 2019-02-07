from aqeapis.ver1 import BaseCategoriesV1
from aqeapis.ver2 import BaseCategoriesV2
from aqeconfigs.dataclasses import UserInfo
from app.helpers.constants import PAGELIMIT


def _get_v1_categories(user: UserInfo, category_id: str) -> dict:
    """
    Gets classes @ /api/v1/categories

    :param user:
    :param category_id:
    :return:
    """
    # Get /v1/categories
    categoriesv1_api = BaseCategoriesV1(user)
    return categoriesv1_api.get_category(category_id)


def _get_v2_categories(user: UserInfo, category_id: str, expected_classes: int) -> list:
    """
    Gets classes @ /api/v2/categories

    :param user:
    :param category_id:
    :param expected_classes:
    :return:
    """
    v2_workouts = []
    v2_pages = (expected_classes // PAGELIMIT) + 1

    categoriesv2_api = BaseCategoriesV2(user)

    for i in range(1, v2_pages + 1):
        categories_v2 = categoriesv2_api.get_category(category_id, params={'pageLimit': PAGELIMIT, 'pageOffset': i})
        v2_workouts.extend(categories_v2['workouts'])

    return v2_workouts


def get_categoryies(user: UserInfo, category_id: str) -> (dict, list):
    """
    Returns both v1 and v2 categories

    :param user:
    :param category_id:
    :return:
    """
    v1_categories_resp = _get_v1_categories(user, category_id)
    v2_category_resp = _get_v2_categories(user, category_id, len(v1_categories_resp['children']))

    return (v1_categories_resp, v2_category_resp)
