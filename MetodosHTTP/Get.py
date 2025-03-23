'''Importa a biblioteca necessaria para fazer requisicoes'''
import requests
'''Faz a requisicao no link da API'''
requisicao = requests.get("https://metodoshttp-198c0-default-rtdb.europe-west1.firebasedatabase.app/.json")
'''Printa a resposta da API para a requisicao. 200 = Sucess, 404 = Failed'''
print(requisicao)
'''printa o dicionario JSON retornado pela API'''
print(requisicao.json())

