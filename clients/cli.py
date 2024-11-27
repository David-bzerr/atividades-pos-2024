import requests

# URL da API para obter os usuários
api_url = "https://jsonplaceholder.typicode.com/users"

# Fazendo a requisição GET para obter os usuários
response = requests.get(api_url)

# Convertendo a resposta para um objeto Python (lista de dicionários)
tudo = response.json()

def mostrar_nomes():
    for usuario in tudo:
        print(f"ID: {usuario['id']}, Nome: {usuario['name']}")

def listar_user(user_id):
    # URL da API para obter as tarefas de um usuário específico
    api_url_user = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    
    # Fazendo a requisição GET para obter as tarefas do usuário específico
    response_todos = requests.get(api_url_user)
    
    # Convertendo a resposta para um objeto Python (lista de dicionários)
    tarefas = response_todos.json()
    
    if tarefas:
        print(f"Tarefas do usuário com ID {user_id}:")
        for tarefa in tarefas:
            print(f"ID: {tarefa['id']}, Título: {tarefa['title']}, Concluída: {tarefa['completed']}")
    else:
        print(f"Nenhuma tarefa encontrada para o usuário com ID {user_id}.")

def criar_user():
    # Solicita os dados ao usuário
    name = input("Digite o nome: ")
    username = input("Digite o username: ")
    email = input("Digite o email: ")
    street = input("Digite o endereço: ")
    city = input("Digite a cidade: ")

    # Cria o dicionário com o endereço
    user_address = {
        "street": street,
        "city": city
    }

    # Cria o dicionário com os dados do usuário, incluindo o endereço
    user_data = {
        "name": name,
        "username": username,
        "email": email,
        "address": user_address
    }

    # Envia uma requisição POST para a API com o dicionário como JSON
    response = requests.post(api_url, json=user_data)
    
    # Exibe a resposta JSON e o código de status
    print(response.json())
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 201:
        print("Usuário criado com sucesso!")
    else:
        print("Falha ao criar usuário!")





def main():
    print("1-Listar todos os usuários")
    print("2-Listar as tarefas de um usuário específico")
    print("3-Modificar usuário")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        mostrar_nomes()

    elif escolha == "2":
        user_id = input("Digite o ID do usuário: ")
        listar_user(user_id)
    
    elif escolha == "3":
        print("1-criar usuario")
        print("2-ler usuario")
        print("3-atualizar usuario")
        print("4-deletar usuario")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            criar_user()

        elif escolha == "2":
            user_id = input("Digite o id do usuario: ")
            response = requests.get(f"{api_url}/{user_id}").json()
            print(response)

    else:
        print("Função inválida")

if __name__ == "__main__":
    main()
