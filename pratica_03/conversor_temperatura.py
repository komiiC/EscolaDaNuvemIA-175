"""
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 

O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""
# Função para converter Celsius para Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
# Função para converter Celsius para Kelvin
def celsius_to_kelvin(celsius):
    return celsius + 273.15
# Função para converter Fahrenheit para Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
# Função para converter Fahrenheit para Kelvin
def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15
# Função para converter Kelvin para Celsius
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15
# Função para converter Kelvin para Fahrenheit
def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32
# Função principal para conversão de temperatura
def converter_temperatura(temperatura, unidade_origem, unidade_destino):
    if unidade_origem == 'C':
        if unidade_destino == 'F':
            return celsius_to_fahrenheit(temperatura)
        elif unidade_destino == 'K':
            return celsius_to_kelvin(temperatura)
    elif unidade_origem == 'F':
        if unidade_destino == 'C':
            return fahrenheit_to_celsius(temperatura)
        elif unidade_destino == 'K':
            return fahrenheit_to_kelvin(temperatura)
    elif unidade_origem == 'K':
        if unidade_destino == 'C':
            return kelvin_to_celsius(temperatura)
        elif unidade_destino == 'F':
            return kelvin_to_fahrenheit(temperatura)
    else:
        raise ValueError("Unidade de origem inválida.")
# Leitura dos dados de entrada
temperatura = float(input("Digite a temperatura: "))
unidade_origem = input("Digite a unidade de origem (C = Celsius, F = Fahrenheit, K = Kelvin: ").strip().upper()
unidade_destino = input("Digite a unidade de destino (C = Celsius, F = Fahrenheit, K = Kelvin: ").strip().upper()
# Realiza a conversão
resultado = converter_temperatura(temperatura, unidade_origem, unidade_destino)
# Exibe o resultado
print(f"{temperatura} {unidade_origem} é igual a {resultado:.2f} {unidade_destino}")
# Fim do programa