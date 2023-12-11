class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def mudar_lados(self, novo_lado_a, novo_lado_b):
        self.lado_a = novo_lado_a
        self.lado_b = novo_lado_b

    def retornar_lados(self):
        return self.lado_a, self.lado_b

    def calcular_area(self):
        return self.lado_a * self.lado_b

    def calcular_perimetro(self):
        return 2 * (self.lado_a + self.lado_b)


# Programa principal
lado_a = float(input("Informe o valor do lado A do retângulo: "))
lado_b = float(input("Informe o valor do lado B do retângulo: "))

retangulo = Retangulo(lado_a, lado_b)

area = retangulo.calcular_area()
perimetro = retangulo.calcular_perimetro()

quantidade_pisos = area / 1  # Área de 1m² por piso
quantidade_rodapes = perimetro / 1  # Perímetro de 1m por rodapé

print("Quantidade de pisos necessários:", quantidade_pisos)
print("Quantidade de rodapés necessários:", quantidade_rodapes)
