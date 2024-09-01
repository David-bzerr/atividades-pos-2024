import zeep

# URL do WSDL da API SOAP
wsdl = 'http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL'

# Criar um cliente para a API SOAP usando o WSDL fornecido
client = zeep.Client(wsdl=wsdl)

# Chamar a função CapitalCity para obter a capital da Nova Zelândia (NZ)
capital_nz = client.service.CapitalCity('NZ')

# Exibir a capital da Nova Zelândia
print(f"A capital da Nova Zelândia é: {capital_nz}")
