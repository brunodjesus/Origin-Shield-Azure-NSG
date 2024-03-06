# Requer Azure Cli instalado e efetuado processo de Login az login.
# Requer Parametros do NSG que pode ser consultado no menu Properties na console Azure.
# Adiciona cada Rede Azion a uma regra Sequencial no NSG Azure.
# Le um arquivo txt com os Ips Azion obtidos pelo script anterior.



import os
import subprocess

# Parâmetros de conexão
subscription_id = "3dbe78a8-5803-452c-8a7c-7fd410d0e7d9"
resource_group_name = "LAB"
nsg_name = "NSG_AZION_ORIGIN_SHIELD"
rule_priority_start = 1000


# Arquivo de entrada com IPs
input_file = "/Users/bruno.jesus/Documents/Azion/Projetos/Edge Service/Origin Shield/ips-origin-shield.txt"

# Comando para criar regra no NSG
def create_nsg_rule(ip_address, rule_name, rule_priority):
    command = f"az network nsg rule create --resource-group {resource_group_name} --nsg-name {nsg_name} \
               --name {rule_name} --priority {rule_priority} --source-address-prefixes {ip_address} \
               --source-port-ranges '*' --destination-address-prefixes '*' --destination-port-ranges 80 443 \
               --access Allow --protocol Tcp --description 'Allow HTTP and HTTPS traffic from {ip_address}'"
    os.system(command)

# Função principal
def main():
    rule_counter = 1

    with open(input_file, "r") as file:
        for line in file:
            ip_address = line.strip()
            rule_name = f"RULE{rule_counter:02}"
            rule_priority = rule_priority_start + rule_counter
            create_nsg_rule(ip_address, rule_name, rule_priority)
            rule_counter += 1

if __name__ == "__main__":
    main()
