from rich import print
from rich.panel import Panel

class Churrasco:
    # Atributos de Classe
    consumidor_padrão:float = 0.400 # Cada pessoa come em média 400g de carne
    preço_kg:float = 82.40 # Cada Kg de carne custa 82.40

    def __init__(self, titulo, quant):
        # Atributos de Instancia
        self.titulo = titulo
        self.participantes = quant

    def __str__(self):
        return f"Esse é {self.titulo} com {self.participantes} pessoas participando."

    def calcular_qtd_carne(self) -> float:
        return self.participantes * Churrasco.consumidor_padrão

    def calcular_custo_total(self) -> float:
        return self.calcular_qtd_carne() * Churrasco.preço_kg

    def calcular_custo_individual(self) -> float:
        return self.calcular_custo_total() / self.participantes

    def analisar(self):
        conteudo = f"Analisando [green]{self.titulo}[/] com [blue]{self.participantes} convidados [/]"
        conteudo += f"\nCada participante comerá {Churrasco.consumidor_padrão}Kg e cada Kg custa R${Churrasco.preço_kg:,.2f}"
        conteudo += f"\nRecomendo [blue]comprar {self.calcular_qtd_carne():.3f}Kg[/] de carne"
        conteudo += f"\nO custo total será de [green]R${self.calcular_custo_total():,.2f}[/]"
        conteudo += f"\nCada pessoa pagará [yellow]R${self.calcular_custo_individual():,.2f} [/] para participar."
        painel = Panel(conteudo, title=self.titulo)
        print(painel)

c1 = Churrasco("Churras dos amigos", 15)
c1.analisar()



