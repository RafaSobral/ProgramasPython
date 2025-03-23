import requests

informacoes = '{"Nome": "Lima"}'

requisicao = requests.post("https://metodoshttp-198c0-default-rtdb.europe-west1.firebasedatabase.app/.json", data=informacoes)

print(requisicao)

print(requisicao.json())