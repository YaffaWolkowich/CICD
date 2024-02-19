variable rg_name{
  type    = string
  default ="rg-try-admin"
}

variable rg_location {  
  type    = string
  default = "West Europe"
}

variable storage_account_name {
  type    = string
  default = "sttryadmin"
}

variable key_vault_name {
  type    = string
  default = "kv-try-admin"
}

variable key_vault_sku_name {
  type    = string
  default = "standard"
}

variable key_vault_certificate_permissions {
  type    = list
  default = ["Get", "List", "Update", "Create", "Import", "Delete", "Recover", "Backup", "Restore"]
}

variable key_vault_key_permissions {
  type    = list
  default = ["Create","Get"]
}

variable key_vault_secret_permissions {
  type    = list
  default = ["Get","Set","Delete","Purge","Recover"]
}

variable key_vault_storage_permissions {
  type    = list
  default = ["Get", ]
}

variable key_vault_secret_name {
  type    = string
  default = "ADMIN-SECRET"
}


