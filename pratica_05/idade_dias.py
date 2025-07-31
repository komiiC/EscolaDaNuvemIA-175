"""
Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.
"""
def calcular_idade_em_dias(ano_nascimento):
    from datetime import datetime
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade * 365

input_ano = int(input("Informe o ano de nascimento: "))
idade_dias = calcular_idade_em_dias(input_ano)
print(f"A idade em dias é: {idade_dias} dias")