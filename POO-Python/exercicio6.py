class Retangulo:
    '''classe para representar eum triangulo'''
    def __init__(self, largura, altura):
        '''atributos do traingulo'''
        self.largura = int(largura)
        self.altura = int(altura)

    def calcular_area(self):
        '''calcula a area do retangulo'''
        area = self.altura * self.largura
        return area 
    def calcular_perimetro(self):
        '''calcula o perimetro do retangulo'''
        perimetro = self.altura + self.altura + self.largura + self.largura 
        return perimetro
    
obj = Retangulo(5,3)
calculo1 = obj.calcular_area()
calculo2 = obj.calcular_perimetro()
print(f'Area: {calculo1} Perimetro: {calculo2}')



