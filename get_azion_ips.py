#Obtem a lista de IPs na Azion
#Formata o resultado listando apenas o IP`s.


import requests
import re
from datetime import datetime

# Função para verificar se uma string é um endereço IPv4 válido
def is_valid_ipv4(ip):
    pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
    return pattern.match(ip) is not None

def main():
    # Solicita o token de autorização do usuário
    token = input("Por favor, insira o token de autorização: ")

    # URL da API e cabeçalhos da solicitação
    url = 'https://api.azionapi.net/network_lists/187'
    headers = {
        'Accept': 'application/json; version=3',
        'Authorization': f'Token {token}'
    }

    # Faz a solicitação GET
    response = requests.get(url, headers=headers)

    # Verifica se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Nome do arquivo com a data atual
        filename = f'azion_shield_data_{datetime.now().strftime("%Y-%m-%d")}.txt'

        # Salva o resultado em um arquivo
        with open(filename, 'w') as file:
            file.write(response.text)
        
        print(f"Os dados foram salvos no arquivo '{filename}'.")

        # Nome do arquivo de saída para endereços IPv4
        output_file_name = "ips-origin-shield.txt"

        # Abrir o arquivo de entrada
        with open(filename, "r") as input_file:
            # Ler o conteúdo do arquivo linha por linha
            for line in input_file:
                # Procurar por endereços IPv4 no conteúdo da linha
                ipv4_addresses = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', line)
                # Escrever os endereços IPv4 encontrados em um novo arquivo
                with open(output_file_name, "a") as output_file:
                    for ip in ipv4_addresses:
                        if is_valid_ipv4(ip):
                            output_file.write(ip + "\n")
        print(f"Os endereços IPv4 foram salvos no arquivo '{output_file_name}'.")
    else:
        print(f"A solicitação falhou com o código de status {response.status_code}.")

if __name__ == "__main__":
    main()
