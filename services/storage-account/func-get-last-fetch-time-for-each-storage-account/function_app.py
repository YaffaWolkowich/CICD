import azure.functions as func

from project.read_log_analytics import get_last_fetch_time_array


app = func.FunctionApp()


@app.function_name(name="HttpTrigger1")
@app.route(route="")
def func_get_last_fetch_time_for_each_storage_account(
    req: func.HttpRequest,
) -> func.HttpResponse:
    max_time_foreach_storage = get_last_fetch_time_array()

    return func.HttpResponse(str(max_time_foreach_storage), status_code=200)
