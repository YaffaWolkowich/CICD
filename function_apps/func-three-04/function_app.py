import azure.functions as func
import json
import logging
from config.config_variables import documentation_storage_name
from project.storage_account_test import storage_account_test

app = func.FunctionApp()


@app.function_name(name="HttpTrigger1")
@app.route(route="")
def func_test_storage(req: func.HttpRequest) -> func.HttpResponse:
    body = req.get_body()
    my_json = body.decode("utf8").replace("'", '"')
    data = json.loads(my_json)
    subscription_id = data["subscription_id"]
    subscription_name = data["subscription_name"]
    storage_account = data["storage_account"]
    partition_key = data["partition_key"]
    row_key = data["row_key"]
    last_fetch_time = data["last_fetch_time"]
    response_for_null_storages = {"storage_account": "null"}
    try:
        if storage_account["tag"] == "True":
            paginated_response = {
                "value": [response_for_null_storages],
                "nextLink": None,
            }
            return func.HttpResponse(
                json.dumps(paginated_response), mimetype="application/json"
            )
        if storage_account["name"] == documentation_storage_name:
            paginated_response = {
                "value": [response_for_null_storages],
                "nextLink": None,
            }
            return func.HttpResponse(
                json.dumps(paginated_response), mimetype="application/json"
            )
        logging.warn({'subscription_name':subscription_name,
                    'storage_account':storage_account,
                    'partition_key':partition_key,
                    'row_key':row_key,
                    'last_fetch_time':last_fetch_time
                    })
        object_for_alerts_to_excel = storage_account_test(
            storage_account["name"],
            partition_key,
            row_key,
            subscription_id,
            subscription_name,
            storage_account["id"],
            last_fetch_time,
        )
    except Exception:
        response_for_null_storages = {
            "storage_account": storage_account["name"],
            "alert_body": "null",
        }
        paginated_response = {"value": [response_for_null_storages], "nextLink": None}
        return func.HttpResponse(
            json.dumps(paginated_response), mimetype="application/json"
        )
    paginated_response = {"value": [object_for_alerts_to_excel], "nextLink": None}
    return func.HttpResponse(
        json.dumps(paginated_response), mimetype="application/json"
    )
