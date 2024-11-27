import json  # Importa o módulo JSON para trabalhar com arquivos JSON
import os    # Importa o módulo OS para trabalhar com caminhos de arquivos e operações do sistema

# Define o caminho para o arquivo JSON, combinando o diretório atual do arquivo Python com o caminho relativo do JSON
caminho_json = os.path.join(os.path.dirname(__file__), '../json/imobiliaria.json')

# Abre o arquivo JSON e carrega seus dados na variável 'dados_imobiliaria'
with open(caminho_json, 'r') as arquivo:
    dados_imobiliaria = json.load(arquivo)  # 'json.load' lê o conteúdo do arquivo JSON e o converte em um dicionário Python

# Função para exibir os detalhes de um imóvel específico
def exibir_detalhes(imovel):
    print(f"\nDetalhes do Imóvel ID: {imovel['id']}")  # Exibe o ID do imóvel
    print(f"Descrição: {imovel['descricao']}")  # Exibe a descrição do imóvel
    print("Proprietário:")
    print(f"  Nome: {imovel['proprietario']['nome']}")  # Exibe o nome do proprietário
    print(f"  Email: {imovel['proprietario']['email']}")  # Exibe o email do proprietário
    # Exibe os telefones do proprietário, concatenando-os em uma string separada por vírgulas
    print(f"  Telefones: {', '.join(imovel['proprietario']['telefone'])}")
    print("Endereço:")
    # Exibe as informações de endereço, usando 'get' para fornecer valores padrão caso alguma informação não exista
    print(f"  Rua: {imovel['endereco'].get('rua', 'N/A')}")
    print(f"  Bairro: {imovel['endereco'].get('bairro', 'N/A')}")
    print(f"  Cidade: {imovel['endereco'].get('cidade', 'N/A')}")
    print(f"  Número: {imovel['endereco'].get('numero', 'N/A')}")
    print("Características:")
    # Exibe as características do imóvel, como tamanho, número de quartos e banheiros
    print(f"  Tamanho: {imovel['caracteristicas']['tamanho']} m²")
    print(f"  Número de Quartos: {imovel['caracteristicas']['numQuartos']}")
    print(f"  Número de Banheiros: {imovel['caracteristicas']['numBanheiros']}")
    # Exibe o valor do imóvel formatado como moeda (R$)
    print(f"Valor: R$ {imovel['valor']:,.2f}\n")

# Função principal para o menu interativo
def menu_interativo():
    while True:  # Loop infinito para manter o menu ativo até o usuário decidir sair
        print("Menu de Imóveis:")
        # Percorre a lista de imóveis e exibe o ID e a descrição de cada um no menu
        for imovel in dados_imobiliaria['imobiliaria']['imovel']:
            print(f"ID: {imovel['id']} - Descrição: {imovel['descricao']}")

        # Solicita ao usuário que insira o ID do imóvel ou 'sair' para encerrar
        escolha = input("Digite o ID do imóvel que deseja visualizar (ou 'sair' para encerrar): ")

        if escolha.lower() == 'sair':  # Verifica se o usuário quer sair
            print("Encerrando o programa.")
            break  # Sai do loop, encerrando o programa

        # Encontra o imóvel selecionado pelo ID usando uma expressão geradora
        imovel_selecionado = next((imovel for imovel in dados_imobiliaria['imobiliaria']['imovel'] if imovel['id'] == escolha), None)

        if imovel_selecionado:  # Se o imóvel foi encontrado, exibe seus detalhes
            exibir_detalhes(imovel_selecionado)
        else:
            # Caso o ID não seja encontrado, informa ao usuário e retorna ao menu
            print("ID não encontrado. Por favor, tente novamente.")

# Executa o menu interativo apenas se o script for executado diretamente
if __name__ == "__main__":
    menu_interativo()
