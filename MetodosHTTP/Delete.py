import requests

requisicao = requests.delete("https://metodoshttp-198c0-default-rtdb.europe-west1.firebasedatabase.app/-OH0A3_BlXO6VazdQvHP.json")

print(requisicao)

print(requisicao.json)