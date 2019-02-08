import os
from multiprocessing import Pool
from dotenv import load_dotenv
import aaptivsecrets
import app.alert as alert
from app.helpers import constants
from app.helpers import login


load_dotenv(override=True)
CONFIGS = aaptivsecrets.get_env_var_dict_for_app(os.environ['AAPTIVSECRETS_ENV'], "contentservicealert")
USER = login.get_user(CONFIGS['USER_EMAIL'], CONFIGS['USER_PASSWORD'])


if __name__ == '__main__':
    with Pool(len(constants.CATEGORIES)) as p:
        p.starmap(alert.check_category, [(USER, x['id']) for x in constants.CATEGORIES])
