from date_check import is_past_expiration_by
from update_user_attribute import update_user_attribute
from get_ad_users import retrieving_list_of_users_by_department_name
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
import requests
import datetime

def inspection_process_management(kv_uri,department,days):
    tenant_id,client_id,client_secret,application_id=get_data_from_key_vault_secret(kv_uri)
    access_token=get_access_token(tenant_id, client_id, client_secret)
    if access_token:
        try:
            sending_users_for_testing(access_token,department,days,application_id)
        except Exception as e:
            return "sending_users_for_testing does not succeed"
    else:
        return "Failed to obtain access token"
    
def get_data_from_key_vault_secret(KVUri):
    client = SecretClient(vault_url=KVUri, credential=DefaultAzureCredential())
    tenant_id=client.get_secret('TENANT_ID').value
    client_id=client.get_secret('CLIENT_ID').value
    client_secret=client.get_secret('CLIENT_SECRET').value
    application_id=client.get_secret('APPLICATION_ID').value
    return tenant_id,client_id,client_secret,application_id

def get_access_token(tenant_id, client_id, client_secret):
    try:
        url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'client_secret': client_secret,
            'scope': 'https://graph.microsoft.com/.default'
        }
        response = requests.post(url, headers=headers, data=data)
        access_token = response.json().get('access_token')
        return access_token
    except Exception:
        raise Exception("Failed to get access token")

def sending_users_for_testing(access_token,department,days,application_id):
    users=retrieving_list_of_users_by_department_name(access_token,department,'extension_'+application_id+'_expiration_date')
    for user in users:
        user_expiration_date_check(access_token,user,days,application_id)
    
def user_expiration_date_check(access_token,user,days,application_id):
    attribute_name = f"extension_{application_id}_expiration_date"
    if(attribute_name in user):
        is_past_expiration_by(days,user[attribute_name], access_token,user['id'],attribute_name)
    else:
        update_user_attribute(access_token, user['id'],attribute_name, datetime.date.today())
