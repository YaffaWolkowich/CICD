from unittest.mock import patch, Mock
from project.excel_blob import get_last_row, create_excel_blob


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


class MockContainer:
    def get_container_client(self, container_name):
        return MockBlob()


class MockBlob:
    def get_blob_client(self, blob="blob_name", container="container_name"):
        return MockUploadBlob()


class MockUploadBlob:
    def upload_blob(self, stream, overwrite):
        return "upload_blob"

    def download_blob(self):
        return MockDownloadedBlob()


class MockDownloadedBlob:
    def readall(self):
        return b"readall"


@patch(
    "project.get_connection_string.get_connection_string_from_keyvault",
    return_value="connection_string",
)
@patch(
    "project.excel_blob.BlobServiceClient.from_connection_string",
    Mock(return_value=MockBlob()),
)
@patch("project.excel_blob.Workbook", Mock(return_value=MockWorkbook()))
def test_create_excel_blob(get_connection_string_from_keyvault):
    result = create_excel_blob()
    get_connection_string_from_keyvault.assert_called()
    assert result is None


@patch(
    "project.get_connection_string.get_connection_string_from_keyvault",
    Mock(return_value="connection_string"),
)
@patch(
    "project.excel_blob.BlobServiceClient.from_connection_string",
    Mock(return_value=MockBlob()),
)
@patch(
    "project.excel_blob.Workbook",
    Mock(side_effect=Exception("can not create excel blob")),
)
def test_create_excel_blob_return_exception_message():
    assert create_excel_blob() == "can not create excel blob"


@patch("project.get_connection_string.get_connection_string_from_keyvault")
@patch(
    "project.excel_blob.BlobServiceClient.from_connection_string",
    Mock(return_value=MockContainer()),
)
@patch("project.excel_blob.load_workbook", Mock(return_value=MockWorkbook()))
def test_get_last_row(get_connection_string_from_keyvault):
    result = get_last_row()
    get_connection_string_from_keyvault.assert_called()
    assert result == 1


@patch("project.get_connection_string.get_connection_string_from_keyvault")
@patch(
    "project.excel_blob.BlobServiceClient.from_connection_string",
    Mock(return_value=MockContainer()),
)
@patch(
    "project.excel_blob.load_workbook",
    Mock(side_effect=Exception("load_workbook failed")),
)
def test_get_last_row_return_exception_message(get_connection_string_from_keyvault):
    assert get_last_row() == "load_workbook failed"
