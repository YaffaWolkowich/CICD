import azure.functions as func
import json

# import os
# import sys
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config.config_variables import documentation_storage_name
from project.storage_account_test import *

app = func.FunctionApp()


@app.function_name(name="HttpTrigger1")
@app.route(route="")
def func_three_04(req: func.HttpRequest) -> func.HttpResponse:
    
    body=req.get_body()
    my_json = body.decode('utf8').replace("'", '"')
    data = json.loads(my_json)
    
    subscription_id=data['subscription_id']
    subscription_name=data['subscription_name']
    storage_account=data['storage_account']
    partition_key=data['partition_key']
    row_key=data['row_key']
    last_fetch_time=data['last_fetch_time']

    response_for_null_storages={"storage_account":"null"}
#     {
#   "last_fetch_time": "2024-02-22 06:49:17.274355+00:00",
#   "partition_key": "0",
#   "row_key": 1,
#   "storage_account": {
#     "id": "/subscriptions/a173eef2-33d7-4d55-b0b5-18b271f8d42b/resourceGroups/checkWorkfolwStorage/providers/Microsoft.Storage/storageAccounts/checkworkfolwstoraga55d",
#     "name": "checkworkfolwstoraga55d",
#     "tag": "false"
#   },
#   "subscription_id": "a173eef2-33d7-4d55-b0b5-18b271f8d42b",
#   "subscription_name": "Moon- azure camp"
# }
    # try:
    #     if storage_account['tag'] == "True" :
    #         paginated_response = {
    #         "value": [response_for_null_storages],
    #         "nextLink": None
    #         }
    #         return func.HttpResponse(json.dumps(paginated_response), mimetype="application/json")
        
    #     if(storage_account['name']==documentation_storage_name):
    #         paginated_response = {
    #         "value": [response_for_null_storages],
    #         "nextLink": None
    #         }
    #         return func.HttpResponse(json.dumps(paginated_response), mimetype="application/json")

        
    object_for_alerts_to_excel=storage_account_test(
        storage_account['name'],
        partition_key,
        row_key,
        subscription_id
    )
    # except Exception as e:
    response_for_null_storages={"storage_account":storage_account['name'],"alert_body":"null"}
    paginated_response = {
        "value": [response_for_null_storages],
        "nextLink": None
    }
    #     return func.HttpResponse(json.dumps(paginated_response), mimetype="application/json")
    
    # paginated_response = {
    #     "value": [object_for_alerts_to_excel],
    #     "nextLink": None
    # }
    return func.HttpResponse(json.dumps(paginated_response), mimetype="application/json")