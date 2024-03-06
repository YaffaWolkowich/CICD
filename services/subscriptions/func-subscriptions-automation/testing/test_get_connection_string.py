from unittest.mock import patch, Mock
from project.get_connection_string import get_connection_string_from_keyvault


class MockClient:
    def get_secret(self, secret_name):
        return MockKeyVaultNameValue()


class MockKeyVaultNameValue:
    def __init__(self):
        self.value = "value"


@patch(
    "project.get_connection_string.DefaultAzureCredential",
    Mock(return_value="Credentials"),
)
@patch("project.get_connection_string.SecretClient", Mock(return_value=MockClient()))
def test_get_connection_string_from_keyvault():
    result = get_connection_string_from_keyvault("secret_name")
    assert result == "value"


@patch(
    "project.get_connection_string.DefaultAzureCredential",
    Mock(side_effect=Exception("can not get connection string")),
)
@patch("project.get_connection_string.SecretClient", Mock(return_value=MockClient()))
def test_get_connection_string_from_keyvault_return_error():
    result = get_connection_string_from_keyvault("secret_name")
    assert result == "can not get connection string"
