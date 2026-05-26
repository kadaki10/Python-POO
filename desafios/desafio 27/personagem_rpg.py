import random
from rich import print
from abc import ABC, abstractmethod

class Personagem(ABC):
    def __init__(self, nome, vida ):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def atacar(self, alvo, forca = 100):
        if self.vida > 0 and alvo.vida > 0:
            golpe = self.golpes[random.randrange(0, len(self.golpes))]
            print(f"[green]{self.nome}[/]({self.vida}) atacou [red]{alvo.nome}[/]({alvo.vida}) com um [blue]{golpe}[/] de força {forca}")
            alvo.receber_dano(forca)
        else:
            print(f"O ataque {self.nome} -> {alvo.nome} não pode acontecer")

    def receber_dano(self, dano):
        fator = random.randint(0, dano)
        self.vida -= fator
        if self.vida < 0:
            self.vida = 0
        print(f"[blue]{self.nome}[/] recebeu [red] dano de {fator}[/]!")

    @abstractmethod
    def curar(self):
        pass



class Guerreiro(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Soco", "Golpe de machado", "Pulo giratorio"]

    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator
        print(f"[blue]{self.nome}[/] enrolou uma atadura nos ferimentos e [green] recuperou {fator} pontos [/] de vida.")


class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Bolas de fogo", "Raio de luz", "Magia estatica"]

    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator
        print(f"[blue]{self.nome}[/] fez uma magia de cura e [green] recuperou {fator} pontos[/] de vida.")
