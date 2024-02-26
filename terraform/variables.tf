variable DOCKER_REGISTRY_SERVER_PASSWORD {
  type = string
}

variable DOCKER_REGISTRY_SERVER_USERNAME {
  type = string
}

variable DOCKER_REGISTRY_SERVER_URL {
  type = string
}

variable subscription_id{
  type    = string
  default ="a173eef2-33d7-4d55-b0b5-18b271f8d42b"
}

variable rg_name{
  type    = string
  default ="rg-wow1"
}

variable rg_location {
  type    = string
  default = "West Europe"
}

variable storage_account_name {
  type    = string
  default = "stwow1"
}

variable app_service_plan_name{
  type    = string
  default = "app-func-wow1"
}

variable function_app_name {
  type    = string
  default = "func-wow11"
}

variable IMAGE_NAME {
  type    = string
  default = "mcr.microsoft.com/azure-functions/dotnet"
}

variable IMAGE_TAG {
  type    = string
  default = "4-appservice-quickstart"
}