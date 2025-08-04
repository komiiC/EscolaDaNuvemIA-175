"""
Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário, utilizando a API ViaCEP. O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado.
"""
import requests
def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    
    try:
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        dados = response.json()
        
        if 'erro' in dados:
            print("CEP não encontrado.")
        else:
            logradouro = dados.get('logradouro', 'Não informado')
            bairro = dados.get('bairro', 'Não informado')
            cidade = dados.get('localidade', 'Não informado')
            estado = dados.get('uf', 'Não informado')
            
            print(f"Logradouro: {logradouro}")
            print(f"Bairro: {bairro}")
            print(f"Cidade: {cidade}")
            print(f"Estado: {estado}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao consultar o CEP: {e}")

cep = input("Digite o CEP (somente números): ").strip()
resultado = consultar_cep(cep)