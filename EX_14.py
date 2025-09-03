class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self._saldo = saldo_inicial

    @property
    def saldo(self):
        # atributo somente leitura
        return self._saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0:
            if valor <= self._saldo:
                self._saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente para saque.")
        else:
            print("Valor de saque inválido.")


conta = ContaBancaria(100)
print(f"Saldo inicial: R${conta.saldo:.2f}")

conta.depositar(50)
print(f"Saldo depois depósito: R${conta.saldo:.2f}")

conta.sacar(30)
print(f"Saldo depois saque: R${conta.saldo:.2f}")

conta.sacar(150)
print(f"Saldo final: R${conta.saldo:.2f}")