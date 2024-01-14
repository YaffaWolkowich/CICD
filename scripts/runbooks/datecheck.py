import datetime
from updateuserattribute import update_user_attribute

def is_past_expiration_by(days: int, date, access_token, user_id,attribute_name):
    desired_date = adding_days_to_date(days,date)
    disable_user_by_expiration(desired_date,access_token,user_id,attribute_name)

def adding_days_to_date(days: int, date):
    required_date = date + datetime.timedelta(days=int(days))
    return required_date

def disable_user_by_expiration(date,access_token,user_id,attribute_name):
    if datetime.date.today() > date:
        try:
            update_user_attribute(access_token, user_id, "accountEnabled", "string" )
            update_user_attribute(access_token, user_id, attribute_name, "string" )
        except Exception:
            return

