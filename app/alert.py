import aaptivsecrets
from aqeconfigs.dataclasses import UserInfo
from app.helpers import analysis, categories, constants, slack


CONFIG = aaptivsecrets.get_env_var_dict_for_app('dev', "contentservicealert")


def check_category(user: UserInfo, category_id: str):
    analysis_result = analysis.compare_categories(*categories.get_categoryies(user, category_id))

    if analysis_result:
        slack.send_slack_msg(CONFIG['SLACK_TOKEN'], CONFIG['CHANNEL_ID'], attachments=[analysis_result])
    else:
        slack.send_slack_msg(CONFIG['SLACK_TOKEN'], CONFIG['INFO_CHANNEL_ID'], message=f'Processing completed for {category_id}')
