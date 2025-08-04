"""
Crie um programa que gera uma senha aleatória com o módulo random, utilizando caracteres especiais, possibilitando o usuário a informar a quantidade de caracteres dessa senha aleatória.
"""
import random
import string
def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

while True:
    entrada = input("Digite o tamanho da senha (ou 'sair' para encerrar): ")
    if entrada.lower() == 'sair':
        print("Programa encerrado.")
        break
    try:
        tamanho = int(entrada)
        if tamanho < 1:
            print("O tamanho deve ser um número positivo. Tente novamente.")
            continue
        senha_gerada = gerar_senha(tamanho)
        print(f"Senha gerada: {senha_gerada}")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")