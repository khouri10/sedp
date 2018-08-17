import json 
import requests
from keys import bling_apikey

#contrução genérica da url da API do bling, válida para qualquer tabela
URL_COMECO = 'https://bling.com.br/Api/v2/'
URL_FINAL = '/json/?apikey=' + bling_apikey

#tabelas que serão importadas
tabelas = ['contatos', 'produtos', 'pedidos']

pagina = 1
todas_paginas = []
url = URL_COMECO + tabelas[1] + '/page=' + str(pagina)+ URL_FINAL

print(url)
