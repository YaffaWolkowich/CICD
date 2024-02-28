from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv
import os


load_dotenv()

keyvault_uri = os.getenv("KEYVAULT_URI")
secret_name = os.getenv("SECRET")
excel_secret_name = os.getenv("SECRET_EXCEL")
credential = DefaultAzureCredential()
client = SecretClient(vault_url=keyvault_uri, credential=credential)
secret = client.get_secret(secret_name)
connection_string = secret.value
excel_secret = client.get_secret(excel_secret_name)
# excel_connection_string = "DefaultEndpointsProtocol=https;AccountName=myfirsttrail;AccountKey=bz3aax2d3IX7b3ngkc73W+CqpzKRvUj4So1zAuUxlrpGDuzPDeOGT7tdwD4UiLzSu9iBO6jT6c69+AStETr8tg==;EndpointSuffix=core.windows.net"
excel_connection_string = excel_secret.value
http_trigger_url = os.getenv("HTTP_TRIGGER_URL")
deleted_accounts_table = os.getenv("DELETED_ACCOUNTS_TABLE")
documentation_table = os.getenv("DOCUMENTATION_TABLE")
main_manager = os.getenv("MAIN_MANAGER")
