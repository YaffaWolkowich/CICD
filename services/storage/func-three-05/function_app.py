import azure.functions as func

# from project.process_management import inspection_process_management

app = func.FunctionApp()

@app.function_name(name="HttpTrigger1")
@app.route(route="")
def func_try_user_disable_automation(req: func.HttpRequest) -> func.HttpResponse:
#    inspection_process_management()
   return func.HttpResponse("wow!!!!!!!!!!!!!!", status_code=200)