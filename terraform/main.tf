resource "azurerm_resource_group" "resource_group" {
  name     = var.rg_name
  location = var.rg_location
}

resource "azurerm_storage_account" "storage_account" {
  name                     = var.storage_account_name
  resource_group_name      = azurerm_resource_group.resource_group.name
  location                 = azurerm_resource_group.resource_group.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

# data "azurerm_key_vault" "key_vault" {
#   name                = var.key_vault_name
#   resource_group_name = var.key_vault_resource_group_name
# }

# resource "azurerm_key_vault_secret" "key_vault_secret" {
#   name         = var.key_vault_secret_name
#   value        = azurerm_storage_account.storage_account.primary_connection_string
#   key_vault_id = data.azurerm_key_vault.key_vault.id
# }

resource "azurerm_service_plan" "service_plan" {
  name                = var.app_service_plan_name
  resource_group_name = azurerm_storage_account.storage_account.resource_group_name
  location            = azurerm_storage_account.storage_account.location
  os_type             = "Linux"
  sku_name            = "P1v2"
}

resource "azurerm_linux_function_app" "function_app" {
  name                = var.function_app_name
  resource_group_name = azurerm_storage_account.storage_account.resource_group_name
  location            = azurerm_storage_account.storage_account.location

  storage_account_name       = azurerm_storage_account.storage_account.name
  storage_account_access_key = azurerm_storage_account.storage_account.primary_access_key
  service_plan_id            = azurerm_service_plan.service_plan.id
  functions_extension_version = "~4"

  app_settings =  {
    FUNCTIONS_WORKER_RUNTIME = "python"

    # KEYVAULT_URI = data.azurerm_key_vault.key_vault.vault_uri
    # TENANT_ID = var.tenant_id
    # CLIENT_ID = var.client_id
    # CLIENT_SECRET = var.client_secret
    # APPLICATION_ID = var.application_id

    https_only                          = true
    DOCKER_REGISTRY_SERVER_URL          = var.DOCKER_REGISTRY_SERVER_URL
    DOCKER_REGISTRY_SERVER_USERNAME     = var.DOCKER_REGISTRY_SERVER_USERNAME
    DOCKER_REGISTRY_SERVER_PASSWORD     = var.DOCKER_REGISTRY_SERVER_PASSWORD
    WEBSITES_ENABLE_APP_SERVICE_STORAGE = false
  }

  site_config {
    always_on         = true
    application_stack {
      docker {
        registry_url = var.DOCKER_REGISTRY_SERVER_URL
        image_name = var.IMAGE_NAME
        image_tag = var.IMAGE_TAG
        registry_username = var.DOCKER_REGISTRY_SERVER_USERNAME
        registry_password = var.DOCKER_REGISTRY_SERVER_PASSWORD
      }
    }
  }

  identity {
    type = "SystemAssigned"
  }
}

# resource "azurerm_linux_function_app_slot" "linux_function_app_slot" {
#   name                       = "development"
#   function_app_id            = azurerm_linux_function_app.linux_function_app[count.index].id
#   storage_account_name       = azurerm_storage_account.storage_account.name
#   storage_account_access_key = azurerm_storage_account.storage_account.primary_access_key

#   site_config {
#     always_on = true
#     application_stack {
#       docker {
#         registry_url = var.DOCKER_REGISTRY_SERVER_URL
#         image_name = var.IMAGE_NAME
#         image_tag = var.IMAGE_TAG
#         registry_username = var.DOCKER_REGISTRY_SERVER_USERNAME
#         registry_password = var.DOCKER_REGISTRY_SERVER_PASSWORD
#       }
#     }
#   }

#   count = length(var.function_app_name)
# }

resource "azurerm_logic_app_workflow" "logic_app_workflow" {
  name                = var.logic_app_workflow_name
  location            = var.rg_location
  resource_group_name = var.rg_name

  workflow_parameters = {
    "workflows_logic_app_name" : "{ \"defaultValue\":\"${var.logic_app_workflow_name}\", \"type\" : \"string\"}"
    "location":"{\"defaultValue\": \"${var.rg_location}\",\"type\": \"string\" }"
    "sites_func-get-wow_externalid": "{\"defaultValue\": \"${azurerm_linux_function_app.linux_function_app.id}\",\"type\": \"string\"}"
  }
}

data "azurerm_client_config" "current_client" {}

# resource "azurerm_key_vault_access_policy" "principal" {
#   key_vault_id = data.azurerm_key_vault.key_vault.id
#   tenant_id    = data.azurerm_client_config.current_client.tenant_id
#   object_id    = azurerm_linux_function_app.linux_function_app[count.index].identity[0].principal_id

#   key_permissions = [
#     "Get", "List", "Encrypt", "Decrypt"
#   ]

#   secret_permissions = [
#     "Get",
#   ]

#   count = length(var.function_app_name)
# }

# resource "azurerm_storage_table" "storage_table" {
#   name                 = var.table_name
#   storage_account_name = azurerm_storage_account.storage_account.name

# }
