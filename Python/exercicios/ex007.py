class ContaBancaria:
    def __init__(self, numero_conta, titular, saldo_inicial=0.0):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
        elif valor <= 0:
            print("O valor do saque deve ser positivo.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")

    def exibir_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")


conta = ContaBancaria("12345-6", "Miguel Ferraz", 1500)

conta.exibir_saldo()
conta.depositar(500)
conta.sacar(200)
conta.sacar(2000)
conta.exibir_saldo()
