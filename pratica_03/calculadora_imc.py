"""
Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.


< 18.5: classificacao = "Abaixo do peso" 

< 25: classificacao = "Peso normal"

 < 30: classificacao = "Sobrepeso"

 Para os demais cenários: classificacao = "Obeso"
 """
# Início do código
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        classificacao = "Você está abaixo do peso"
    elif imc < 25:
        classificacao = "Você está no peso normal"
    elif imc < 30:
        classificacao = "Você está com sobrepeso"
    else:
        classificacao = "Você está obeso"
    return imc, classificacao
print("Cálculo do IMC")
if __name__ == "__main__":
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))
    imc, classificacao = calcular_imc(peso, altura)
    print(f"IMC: {imc:.2f}")
    print(f"Classificação: {classificacao}")
# Fim do código