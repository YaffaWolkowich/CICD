import pytest
import project
from unittest.mock import patch, Mock
from project.write_to_excel import download_blob
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class MockSheet:
    def __init__(self):
        self.max_row = 1

    def __getitem__(self, key):
        return None

    def __setitem__(self, key, value):
        pass


class MockWorkbook:
    def __init__(self):
        self.active = MockSheet()

    def save(self, file_stream):
        return "save"


@pytest.fixture
def mock_get_connection_string():
    with patch(
        "project.get_connection_string.get_connection_string_from_keyvault",
        return_value="connection_string",
    ):
        yield


@pytest.fixture
def mock_blob_service_client():
    with patch("project.write_to_excel.BlobServiceClient", Mock(return_value=None)):
        yield


@pytest.fixture
def mock_load_workbook():
    with patch(
        "project.write_to_excel.load_workbook", Mock(return_value=MockWorkbook())
    ):
        yield


@pytest.fixture
def mock_download_blob():
    with patch("project.write_to_excel.download_blob", Mock(return_value=b"att_file")):
        yield


def test_write_to_excel(
    mock_get_connection_string,
    mock_blob_service_client,
    mock_load_workbook,
    mock_download_blob,
):
    subscription_obj = {
        "display_name": "display_name",
        "subscription_id": "subscription_id",
        "body": "body",
    }
    result = project.write_to_excel.write_to_excel(subscription_obj)
    assert result is None


class MockContainer:
    def get_container_client(self, container_name):
        return MockBlob()


class MockBlob:
    def get_blob_client(self, blob_name):
        return MockBlobData()


class MockBlobData:
    def download_blob(self):
        return MockDownloadedBlob()


class MockDownloadedBlob:
    def readall(self):
        return "readall"


@patch("project.get_connection_string.get_connection_string_from_keyvault")
@patch(
    "project.write_to_excel.BlobServiceClient.from_connection_string",
    Mock(return_value=MockContainer()),
)
def test_download_blob(get_connection_string_from_keyvault):
    result = download_blob("container_name", "blob_name")
    get_connection_string_from_keyvault.assert_called()
    assert result == "readall"
