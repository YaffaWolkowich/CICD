import datetime
import requests

from project.connect_to_azure import upload_to_table, retrieve_data_from_table
from config.config_variables import (
    connection_string as con_str,
    alerts_documentation,
    http_trigger_url,
)
import logging

def main_alerts(storage_name, email_body, partitionKey, row_key, subscription_name):
    try:
        logging.info("main alerts")
        manager_information = retrieve_data_from_table(
            True,
            con_str,
            "subscriptionManagersRealy",
            "subName eq @subscription_name",
            {"subscription_name": subscription_name},
            ["subName", "subManagerMail"],
        )[0]
        logging.warn(f"manager_information {manager_information}")
        requests.post(
            http_trigger_url,
            json={
                "recipient_email": manager_information["sub_manager_email"],
                "subject": "Storage Account Alert",
                "body": email_body,
                "excel": None,
            }
        )
        logging.warn("-------------------------------------------------")
    except Exception as e:
        logging.warn(f"warning: {e}")
        manager_information = {"subName": "null", "subManagerMail": "null"}

    alert_to_excel = add_entity_to_alerts_documentation(
        manager_information, storage_name, email_body, partitionKey, row_key
    )
    return alert_to_excel


def add_entity_to_alerts_documentation(
    manager_information, storage_account, email_body, partitionKey, row_key
):
    sender_date = str(datetime.date.today())
    entity = creating_object_for_alerts_documentation_table(
        partitionKey,
        row_key,
        sender_date,
        manager_information["subName"],
        manager_information["subManagerMail"],
        storage_account,
        email_body,
    )
    upload_to_table(alerts_documentation, entity)
    alert_to_excel = {
        "storage_account": storage_account,
        "alert_body": email_body,
        "subscription_name": entity["subName"],
        "subscription_manager_email": entity["subManagerMail"],
    }
    return alert_to_excel


def creating_object_for_alerts_documentation_table(
    partitionKey,
    row_key,
    sender_date,
    sub_name,
    sub_manager_email,
    storage_account,
    email_body,
):
    obj = {
        "PartitionKey": str(partitionKey),
        "RowKey": str(row_key),
        "sender_date": sender_date,
        "subName": sub_name,
        "subManagerMail": sub_manager_email,
        "storage_account": storage_account,
        "email_body": email_body,
    }
    return obj
