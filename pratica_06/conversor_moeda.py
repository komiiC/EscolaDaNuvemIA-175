"""
Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL). O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, máximo e mínimo da cotação, além da data e hora da última atualização. Utilize a API da AwesomeAPI para obter os dados de cotação.
"""
import requests
def consultar_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    response = requests.get(url)

    try:
        response.raise_for_status()
        dados = response.json()
        chave = f"{moeda}BRL"
        if chave not in dados:
            print("Moeda não encontrada.")
            return

        cotacao = dados[chave]
        valor_atual = cotacao['bid']
        valor_maximo = cotacao['high']
        valor_minimo = cotacao['low']
        data_hora = cotacao['create_date']

        print(f"Cotação de {moeda} em relação ao BRL:")
        print(f"Valor atual: R$ {valor_atual}")
        print(f"Valor máximo: R$ {valor_maximo}")
        print(f"Valor mínimo: R$ {valor_minimo}")
        print(f"Data e hora da última atualização: {data_hora}")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao consultar a cotação: {e}")

while True:
    moeda = input("Digite o código da moeda (ex: USD, EUR, GBP) ou 'sair' para encerrar: ").strip().upper()
    if moeda == 'SAIR':
        print("Programa encerrado.")
        break
    consultar_cotacao(moeda)