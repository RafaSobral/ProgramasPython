class Veiculo:
    '''Classe para representar um veiculo'''
    def __init__(self, marca, modelo, ano):
        '''atributos do veiculo'''
        self.marca = marca
        self.modelo = modelo
        self.ano = ano 

    def exibir_detalhes(self):
        '''exibe os detalhes do carro'''
        print(f'Marca: {self.marca}\n Modelo: {self.modelo}\n Ano: {self.ano}')

class Carro(Veiculo):
    '''classe derivada da classe veiculo que herda os mesmos atributos da classe pai'''
    def __init__(self, marca, modelo, ano, qtdPortas):
        '''inicializando a classe pai para herdar os atributos'''
        super().__init__(marca, modelo, ano)
        '''adicionando o atributo quantidade de portas'''
        self.qtdPortas = qtdPortas

    '''exibir detalhes com o novo atributo'''
    def exibir_detalhes(self):
        '''inicializando a classe pai e printando os tres primeiros atributos'''
        super().exibir_detalhes()
        '''depois que os 3 atributos da classe pai foram printados, ele printa o novo atributo abaixo'''
        print(f'Quantidade de Portas: {self.qtdPortas}')


carro1 = Veiculo("Fiat", "Uno", 2010)
carro1.exibir_detalhes()
carro2 = Carro("Volkswagen", "Gol", 2022, 4)
carro2.exibir_detalhes()

    
        
    
        

        