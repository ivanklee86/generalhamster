import app.helpers.categories as categories
from app.helpers import constants
from tests.utilities.fixtures import generated_user   # noqa: F401


def test_get_v1_categories(generated_user):  # noqa: F811
    category_info = categories._get_v1_categories(generated_user, constants.STRETCHING['id'])

    assert len(category_info['children']) > 0


def test_get_v2_categories(generated_user):  # noqa: F811
    v1_categoreis = categories._get_v1_categories(generated_user, constants.STRETCHING['id'])

    category_info = categories._get_v2_categories(generated_user,
                                                  constants.STRETCHING['id'],
                                                  len(v1_categoreis['children']))

    assert len(category_info) > 0


def test_get_categories(generated_user):  # noqa: F811
    (v1, v2) = categories.get_categoryies(generated_user, constants.STRETCHING['id'])

    assert len(v1['children']) > 0
    assert len(v2) > 0
