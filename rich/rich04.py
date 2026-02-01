from rich import print
from rich import inspect

class ContaBancaria:
    """
Cri uma conta bancaria e permite fazer saques e depositos
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo."


    def depositar(self, valor):
        self.saldo += valor
        print(f"Deposito de R${valor:,.2f} autorizado na conta {self.id} ")

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"saque NEGADO de R${valor:,.2f} na conta {self.id}: SALDO INSUFICIENTE")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:,.2f} autorizado na conta {self.id} ")


c = ContaBancaria(112, "José", 500)
inspect(c)
