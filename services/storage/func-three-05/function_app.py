import azure.functions as func
import logging
import requests
import json

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# from config.config_variables import (
#     documentation_table,
#     excel_connection_string,
#     main_manager,
#     http_trigger_url,
# )


from project.managed_deleted_storages import deleted_storages
from project.write_to_excel import write_and_upload


app = func.FunctionApp()


@app.function_name(name="HttpTrigger1")
@app.route(route="")
def func_send_excel_mark_delete(req: func.HttpRequest) -> func.HttpResponse:
    try:
        body = req.get_body()
        my_json = body.decode("utf8").replace("'", '"')
        data = json.loads(my_json)
        logging.info(f"data: {data}")
        alerts_to_excel = data["alerts_to_excel"]
        partition_key = data["partition_key"]
        all_storages = data["all_storages"]
        # write_and_upload(excel_connection_string, alerts_to_excel)
        # requests.post(
        #     http_trigger_url,
        #     json={
        #         "recipient_email": main_manager,
        #         "subject": "Summary Alerts For Storage Accounts",
        #         "body": "summary file",
        #         "excel": "alert_file.xlsx",
        #     },
        # )
        # deleted_storages(documentation_table, int(partition_key) - 1, all_storages)
    except Exception as e:
        logging.warn(f"-<<->>-{e}")

    return func.HttpResponse("success - end logic app", status_code=200)
