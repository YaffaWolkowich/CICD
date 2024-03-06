from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.mgmt.subscription import SubscriptionClient
from azure.data.tables import TableClient
import json
import pandas as pd

from config.config_variables import keyvault_uri, secret_name


def get_connection_string_from_keyvalut():
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=keyvault_uri, credential=credential)
    secret = client.get_secret(secret_name)
    return secret.value


def create_subscription_client():
    subscription_client = SubscriptionClient(credential=DefaultAzureCredential())
    return subscription_client


def get_subscription_list():
    subscription_client = create_subscription_client()
    sub_list = subscription_client.subscriptions.list()
    return sub_list


def get_last_partitionKey(table_name):
    connection_string = get_connection_string_from_keyvalut()
    table_client = TableClient.from_connection_string(connection_string, table_name)
    partitionKeys_table = convert_to_json(
        table_client.query_entities(
            query_filter="",
            select=["*"],
        )
    )
    if partitionKeys_table == {}:
        return -1
    table = [
        int(partition["PartitionKey"]) for partition in partitionKeys_table.values()
    ]
    return max(table)


def convert_to_json(entities):
    return json.loads(pd.Series.to_json(pd.Series(entities)))
