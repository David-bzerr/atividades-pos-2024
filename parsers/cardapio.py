from xml.dom.minidom import parse  # Importa a função 'parse' do módulo 'xml.dom.minidom' para analisar arquivos XML

# Faz o parse (análise) do arquivo XML 'cardapio.xml' e carrega o documento DOM na variável 'dom'
dom = parse("../xml/cardapio.xml")
# Obtém o elemento raiz do documento XML, que é o elemento 'cardapio'
cardapio = dom.documentElement
# Obtém uma lista de todos os elementos 'prato' dentro do elemento raiz 'cardapio'
pratos = cardapio.getElementsByTagName("prato")

# Função para exibir o menu de pratos
def mostrar_menu(pratos):
    print("Menu:")
    # Itera sobre a lista de pratos
    for prato in pratos:
        # Obtém o atributo 'id' de cada prato
        id_prato = prato.getAttribute('id')
        # Obtém o nome do prato a partir do elemento 'nome'
        nome_prato = prato.getElementsByTagName('nome')[0].firstChild.data
        # Exibe o ID e o nome do prato
        print(f"{id_prato} - {nome_prato}")

# Função para exibir os detalhes de um prato específico
def mostrar_detalhes(prato):
    # Obtém e exibe o nome do prato
    nome = prato.getElementsByTagName('nome')[0].firstChild.data
    # Obtém e exibe a descrição do prato
    descricao = prato.getElementsByTagName('descricao')[0].firstChild.data
    # Obtém e exibe o preço do prato
    preco = prato.getElementsByTagName('preco')[0].firstChild.data
    # Obtém e exibe as calorias do prato
    calorias = prato.getElementsByTagName('calorias')[0].firstChild.data

    # Exibe as informações detalhadas do prato
    print(f"Nome: {nome}")
    print(f"Descrição: {descricao}")
    print(f"Preço: {preco}")
    print(f"Calorias: {calorias}")

# Função principal para executar o menu interativo
def main():
    # Carrega e faz o parse do arquivo XML 'cardapio.xml'
    doc = parse("C:/Users/Rafin/Documents/atividades-pos-2024/xml/cardapio.xml")
    
    # Obtém todos os elementos 'prato' do documento XML
    pratos = doc.getElementsByTagName("prato")
    
    # Exibe o menu de pratos
    mostrar_menu(pratos)
    
    # Solicita ao usuário que escolha um prato pelo ID
    escolha = input("\nDigite o ID do prato para ver mais detalhes: ")

    # Inicializa a variável 'prato_escolhido' como None
    prato_escolhido = None
    # Procura pelo prato com o ID escolhido
    for prato in pratos:
        if prato.getAttribute('id') == escolha:
            prato_escolhido = prato  # Se encontrar o prato, armazena-o em 'prato_escolhido'
            break  # Interrompe o loop ao encontrar o prato

    if prato_escolhido:
        # Se o prato foi encontrado, exibe os detalhes do prato
        print("\nDetalhes do Prato:")
        mostrar_detalhes(prato_escolhido)
    else:
        # Caso contrário, informa que o prato não foi encontrado
        print("Prato não encontrado. Por favor, tente novamente.")

# Verifica se o script está sendo executado diretamente (e não importado como módulo)
if __name__ == "__main__":
    main()  # Chama a função principal para executar o programa
