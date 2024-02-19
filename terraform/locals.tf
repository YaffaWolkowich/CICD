locals {
  automation_variables = [
    {
      name  = "department_var"
      value = "moon"
    },
    {
      name  = "x_days_var"
      value = "3"
    },
    {
      name  = "kv_uri_var"
      value = "https://${var.key_vault_name}.vault.azure.net"
    }
  ]
}