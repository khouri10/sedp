import json 
import requests
from keys import bling_apikey

#contrução genérica da url da API do bling, válida para qualquer tabela
URL_COMECO = 'https://bling.com.br/Api/v2/'
URL_FINAL = '/json/?apikey=' + bling_apikey

def criar_arquivo_json(tabela, params=None):
    """ busca as tabelas do Bling pela API e exporta para um arquivo
    bling_[nome da tabela].json . Aceita parametros para a url de acordo com
    biblioteca Requests, exemplo: {'estoque':'S'}"""
    pagina = 1
    todas_paginas = []

    while True:
        #consturção da url pra cada página da tabela usada
        url = URL_COMECO + tabela + '/page=' + str(pagina)+ URL_FINAL
        response = requests.get(url, params)
        data = response.json()
        if 'erros' in data['retorno']:
            print('done')
            break
        else:
            pagina_atual = data['retorno'][tabela]
            todas_paginas += pagina_atual
            print(pagina)
            pagina += 1

    with open('bling_' + tabela + '.json', 'w') as outfile:
        json.dump(todas_paginas, outfile)


    print(len(todas_paginas))

criar_arquivo_json('produtos')
#criar_arquivo_json('contatos')
#criar_arquivo_json('pedidos')
#criar_arquivo_json('contasreceber')


