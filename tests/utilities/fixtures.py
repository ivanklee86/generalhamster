import pytest
from dotenv import load_dotenv
import aaptivsecrets
from app.helpers.login import get_user
from app.helpers.categories import get_categoryies
from app.helpers.constants import OUTDOORRUNNING


@pytest.fixture()
def configs():
    load_dotenv(override=True)
    yield aaptivsecrets.get_env_var_dict_for_app('dev', "contentservicealert")


@pytest.fixture()
def generated_user():
    load_dotenv(override=True)
    configs = aaptivsecrets.get_env_var_dict_for_app('dev', "contentservicealert")
    yield get_user(configs['USER_EMAIL'], configs['USER_PASSWORD'])


@pytest.fixture()
def categories_data():
    load_dotenv(override=True)
    configs = aaptivsecrets.get_env_var_dict_for_app('dev', "contentservicealert")
    user = get_user(configs['USER_EMAIL'], configs['USER_PASSWORD'])
    yield get_categoryies(user, OUTDOORRUNNING['id'])
