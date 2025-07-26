"""
A fórmula para calcular a área de uma circunferência é: área = π ×raio2. Considerando para
este problema que π = 3.14159265: 

• Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π. 

Entrada: A entrada contém um valor de ponto flutuante (dupla precisão), no caso, a variável
raio.
Saída: Apresente a mensagem "A=" seguido pelo valor da variável area, conforme exemplo
abaixo, com 4 casas após o ponto decimal. Utilize variáveis de dupla precisão (double). Como
em todos os problemas, não esqueça de imprimir o fim de linha após o resultado, caso contrário,
você receberá "Presentation Error".
"""
import math
# Início do código
def calcular_area_circunferencia(raio):
    pi = 3.14159265
    area = pi * (raio ** 2)
    return area

if __name__ == "__main__":
    raio = float(input("Insira o valor do raio: "))
    area = calcular_area_circunferencia(raio)
    print(f"A={area:.4f}")
# Fim do código

