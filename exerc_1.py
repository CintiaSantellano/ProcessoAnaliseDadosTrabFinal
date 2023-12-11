class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def troca_cor(self, nova_cor):
        self.cor = nova_cor

    def mostra_cor(self):
        return self.cor

# Exemplo de uso da classe Bola
minha_bola = Bola("rosa", 2, "couro")
print("Cor atual da bola:", minha_bola.mostra_cor())  

minha_bola.troca_cor("verde")
print("Cor atual da bola:", minha_bola.mostra_cor())  
