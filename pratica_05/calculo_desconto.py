"""
Crie um programa que receba o preço original de um produto e um percentual de desconto, realizando o cálculo do preço final após a aplicação do desconto. Requisitos:
Permitir que o usuário informe o preço do produto e o percentual de desconto.
Utilizar operações matemáticas para calcular o valor do desconto e o preço final.
Exibir o preço final com duas casas decimais para garantir precisão. Entrada esperada: preço do produto (exemplo: 250.75) e o percentual de desconto (exemplo: 10).
"""
def calcular_preco_final(preco_original, percentual_desconto):
    desconto = preco_original * (percentual_desconto / 100)
    preco_final = preco_original - desconto
    return preco_final
input_preco = float(input("Informe o preço original do produto: R$ "))
input_desconto = float(input("Informe o percentual de desconto: "))
preco_final = calcular_preco_final(input_preco, input_desconto)
print(f"O preço final após o desconto é: R$ {preco_final:.2f}")