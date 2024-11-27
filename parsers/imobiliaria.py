# Importa a biblioteca minidom para trabalhar com XML
from xml.dom.minidom import parse

# Carrega e faz o parse do arquivo XML, criando um objeto DOM
dom = parse("../xml/imobiliaria2.xml")

# Obtém o elemento raiz do XML (neste caso, o elemento <imobiliaria>)
imobiliaria = dom.documentElement

# Obtém uma lista de todos os elementos <imovel> no XML
imoveis = imobiliaria.getElementsByTagName("imovel")

# Função para exibir o menu com os IDs dos imóveis
def mostrar_menu(imoveis):
    print("Menu:")  # Exibe o título do menu
    # Percorre a lista de imóveis e exibe o ID de cada um
    for imovel in imoveis:
        # Obtém o atributo 'id' do elemento <imovel>
        id_imovel = imovel.getAttribute('id')
        print(f"ID: {id_imovel}")  # Exibe o ID do imóvel

# Função para exibir os detalhes de um imóvel específico
def mostrar_detalhes(imovel):
    # Obtém o conteúdo do elemento <descricao>
    descricao = imovel.getElementsByTagName('descricao')[0].firstChild.data

    # Extrai as informações do proprietário do imóvel
    proprietario_element = imovel.getElementsByTagName('proprietario')[0]
    nome_proprietario = proprietario_element.getElementsByTagName('nome')[0].firstChild.data
    email_proprietario = proprietario_element.getElementsByTagName('email')[0].firstChild.data
    telefone_proprietario = proprietario_element.getElementsByTagName('telefone')[0].firstChild.data

    # Extrai as informações do endereço do imóvel
    endereco_element = imovel.getElementsByTagName('endereco')[0]
    rua = endereco_element.getElementsByTagName('rua')[0].firstChild.data
    bairro = endereco_element.getElementsByTagName('bairro')[0].firstChild.data
    cidade = endereco_element.getElementsByTagName('cidade')[0].firstChild.data
    numero = endereco_element.getElementsByTagName('numero')[0].firstChild.data

    # Extrai as informações das características do imóvel
    caracteristicas_element = imovel.getElementsByTagName('caracteristicas')[0]
    tamanho = caracteristicas_element.getElementsByTagName('tamanho')[0].firstChild.data
    num_quartos = caracteristicas_element.getElementsByTagName('numQuartos')[0].firstChild.data
    num_banheiros = caracteristicas_element.getElementsByTagName('numBanheiros')[0].firstChild.data

    # Exibe todas as informações do imóvel de forma organizada
    print(f"Descrição: {descricao}")
    print(f"Proprietário: {nome_proprietario}")
    print(f"Email: {email_proprietario}")
    print(f"Telefone: {telefone_proprietario}")
    print(f"Endereço: Rua {rua}, {numero}, Bairro {bairro}, {cidade}")
    print(f"Características: Tamanho - {tamanho} m², Quartos - {num_quartos}, Banheiros - {num_banheiros}")

# Função principal que controla o fluxo do programa
def main():
    # Obtém todos os imóveis novamente para garantir que a lista esteja atualizada
    imoveis = dom.getElementsByTagName("imovel")
    
    # Exibe o menu de imóveis com os IDs disponíveis
    mostrar_menu(imoveis)
    
    # Solicita ao usuário que escolha um imóvel pelo ID
    escolha = input("\nDigite o ID do imóvel para ver mais detalhes: ")

    # Inicializa uma variável para armazenar o imóvel escolhido
    imovel_escolhido = None
    
    # Procura o imóvel na lista de imóveis pelo ID fornecido pelo usuário
    for imovel in imoveis:
        if imovel.getAttribute('id') == escolha:
            imovel_escolhido = imovel
            break  # Sai do loop ao encontrar o imóvel

    # Se o imóvel foi encontrado, exibe os detalhes
    if imovel_escolhido:
        print("\nDetalhes do Imóvel:")
        mostrar_detalhes(imovel_escolhido)
    else:
        # Se o ID não for encontrado, exibe uma mensagem de erro
        print("Imóvel não encontrado. Por favor, tente novamente.")

# Se o arquivo for executado diretamente, chama a função principal
if __name__ == "__main__":
    main()
