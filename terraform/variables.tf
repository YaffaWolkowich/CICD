variable subscription_id {
  type        = string
  default     = "a173eef2-33d7-4d55-b0b5-18b271f8d42b"
}

variable resource_group_name {
  type        = string
  default     = "automationAccountTaskTry"
}

variable resource_group_location {
  type        = string
  default     = "West Europe"
}

variable automation_account_name {
  type        = string
  default     = "ExternalUserManagementAutomation"
}
variable sku_name {
  type        = string
  default     = "Basic"
}

variable automation_runbook_name {
  type        = string
  default     = "ExternalUserManagementRunbook"
}

variable automation_schedule_name {
  type        = string
  default     = "ExternalUserManagementSchedule"
}

variable automation_schedule_frequency {
  type        = string
  default     = "Week"
}

variable automation_schedule_interval {
  type        = number
  default     = 1
}

variable automation_schedule_timezone {
  type        = string
  default     = "Asia/Jerusalem"
}

variable automation_schedule_start_time {
  type        = string
  default     = "2023-12-28T13:15:00+02:00"
}

variable automation_runbook_type {
  type        = string
  default     = "Python3"
}

variable automation_runbook_description {
  type        = string
  default     = "runbook for automating the management of external users"
}

variable automation_runbook_publish_content_link_uri {
  type        = string
  default     = "https://aaa.com"
}

variable python3_packages {
  type        = list(map(string))
  default     = [
    {
    "name":"azure_identity",
    "content_uri":"https://files.pythonhosted.org/packages/30/10/5dbf755b368d10a28d55b06ac1f12512a13e88874a23db82defdea9a8cd9/azure_identity-1.15.0-py3-none-any.whl"
    },
    {
    "name":"azure_core",
    "content_uri":"https://files.pythonhosted.org/packages/b0/e2/b6cdd23d8d9cc430410cc309879883aff67736c02528cd1fdc07c48158b1/azure_core-1.29.6-py3-none-any.whl"
    },
    {
    "name":"cryptography318",
    "content_uri":"https://files.pythonhosted.org/packages/3a/b2/dc344d0cd962f040a956253843a130d44117f7e481114cd3453a85863474/cryptography318-1.0.0-py3-none-any.whl"
    },
    {
    "name":"msal",
    "content_uri":"https://files.pythonhosted.org/packages/b7/61/2756b963e84db6946e4b93a8e288595106286fc11c7129fcb869267ead67/msal-1.26.0-py2.py3-none-any.whl"
    },
    {
    "name":"six",
    "content_uri":"https://files.pythonhosted.org/packages/d9/5a/e7c31adbe875f2abbb91bd84cf2dc52d792b5a01506781dbcf25c91daf11/six-1.16.0-py2.py3-none-any.whl"
    },
    {
    "name":"typing-extensions",
    "content_uri":"https://files.pythonhosted.org/packages/b7/f4/6a90020cd2d93349b442bfcb657d0dc91eee65491600b2cb1d388bc98e6b/typing_extensions-4.9.0-py3-none-any.whl"
    },
    {
    "name":"anyio",
    "content_uri":"https://files.pythonhosted.org/packages/bf/cd/d6d9bb1dadf73e7af02d18225cbd2c93f8552e13130484f1c8dcfece292b/anyio-4.2.0-py3-none-any.whl"
    },
    {
    "name":"sniffio",
    "content_uri":"https://files.pythonhosted.org/packages/c3/a0/5dba8ed157b0136607c7f2151db695885606968d1fae123dc3391e0cfdbf/sniffio-1.3.0-py3-none-any.whl"
    },
    {
    "name":"exceptiongroup",
    "content_uri":"https://files.pythonhosted.org/packages/b8/9a/5028fd52db10e600f1c4674441b968cf2ea4959085bfb5b99fb1250e5f68/exceptiongroup-1.2.0-py3-none-any.whl"
    },
    {
    "name":"azure_keyvault_secrets",
    "content_uri":"https://files.pythonhosted.org/packages/d0/cf/92298854e657c29d31f9b028dec3ce9802467bff97c74d6c4145e9cfa96f/azure_keyvault_secrets-4.7.0-py3-none-any.whl"
    },
    {
    "name":"msrest",
    "content_uri":"https://files.pythonhosted.org/packages/15/cf/f2966a2638144491f8696c27320d5219f48a072715075d168b31d3237720/msrest-0.7.1-py3-none-any.whl"
    }
  ]
  description = "description"
}

variable key_vault_name {
  type        = string
  default = "user-management-vault"
}

variable key_vault_sku_name {
  type        = string
  default     = "standard"
}

variable key_vault_certificate_permissions {
  type        = list
  default = ["Get", "List", "Update", "Create", "Import", "Delete", "Recover", "Backup", "Restore"]
}

variable key_vault_key_permissions {
  type        = list
  default = ["Create","Get"]
}

variable key_vault_secret_permissions {
  type        = list
  default = ["Get","Set","Delete","Purge","Recover"]
}

variable key_vault_storage_permissions {
  type        = list
  default =  ["Get", ]
}

variable key_vault_secret_items {
  type        = list(map(string))
  default = [
    {
    name  = "CLIENT-SECRET"
    value  = ""
    },
    {
    name  = "CLIENT-ID"
    value  = ""
    },
    {
    name  = "TENENT-ID"
    value  = ""
    }
    ]
}





























