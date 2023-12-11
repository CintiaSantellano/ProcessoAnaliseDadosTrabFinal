class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f'Ponto: ({self.x}, {self.y})')


class Retangulo:
    def __init__(self, largura, altura, ponto_inicial):
        self.largura = largura
        self.altura = altura
        self.ponto_inicial = ponto_inicial

    def encontrar_centro(self):
        x_centro = self.ponto_inicial.x + self.largura / 2
        y_centro = self.ponto_inicial.y + self.altura / 2
        centro = Ponto(x_centro, y_centro)
        return centro


# Criar objetos da classe Retangulo
retangulo1 = Retangulo(10, 5, Ponto(0, 0))
retangulo2 = Retangulo(7, 3, Ponto(2, 2))

# Encontrar o centro dos retângulos
centro1 = retangulo1.encontrar_centro()
centro2 = retangulo2.encontrar_centro()

# Imprimir os valores dos pontos de partida e os centros dos retângulos
retangulo1.ponto_inicial.imprimir()
centro1.imprimir()

retangulo2.ponto_inicial.imprimir()
centro2.imprimir()
