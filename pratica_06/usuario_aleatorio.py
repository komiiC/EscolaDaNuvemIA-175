"""
Crie um programa que gera um perfil de usuário aleatório usando a API 'Random User Generator'. O programa deve exibir o nome, email e país do usuário gerado.
"""
import requests
def gerar_usuario():
    url = "https://randomuser.me/api/"
    response = requests.get(url)
    try:
        data = response.json()
        usuario = data['results'][0]
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']
        return nome, email, pais
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API: {e}")

while True:
    entrada = input("Pressione Enter para gerar um usuário aleatório (ou 'sair' para encerrar): ")
    if entrada.lower() == 'sair':
        print("Programa encerrado.")
        break
    usuario_gerado = gerar_usuario()
    if usuario_gerado:
        nome, email, pais = usuario_gerado
        print(f"Nome: {nome}\nEmail: {email}\nPaís: {pais}")
    else:
        print("Não foi possível gerar o usuário. Tente novamente.")