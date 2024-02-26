from azure.storage.blob import BlobServiceClient
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# import project.get_connection_string
# import config.config_variables

def download_blob_excel(blob_name):
    # secret = config.config_variables.email_secret
    connection_string = "DefaultEndpointsProtocol=https;AccountName=myfirsttrail;AccountKey=bz3aax2d3IX7b3ngkc73W+CqpzKRvUj4So1zAuUxlrpGDuzPDeOGT7tdwD4UiLzSu9iBO6jT6c69+AStETr8tg==;EndpointSuffix=core.windows.net"
    container_name = 'excel'
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    blob_client = container_client.get_blob_client(blob_name)
    blob_data = blob_client.download_blob().readall()
    return blob_data


def delete_blob_excel(container_name, blob_name):
    # secret = config.config_variables.email_secret
    connection_string = "DefaultEndpointsProtocol=https;AccountName=myfirsttrail;AccountKey=bz3aax2d3IX7b3ngkc73W+CqpzKRvUj4So1zAuUxlrpGDuzPDeOGT7tdwD4UiLzSu9iBO6jT6c69+AStETr8tg==;EndpointSuffix=core.windows.net"
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    container_client.delete_blob(blob_name)
