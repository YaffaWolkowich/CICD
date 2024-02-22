FROM mcr.microsoft.com/azure-functions/python:4-python3.10
ENV AzureWebJobsScriptRoot=/home/site/wwwroot \
    AzureFunctionsJobHost__Logging__Console__IsEnabled=true \
    AzureWebJobsFeatureFlags=EnableWorkerIndexing \
    AzureWebJobsStorage=UseDevelopmentStorage=true
COPY requirements.txt /
RUN pip install -r /requirements.txt
# RUN python3 -m pip install openpyxl
# RUN pip3 install openpyxl
COPY . /home/site/wwwroo