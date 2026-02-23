class Eletrodomestico:
    def __init__(self, cor, potencia, tensao, preco):
        self.cor = cor
        self.potencia = potencia
        self.tensao = tensao
        self.preco = preco


class Ventilador(Eletrodomestico):
    def __init__(self, cor, potencia, tensao, preco, quantidade_de_portas=1):
        super().__init__(cor, potencia, tensao, preco)
        self.quantidade_de_portas = quantidade_de_portas


class Pessoa:
    def __init__(self, nome, saldo_na_conta):
        self.nome = nome
        self.saldo_na_conta = saldo_na_conta
        self.eletrodomesticos = []

    def comprar_eletrodomestico(self, eletrodomestico):
        if eletrodomestico.preco <= self.saldo_na_conta:
            self.saldo_na_conta -= eletrodomestico.preco
            self.eletrodomesticos.append(eletrodomestico)
            print("Compra realizada!")
        else:
            print("Saldo insuficiente!")


# Criando objetos
vent = Ventilador("Preto", 200, 110, 300)
pessoa = Pessoa("João", 500)

# Fazendo compra
pessoa.comprar_eletrodomestico(vent)

# Mostrando saldo restante
print("Saldo restante:", pessoa.saldo_na_conta)