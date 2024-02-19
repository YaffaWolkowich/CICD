terraform {
  backend "azurerm" {
    resource_group_name  = "rg-try-again"
    storage_account_name = "sttryagain"
    container_name       = "terraform-state"
    key                  = "terraform.tfstate"
  }
}

provider "azurerm" {
  features {
    resource_group {
      prevent_deletion_if_contains_resources = false
    }
  }
  subscription_id = var.subscription_id
}

module administrator {
  source = "../administrator/"
}


module user-disable {
  source = "../user-disable/"
  key_vault_name = module.administrator.key_vault_name
  key_vault_resource_group_name = module.administrator.key_vault_resource_group_name
  tenant_id = var.TENANT_ID
  client_id = var.CLIENT_ID
  client_secret = var.CLIENT_SECRET
  application_id = var.APPLICATION_ID
  DOCKER_REGISTRY_SERVER_URL = var.DOCKER_REGISTRY_SERVER_URL
  DOCKER_REGISTRY_SERVER_USERNAME = var.DOCKER_REGISTRY_SERVER_USERNAME
  DOCKER_REGISTRY_SERVER_PASSWORD = var.DOCKER_REGISTRY_SERVER_PASSWORD

  depends_on = [
      module.administrator
  ]
}
