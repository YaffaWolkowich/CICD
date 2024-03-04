import azure.functions as func
import logging

app = func.FunctionApp()


@app.function_name(name="HttpTrigger1")
@app.route(route="")
def func_test_storage(req: func.HttpRequest) -> func.HttpResponse:
   logging.info("hello")

   return func.HttpResponse("success - end logic app", status_code=200)
