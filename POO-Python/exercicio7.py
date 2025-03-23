class ContaBancaria:
    '''Classe para representar uma conta bancaria'''
    def __init__(self, numero, titular, saldo):
        """atributos da conta bancaria"""
        self.numero = int(numero) 
        self.titular = titular
        self.saldo = float(saldo)

    def depositar(self, valor):
        '''deposita um valorna conta'''
        self.saldo += valor

    def sacar(self, valor):
        '''retira um valor da conta'''
        self.saldo -= valor

    def exibir_saldo(self):
        '''exibe o saldo da conta'''
        return self.saldo
    
    def __str__(self):
        '''retorna uma representacao em string da conta bancaria'''
        return f' Titular: {self.titular}\n Conta N:{self.numero}\n Saldo: {self.saldo}'
    
conta1 = ContaBancaria(12093,'Rafael', 182.50)
print(conta1)
conta1.depositar(10)
saldo = conta1.exibir_saldo()
print(saldo)
conta1.sacar(10)
saldo = conta1.exibir_saldo()
print(saldo)
    


        
