import azure.functions as func
import logging

# import os
# import sys
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from azure.data.tables import TableClient
from config.config_variables import documentation_storage_name
from project.storage_account_test import *
from config.config_variables import connection_string


def func_three_04():
    answer=storage_account_test(
        "storage_account",
        1,
        2,
        "subscription_id",
        "subscription_name",
        "storage_account",
        "last_fetch_time"
    )

    logging.info(f"answer: {answer}")
    return func.HttpResponse(
        f"This HTTP triggered function -{answer}",
        status_code = 200
    )


def storage_account_test(
    storage_account,
    partitionKey,
    row_key,
    subscription_id,
    subscription_name,
    storage_account_id,
    last_fetch_time,
):
    entity = create_object_for_documentation_table(
        str(partitionKey),
        str(row_key),
        datetime.today(),
        subscription_id,
        'resource_group_name',
        storage_account,
        "current_used_storage_capacity",
        "last_fetch_time",
        "alert",
        "alert_reason_for_check_used_capacity",
        "alert",
        "alert_reason_for_check_last_fetch",
    )
    logging.warn("entity")
    logging.warn(entity)
    ans=upload_to_table(documentation_table, entity)
    logging.warn(f"VVV {ans}")
    return ans




def create_object_for_documentation_table(
    partitionKey,
    row_key,
    test_date,
    subscription_id,
    resource_group,
    storage_name,
    current_storage_used_capacity,
    last_storage_fetch_time,
    alert_for_check_used_capacity,
    alert_reason_for_check_used_capacity,
    alert_for_check_last_fetch,
    alert_reason_for_check_last_fetch,
):
    obj = {
        "PartitionKey": partitionKey,
        "RowKey": row_key,
        "test_date": test_date,
        "subscription_id": subscription_id,
        "resource_group": resource_group,
        "storage_name": storage_name,
        "used_storage_capacity": current_storage_used_capacity,
        "alert_for_check_used_capacity": alert_for_check_used_capacity,
        "alert_reason_for_check_used_capacity": alert_reason_for_check_used_capacity,
        "alert_for_check_last_fetch": alert_for_check_last_fetch,
        "alert_reason_for_check_last_fetch": alert_reason_for_check_last_fetch,
    }
    if last_storage_fetch_time:
        obj["last_storage_fetch_time"] = last_storage_fetch_time
    return obj


def upload_to_table(my_table_name, my_entity):
    logging.info("---------------------------")
    table_client = TableClient.from_connection_string(
        connection_string, table_name=my_table_name
    )
    logging.warning(f"table_client - {table_client}")
    table_client.create_entity(entity=my_entity)
    logging.info("++++++++++++++++++++++++++++++++++++")
    return True

func_three_04()
