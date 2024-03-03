from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv
import os


load_dotenv()

# keyvault_uri = os.getenv("KEYVAULT_URI")
# secret_name = os.getenv("SECRET")
# excel_secret_name = os.getenv("SECRET_EXCEL")
# credential = DefaultAzureCredential()
# client = SecretClient(vault_url=keyvault_uri, credential=credential)
# secret = client.get_secret(secret_name)
# connection_string = secret.value
# excel_secret = client.get_secret(excel_secret_name)
# excel_connection_string = excel_secret.value
# http_trigger_url = os.getenv("HTTP_TRIGGER_URL")
# deleted_accounts_table = os.getenv("DELETED_ACCOUNTS_TABLE")
# documentation_table = os.getenv("DOCUMENTATION_TABLE")
main_manager = os.getenv("MAIN_MANAGER")
