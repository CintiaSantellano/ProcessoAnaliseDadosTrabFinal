class Tamagotchi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def alterar_fome(self, nova_fome):
        self.fome = nova_fome

    def alterar_saude(self, nova_saude):
        self.saude = nova_saude

    def alterar_idade(self, nova_idade):
        self.idade = nova_idade

    def retornar_nome(self):
        return self.nome

    def retornar_fome(self):
        return self.fome

    def retornar_saude(self):
        return self.saude

    def retornar_idade(self):
        return self.idade


# Exemplo de uso da classe Tamagotchi
bichinho = Tamagotchi("Lalá", 5, 8, 2)

print("Nome:", bichinho.retornar_nome())
print("Fome:", bichinho.retornar_fome())
print("Saúde:", bichinho.retornar_saude())
print("Idade:", bichinho.retornar_idade())

bichinho.alterar_nome("Nena")
bichinho.alterar_fome(3)
bichinho.alterar_saude(9)
bichinho.alterar_idade(3)

print("Nome:", bichinho.retornar_nome())
print("Fome:", bichinho.retornar_fome())
print("Saúde:", bichinho.retornar_saude())
print("Idade:", bichinho.retornar_idade())
