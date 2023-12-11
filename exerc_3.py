class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterar_nome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

# Exemplo de uso da classe ContaCorrente
conta = ContaCorrente(123, "João")

print("Nome do correntista:", conta.nome_correntista)
print("Número da conta:", conta.numero_conta)
print("Saldo:", conta.saldo)

conta.alterar_nome("Maria")
print("Novo nome do correntista:", conta.nome_correntista)

conta.deposito(1000)
print("Saldo após depósito:", conta.saldo)

conta.saque(500)
print("Saldo após saque:", conta.saldo)

conta.saque(800)
print("Saldo após saque:", conta.saldo)
