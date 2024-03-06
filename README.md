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

input_file = (informe aqui o caminho do arquivo resultado do Script get_azion_ips.py - ips-origin-shield.txt

Execute o Script e acompanhe os Logs:

  / Running ..
