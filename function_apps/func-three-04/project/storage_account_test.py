from datetime import datetime

from config.config_variables import documentation_table
from project.alert_reason_enum import alert_reasons
from project.connect_to_azure import (
    upload_to_table,
    # find_resource_group_name,
    # create_storage_management_client,
)
# from project.last_fetch_time import check_last_fetch_is_early
# from project.send_alert_email import main_alerts
# from project.used_capacity_comparison import used_capacity_comparison_test


def storage_account_test():
    entity = create_object_for_documentation_table(
        "storage_account",
        "partition_key",
        "row_key",
        "subscription_id"
        "12.5",
        "12-21-03",
        'null',
        'alert reason',
        "null",
        "aaa",
        "bbb",
        "ccc",
    )
    a=upload_to_table(documentation_table, entity)
    # try:
    #     object_for_alerts_to_excel = check_alert(
    #         used_capacity_comparison_test_result["alert"],
    #         last_fetch_is_early_result["alert"],
    #         storage_account,
    #         partitionKey,
    #         row_key,
    #         subscription_name,
    #     )
    # except Exception as e:
    #     raise e
    # return object_for_alerts_to_excel
    return a


# def check_alert(
#     used_capacity_comparison_test_result,
#     last_fetch_is_early_result,
#     storage_name,
#     partitionKey,
#     row_key,
#     subscription_name,
# ):
#     alert = used_capacity_comparison_test_result or last_fetch_is_early_result
#     if alert:
#         alert_reason = (
#             alert_reasons.USED_CAPACITY.value
#             if used_capacity_comparison_test_result
#             else ""
#         )
#         alert_reason += (
#             " and " if last_fetch_is_early_result and alert_reason != "" else ""
#         )
#         alert_reason += (
#             alert_reasons.LAST_FETCH_TIME.value if last_fetch_is_early_result else ""
#         )
#         if alert_reason != "":
#             alert_reason = ":storage account " + storage_name + "\n" + alert_reason
#             try:
#                 object_for_alerts_to_excel = main_alerts(
#                     storage_name, alert_reason, partitionKey, row_key, subscription_name
#                 )
#                 return object_for_alerts_to_excel
#             except Exception as e:
#                 raise e
#     return {"storage_account": storage_name, "alert_body": "null"}


def create_object_for_documentation_table(
    partitionKey,
    row_key,
    test_date,
    subscription_id,
    resource_group,
    storage_name,
    current_storage_used_capacity,
    last_storage_fetch_time,
    alert_for_check_used_capacity,
    alert_reason_for_check_used_capacity,
    alert_for_check_last_fetch,
    alert_reason_for_check_last_fetch,
):
    obj = {
        "PartitionKey": partitionKey,
        "RowKey": row_key,
        "test_date": test_date,
        "subscription_id": subscription_id,
        "resource_group": resource_group,
        "storage_name": storage_name,
        "used_storage_capacity": current_storage_used_capacity,
        "alert_for_check_used_capacity": alert_for_check_used_capacity,
        "alert_reason_for_check_used_capacity": alert_reason_for_check_used_capacity,
        "alert_for_check_last_fetch": alert_for_check_last_fetch,
        "alert_reason_for_check_last_fetch": alert_reason_for_check_last_fetch,
    }
    # if last_storage_fetch_time:
    #     obj["last_storage_fetch_time"] = last_storage_fetch_time
    return obj
