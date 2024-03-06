from dotenv import load_dotenv
import os

load_dotenv()

keyvault_uri = os.getenv("KEYVAULT_URI")
secret_name = os.getenv("SECRET")
documentation_table = os.getenv("DOCUMENTATION_TABLE")
