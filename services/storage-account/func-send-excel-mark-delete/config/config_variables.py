from dotenv import load_dotenv
import os


load_dotenv()

keyvault_uri = os.getenv("KEYVAULT_URI")
secret_name = os.getenv("SECRET")
excel_secret_name = os.getenv("SECRET_EXCEL")
http_trigger_url = os.getenv("HTTP_TRIGGER_URL")
deleted_accounts_table = os.getenv("DELETED_ACCOUNTS_TABLE")
documentation_table = os.getenv("DOCUMENTATION_TABLE")
main_manager = os.getenv("MAIN_MANAGER")
