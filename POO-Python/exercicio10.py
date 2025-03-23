class Produto:
    '''classe para representar um produto'''
    def __init__(self, nome, preco, estoque):
        '''atributos do produto'''
        self.nome = nome 
        self.preco = float(preco) 
        self.estoque = int(estoque) 

    '''metodo para adicionar qntd de produtos em estoque'''
    def adicionar_estoque(self, qtd):
        self.estoque += qtd

    '''metodo para retirar um produto de estoque'''
    def retirar_estoque(self, qtd):
        '''verifica se tem a quantidade disponivel para retirar'''
        if self.estoque - qtd <= -1:
            print(f'Não temos essa quantidade. Qtd Atual: {self.estoque}')   
        else:
           self.estoque -= qtd
    '''exibe as informacoes do produto com o estoque atualizado'''
    def exibir_informacoes(self):
        print(f'Produto: {self.nome} Preco: {self.preco} Estoque: {self.estoque}')


produto = Produto('Mouse',34.90,23)
produto.exibir_informacoes()
produto.adicionar_estoque(10)
produto.exibir_informacoes()
produto.retirar_estoque(34)
produto.exibir_informacoes()
produto.adicionar_estoque(10)
produto.exibir_informacoes()

