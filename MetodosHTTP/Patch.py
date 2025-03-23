import requests

informacoes = '{"Nome": "Sobral"}'

requisicao = requests.patch("https://metodoshttp-198c0-default-rtdb.europe-west1.firebasedatabase.app/-OH0A3_BlXO6VazdQvHP.json", data=informacoes )

print(requisicao)
print(requisicao.json())