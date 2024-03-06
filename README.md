<img width="1679" alt="image" src="https://github.com/brunodjesus/Origin-Shield-Azure-NSG/assets/113184197/f25a16a2-6d57-4db0-92cb-3bedbffec808">



Pre-reqs:

Instalacao do Azure Cli:
  - https://learn.microsoft.com/en-us/cli/azure/install-azure-cli

Python Versao 3
- pip install requests



1 - Executar o Script:
python3 get_azion_ips.py 

:: Por favor, insira o token de autorização: azion8c286fb521a942ee06c780473dd29fc1cf9
:: Os dados foram salvos no arquivo 'azion_shield_data_2024-03-06.txt'
:: Os endereços IPv4 foram salvos no arquivo 'ips-origin-shield.txt'              --> Arquivo Formatado apenas com os IPs - (padrao ipv4) separados por linha.


2 - Parametriz o Script: create_nsg_rules.py


subscription_id = 
resource_group_name = 
nsg_name = 
rule_priority_start 

# Arquivo de entrada com IPs
input_file = 

Execute o Script e acompanhe os Logs:

 ],
  "direction": "Inbound",
  "etag": "W/\"d22ca33f-65f8-4531-9be8-7af480504333\"",
  "id": "/subscriptions/3dbe78a8-5803-452c-8a7c-7fd410d0e7d9/resourceGroups/LAB/providers/Microsoft.Network/networkSecurityGroups/NSG_AZION_ORIGIN_SHIELD/securityRules/RULE96",
  "name": "RULE96",
  "priority": 1096,
  "protocol": "Tcp",
  "provisioningState": "Succeeded",
  "resourceGroup": "LAB",
  "sourceAddressPrefix": "195.181.174.150",
  "sourceAddressPrefixes": [],
  "sourcePortRange": "*",
  "sourcePortRanges": [],
  "type": "Microsoft.Network/networkSecurityGroups/securityRules"
}
{
  "access": "Allow",
  "description": "Allow HTTP and HTTPS traffic from 187.122.251.128",
  "destinationAddressPrefix": "*",
  "destinationAddressPrefixes": [],
  "destinationPortRanges": [
    "80",
    "443"
  ],
  "direction": "Inbound",
  "etag": "W/\"963e9aab-0333-4ca6-9b3f-2cc34c4a89d8\"",
  "id": "/subscriptions/3dbe78a8-5803-452c-8a7c-7fd410d0e7d9/resourceGroups/LAB/providers/Microsoft.Network/networkSecurityGroups/NSG_AZION_ORIGIN_SHIELD/securityRules/RULE97",
  "name": "RULE97",
  "priority": 1097,
  "protocol": "Tcp",
  "provisioningState": "Succeeded",
  "resourceGroup": "LAB",
  "sourceAddressPrefix": "187.122.251.128",
  "sourceAddressPrefixes": [],
  "sourcePortRange": "*",
  "sourcePortRanges": [],
  "type": "Microsoft.Network/networkSecurityGroups/securityRules"

                            
