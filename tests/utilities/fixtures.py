import os
import pytest
from dotenv import load_dotenv


@pytest.fixture()
def envconfigs():
    load_dotenv()

    configs = {
        'API_TOKEN': os.environ['API_TOKEN'],
        'CHANNEL_ID': os.environ['CHANNEL_ID'],
    }

    yield configs
