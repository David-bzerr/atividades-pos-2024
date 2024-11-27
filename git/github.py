import requests
from requests.auth import HTTPBasicAuth

user = input("user: ")
password = "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"
  



def seguir():
    user = input("User:")
    response = requests.put('https://api.github.com/user/following/{user}',
            auth = HTTPBasicAuth('David-bzerr', password))

    print(response.text)
    print(response)

def deseguir():
    user = input("User:")
    response = requests.delete('https://api.github.com/user/following/{user}',
            auth = HTTPBasicAuth('David-bzerr', password))
    
    print(response.text)
    print(response)


def main():
    
    print("1-digite o nome de quem deseja seguir")
    print("2-digite  nome de quem sedeja parar de seguir")
    escolha = input("")
    if escolha =="1":
        seguir()
    
    elif escolha =="1":
        deseguir()

    else:
        print("Invalido")

if __name__ == "__main__":
    main()
