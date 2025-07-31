"""
Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.
"""
def eh_palindromo(texto):
    # Remove espaços e pontuação, e converte para minúsculas
    texto_limpo = ''.join(char.lower() for char in texto if char.isalnum())
    
    # Verifica se o texto é igual ao seu reverso
    return texto_limpo == texto_limpo[::-1]
def verificar_palindromo(texto):
    if eh_palindromo(texto):
        return "Sim"
    else:
        return "Não"
interface = input("Digite uma palavra ou frase: ")
resultado = verificar_palindromo(interface)
print(resultado)