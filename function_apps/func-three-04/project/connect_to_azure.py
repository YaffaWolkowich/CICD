from azure.core.exceptions import ResourceNotFoundError
from azure.data.tables import TableClient
from azure.identity import DefaultAzureCredential
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.monitor import MonitorManagementClient
import pandas as pd
import json
import logging

from config.config_variables import connection_string


def create_monitor_management_client(sub_id):
    monitor_client = MonitorManagementClient(
        credential=DefaultAzureCredential(), subscription_id=sub_id
    )
    return monitor_client


def create_storage_management_client(sub_id):
    storage_client = StorageManagementClient(
        credential=DefaultAzureCredential(), subscription_id=sub_id
    )
    return storage_client


def retrieve_data_from_table(
    flag, con_str, table_name, query_filter, parameters="None", select=["*"]
):
    logging.info(f"-------{table_name}--------------")
    try:
        table = TableClient.from_connection_string(con_str, table_name)
        queried_entities = table.query_entities(
            query_filter=query_filter, select=select, parameters=parameters
        )
        logging.info(f"<><><><><><><><><><><><><><><><><><><><><><{convert_to_json(queried_entities)}")
        return convert_to_json(queried_entities) if flag else queried_entities
    
    except ResourceNotFoundError:
        logging.warn("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        raise ResourceNotFoundError("This table does not exist")
    except Exception as e:
        logging.warn(f"exception {e}")


def convert_to_json(queried_entities):
    return list((json.loads(pd.Series.to_json(pd.Series(queried_entities)))).values())


def find_resource_group_name(storage_account_id):
    if storage_account_id.find("resourceGroups") != -1:
        resource_group_name = storage_account_id[
            storage_account_id.find("resourceGroups") + 15 : storage_account_id.find(
                "/", storage_account_id.find("resourceGroups") + 15
            )
        ]
    else:
        resource_group_name = ""
    return resource_group_name


def upload_to_table(my_table_name, my_entity):

    table_client = TableClient.from_connection_string(
        connection_string, table_name=my_table_name
    )
    table_client.create_entity(entity=my_entity)

    return True
