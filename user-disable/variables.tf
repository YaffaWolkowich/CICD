variable DOCKER_REGISTRY_SERVER_PASSWORD {
  type = string
}

variable DOCKER_REGISTRY_SERVER_USERNAME {
  type = string
}

variable DOCKER_REGISTRY_SERVER_URL {
  type = string
}

variable key_vault_name {
  type = string
}

variable key_vault_resource_group_name {
  type = string
}

variable rg_name {
  type    = string
  default = "rg-user-disable-automation"
}

variable rg_location {  
  type      = string
  default   =   "West Europe"
}

variable storage_account_name {
  type    = string
  default = "stuserdisableautomation"
}




variable key_vault_secret_name {
  type        = string
  default     = "CONNECTION-STRING-USER-DISABLE"
}


variable app_service_plan_name{
  type = string
  default = "app-user-disable"
}

variable function_app_name {
  type  = string
  default = "func-user-disable"
}

variable "tenant_id" {
  type=string
}

variable "client_id" {
  type=string
}

variable "client_secret" {
  type=string
}

variable "application_id" {
  type = string
}


variable IMAGE_NAME {
  type        = string
  default     = "mcr.microsoft.com/azure-functions/dotnet"
}

variable IMAGE_TAG {
  type        = string
  default     = "4-appservice-quickstart"
}

