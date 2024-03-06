from unittest.mock import patch, Mock

from project.managed_subscription import (
    get_connection_string_from_keyvalut,
    convert_to_json,
    get_last_partitionKey,
    get_subscription_list,
    create_subscription_client,
)


class MockClient:
    def get_secret(self, secret_name):
        return MockSecret()


class MockSecret:
    def __init__(self):
        self.value = "value"


@patch(
    "project.managed_subscription.DefaultAzureCredential",
    Mock(return_value="DefaultAzureCredential"),
)
@patch("project.managed_subscription.keyvault_uri", "keyvault_uri")
@patch("project.managed_subscription.secret_name", "secret_name")
@patch("project.managed_subscription.SecretClient", Mock(return_value=MockClient()))
def test_get_connection_string_from_keyvalut():
    assert get_connection_string_from_keyvalut() == "value"


@patch(
    "project.managed_subscription.DefaultAzureCredential",
    Mock(return_value="azure cli credential"),
)
@patch("project.managed_subscription.SubscriptionClient")
def test_create_subscription_client(SubscriptionClient):
    create_subscription_client()
    SubscriptionClient.assert_called_once_with(credential="azure cli credential")


@patch("project.managed_subscription.create_subscription_client")
def test_get_subscription_list(create_subscription_client):
    get_subscription_list()
    create_subscription_client.assert_called_once_with()


@patch(
    "project.managed_subscription.get_connection_string_from_keyvalut",
    Mock(return_value="123456-789456"),
)
@patch(
    "project.managed_subscription.convert_to_json",
    Mock(
        return_value={
            "1": {"PartitionKey": "1"},
            "2": {"PartitionKey": "2"},
            "3": {"PartitionKey": "3"},
            "4": {"PartitionKey": "4"},
            "5": {"PartitionKey": "5"},
        }
    ),
)
@patch("project.managed_subscription.TableClient")
def test_get_last_partitionKey_called_connection_string(TableClient):
    get_last_partitionKey("table_name")
    TableClient.from_connection_string.assert_called_once_with(
        "123456-789456", "table_name"
    )


@patch(
    "project.managed_subscription.get_connection_string_from_keyvalut",
    Mock(return_value="123456-789456"),
)
@patch(
    "project.managed_subscription.convert_to_json",
    Mock(
        return_value={
            "1": {"PartitionKey": "1"},
            "2": {"PartitionKey": "2"},
            "3": {"PartitionKey": "3"},
            "4": {"PartitionKey": "4"},
            "5": {"PartitionKey": "5"},
        }
    ),
)
@patch("project.managed_subscription.TableClient")
def test_get_last_partitionKey_called_query_entities(TableClient):
    get_last_partitionKey("table_name")
    TableClient.from_connection_string().query_entities.assert_called_once_with(
        query_filter="", select=["*"]
    )


@patch(
    "project.managed_subscription.get_connection_string_from_keyvalut",
    Mock(return_value="123456-789456"),
)
@patch(
    "project.managed_subscription.convert_to_json",
    Mock(
        return_value={
            "1": {"PartitionKey": "1"},
            "2": {"PartitionKey": "2"},
            "3": {"PartitionKey": "3"},
            "4": {"PartitionKey": "4"},
            "5": {"PartitionKey": "5"},
        }
    ),
)
@patch("project.managed_subscription.TableClient")
def test_get_last_partitionKey_return_5(TableClient):
    assert get_last_partitionKey("table_name") == 5


@patch(
    "project.managed_subscription.get_connection_string_from_keyvalut",
    Mock(return_value="123456-789456"),
)
@patch(
    "project.managed_subscription.convert_to_json",
    Mock(return_value={}),
)
@patch("project.managed_subscription.TableClient")
def test_get_last_partitionKey_return_negative_one(TableClient):
    assert get_last_partitionKey("table_name") == -1


@patch("project.managed_subscription.pd")
@patch("project.managed_subscription.json.loads", Mock(return_value="json"))
def test_convert_to_json_convert_entities(pd):
    assert convert_to_json("entities") == "json"
