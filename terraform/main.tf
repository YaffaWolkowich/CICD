provider "azurerm" {
  subscription_id=var.subscription_id
  features {
    key_vault {
      purge_soft_delete_on_destroy    = true
      recover_soft_deleted_key_vaults = true
    }
  }
}

resource "azurerm_resource_group" "resource_group" {
  name     = var.resource_group_name
  location = var.resource_group_location
}

# resource "azurerm_automation_account" "automation_account" {
#   name                = var.automation_account_name
#   location            = azurerm_resource_group.resource_group.location
#   resource_group_name = azurerm_resource_group.resource_group.name
#   sku_name            = var.sku_name
#   tags = {
#     environment = "development"
#   }
# }

# resource "azurerm_automation_runbook" "automation_runbook" {
#   name                = var.automation_runbook_name
#   location            = azurerm_resource_group.resource_group.location
#   resource_group_name = azurerm_resource_group.resource_group.name
#   automation_account_name  = azurerm_automation_account.automation_account.name
#   log_verbose         = "true"
#   log_progress        = "true"
#   description         = var.automation_runbook_description
#   runbook_type        = var.automation_runbook_type

#   publish_content_link {
#     uri = var.automation_runbook_publish_content_link_uri
#   }
  
# }


# resource "azurerm_automation_schedule" "automation_schedule" {
#   name                    = var.automation_schedule_name
#   resource_group_name     = azurerm_resource_group.resource_group.name
#   automation_account_name = azurerm_automation_account.automation_account.name
#   frequency               = var.automation_schedule_frequency
#   interval                = var.automation_schedule_interval
#   timezone                = var.automation_schedule_timezone
#   start_time              = var.automation_schedule_start_time
# }

# resource "azurerm_automation_job_schedule" "automation_job_schedule" {
#   resource_group_name     = azurerm_resource_group.resource_group.name
#   automation_account_name = azurerm_automation_account.automation_account.name
#   schedule_name           = azurerm_automation_schedule.automation_schedule.name
#   runbook_name            = azurerm_automation_runbook.automation_runbook.name
#   }


# resource "azurerm_automation_variable_string" "automation_variable_string" {
#   count                   = length(local.automation_variables)
#   name                    = local.automation_variables[count.index].name
#   resource_group_name     = azurerm_resource_group.resource_group.name
#   automation_account_name = azurerm_automation_account.automation_account.name
#   value                   = local.automation_variables[count.index].value
# }

# resource "azurerm_automation_python3_package" "automation_python3_package" {
#   count                   = length(var.python3_packages)
#   name                    = var.python3_packages[count.index].name
#   resource_group_name     = azurerm_resource_group.resource_group.name
#   automation_account_name = azurerm_automation_account.automation_account.name
#   content_uri             = var.python3_packages[count.index].content_uri
  
# }

# data "azurerm_client_config" "current_client" {}

# resource "azurerm_key_vault" "key_vault" {
#   name                = var.key_vault_name
#   location            = azurerm_resource_group.resource_group.location
#   resource_group_name = azurerm_resource_group.resource_group.name
#   soft_delete_retention_days  = 7
#   tenant_id           = data.azurerm_client_config.current_client.tenant_id
#   sku_name            = var.key_vault_sku_name

#   access_policy {
#     tenant_id = data.azurerm_client_config.current_client.tenant_id
#     object_id = data.azurerm_client_config.current_client.object_id

#     certificate_permissions = var.key_vault_certificate_permissions

#     key_permissions = var.key_vault_key_permissions

#     secret_permissions = var.key_vault_secret_permissions

#     storage_permissions = var.key_vault_storage_permissions
#   }
# }

# resource "azurerm_key_vault_secret" "key_vault_secret" {
#   count        =length(var.key_vault_secret_items)
#   name         = var.key_vault_secret_items[count.index].name
#   value        = var.key_vault_secret_items[count.index].value
#   key_vault_id = azurerm_key_vault.key_vault.id
# }






