# def mostrar_nome(nome):
#     print(f"Boa Noite!{nome}")

# nome = input("Digite o seu nome")
# mostrar_nome(nome)

# qtd_nome = int(input('Quantas pessoas deseja cadastrar?'))
# for i in range(qtd_nome):
#     nome = input(f'Digite o seu nome {i + 1}: ')
#     mostrar_nome(nome)

# def soma (a,b):
#     s = a+b 
#     print(f'A soma de {a} + {b} = {s}')

# a = int(input('Digite o primeiro numero:'))
# b = int(input('Digite o segundo numero:'))

# soma(a,b)

# soma(a=10,b=20)

# def sub(a,b):
#     return a - b

# print(f'A subtracao de {a} - {b} = {sub(a,b)}')




# def imc(peso, altura):
#     return (peso/altura ** 2)

# peso = float(input('Digite o seu peso:'))
# altura = float(input('Digite a sua altura:'))

# print(imc(peso,altura))

# def soma_e_media(valor1,valor2):
#     soma = valor1 + valor2 
#     media = (valor1 + valor2) / 2
#     return soma,media

# valor1 = int(input('Digite o valor1: '))
# valor2 = int(input('Digite o valor2: '))

# print(soma_e_media(valor1,valor2))

# def soma(*args):
#     total = 0 
#     for numeros in args:
#         total += numeros
#     return total

# valores = int(input('Digite os numeros'))

# valores = int(input("Digite os numeros separados por virgula ")).slipt()
# valores_int = ([int(valor) for valor in valores])

# resultado = soma(*valores_int)

# print(f'A soma dos valores é: {resultado}')
# print()

# def maior(*args):
#     print(args)
#     print(type(args))

#     for num in args:
#         if num > 30:
#             print(num)

# maior(10,20,30,40,50,60)

# r =  {'max':10, 'meio':5, 'min':0}
# def funcao(*args):
#     for chave in args:
#         print(chave)

# funcao(*r)

# def exemplo(**kwargs):
#     print(kwargs)

# exemplo(a=1,b=2,c=3)
# '''
# try:
#     operacao
# except:
#     error 
# else:
#     certo
# finally:
#     certo/errado'''

# '''try:
#     num = int(input('Digite um numero: '))
#     print(num)
# except:
#     print('Digite um numero válido')'''


# try: 
#     a = int(input('Digite um numero:'))
#     b = int(input('Digite outro numero:'))
#     r = a/b
# except:
#     print('Tivemos um problema no sistema')
# else:
#     print(f'A divisao de {a} / {b} = {r}')
