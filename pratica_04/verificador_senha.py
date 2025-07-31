"""
Crie um programa que verifique se uma senha é forte. Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número. O programa deve continuar pedindo senhas até que uma válida seja inserida ou o usuário digite 'sair'.
"""
def verificar_senha(senha):
    if len(senha) < 8:
        return False
    if not any(char.isdigit() for char in senha):
        return False
    return True

while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")
    if senha.lower() == 'sair':
        print("Programa encerrado.")
        break
    if verificar_senha(senha):
        print("Senha forte!")
        break
    else:
        print("Senha fraca. Tente novamente.")