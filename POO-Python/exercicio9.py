class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome 
        self.salario = float(salario) 

class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus 

    def calcular_salario(self):
        self.total = self.salario + self.bonus 
        print(self.total)
    
    def exibir_dados(self):
        print(f'Nome: {self.nome}\nSalario: {self.salario}\nBonus:{self.bonus}\nTotal: {self.total}')

func = Funcionario("João", 2000)
print(func.nome, func.salario)  # João, 2000

gerente = Gerente("Maria", 3000, 1500)
print(gerente.calcular_salario())  # 4500
gerente.exibir_dados()  # Nome: Maria, Salário: 3000, Bônus: 1500, Total: 4500



        