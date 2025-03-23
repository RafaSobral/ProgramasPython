import time 
import pyotp
import qrcode

chave_mestre = "LCZVZ6GRTCIXBDMLMCUBHVWXY7MUGLFI"

codigo = pyotp.TOTP(chave_mestre)
print(codigo.now())

codigo_usuario = input("Codigo: ")
print(codigo.verify(codigo_usuario))

link = pyotp.TOTP(chave_mestre).provisioning_uri(name="Rafael", issuer_name="AutenticacaoPython")

meu_qrcode = qrcode.make(link)
meu_qrcode.save("qrcode.png")
