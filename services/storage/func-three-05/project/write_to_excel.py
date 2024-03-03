from azure.storage.blob import BlobServiceClient
import pandas as pd
import os
import  logging
def write_and_upload(connection_string, data):
    logging.warn("1. write")
    blob_file = "alert_file.xlsx"
    container = "excel"
    write_excel_file(data, blob_file)
    logging.warn("2. write")
    upload_blob_file(connection_string, container, blob_file)
    logging.warn("3. write")


def write_excel_file(data, blob_file):
    df = pd.DataFrame(data)
    custom_header = [
        "Storage Account",
        "Alert Body",
        "Subscription Name",
        "Subscription Manager Email",
    ]
    df.to_excel(blob_file, index=False, header=custom_header)
    logging.info("---------------------------")


def upload_blob_file(connection_string, container, blob_file):
    logging.info(f"connection_string - {connection_string}")
    logging.info(f"container - {container}")
    logging.info(f"blob_file - {blob_file}")
    try:
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        container_client = blob_service_client.get_container_client(container=container)
        with open(os.path.join("./", blob_file), "rb") as data:
            container_client.upload_blob(name=blob_file, data=data, overwrite=True)
    except Exception as e:

        logging.warn(f"<><><><><><><><><>{e}")