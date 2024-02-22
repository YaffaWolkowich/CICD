import azure.functions as func

# import os
# import sys
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# from config.config_variables import documentation_storage_name
from project.storage_account_test import *

app = func.FunctionApp()


@app.function_name(name="HttpTrigger1")
@app.route(route="")
def func_three_04(req: func.HttpRequest) -> func.HttpResponse:
    
    # body=req.get_body()
    # my_json = body.decode('utf8').replace("'", '"')
    # data = json.loads(my_json)
    
    # subscription_id=data['subscription_id']
    # storage_account=data['storage_account']
    # partition_key=data['partition_key']
    # row_key=data['row_key']

    answer=storage_account_test()

    #     return func.HttpResponse(json.dumps(paginated_response), mimetype="application/json")
    
    # paginated_response = {
    #     "value": [object_for_alerts_to_excel],
    #     "nextLink": None
    # }
    # return func.HttpResponse(json.dumps(paginated_response), mimetype="application/json")
    return func.HttpResponse(f"{answer}  ------for a personalized response.",status_code=200)
