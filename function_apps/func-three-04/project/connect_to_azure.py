from azure.core.exceptions import ResourceNotFoundError
from azure.data.tables import TableClient
from azure.identity import DefaultAzureCredential
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.monitor import MonitorManagementClient
import pandas as pd

from config.config_variables import connection_string



def upload_to_table(my_table_name, my_entity):
    table_client = TableClient.from_connection_string(
        connection_string, table_name=my_table_name
    )
    table_client.create_entity(entity=my_entity)
    return True
