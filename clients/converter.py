import zeep

# URL do WSDL da API SOAP para conversão de números
wsdl = 'http://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL'

# Criar um cliente para a API SOAP usando o WSDL fornecido
client = zeep.Client(wsdl=wsdl)

# Solicitar ao usuário que digite um número
numero = int(input("Digite um número para converter para texto por extenso em inglês: "))

# Obter a versão por extenso do número em inglês
numero_extenso = client.service.NumberToWords(numero)

# Exibir o resultado
print(f"O número {numero} por extenso em inglês é: {numero_extenso}")
