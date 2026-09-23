from abc import ABC, abstractmethod
import locale

class Pagamento(ABC):

    def __init__(self):
        self._valor = None

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor: float):
        if valor > 0:
            self._valor = valor
        else:
            raise ValueError(f"O pagamento só pode ser efetuado para valores positivos")

    @property
    def fvalor(self):
        # return f"R{self._valor:,.2f}"
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        return locale.currency(self._valor, grouping=True, symbol=True, international=False)

    @abstractmethod
    def pagar(self, valor:float):
        pass

class Boleto(Pagamento):
    def pagar(self, valor: float):
        try:
            self.valor = valor
            # Código para efetuar o pagamento
            return f"Pagamento CONFIRMADO de {self.fvalor} via Boleto"
        except Exception as e:
            return f"Falha no pagamento de {self.fvalor} via Boleto!"



class Pix(Pagamento):
    def pagar(self, valor: float):
        try:
            self.valor = valor
            # Código para efetuar o pagamento
            return f"Pagamento CONFIRMADO de {self.fvalor} via Pix"
        except Exception as e:
            return f"Falha no pagamento de {self.fvalor} via Pix!"


class CartaoCredito(Pagamento):
    def pagar(self, valor:float):
        try:
            self.valor = valor
            # Código para efetuar o pagamento
            return f"Pagamento CONFIRMADO de {self.fvalor} via Cartão de crédito"
        except Exception as e:
            return f"Falha no pagamento de {self.fvalor} via Cartao de Credito!"


def finalizar_compra(tipo_pag: Pagamento, valor:float):
    print(tipo_pag.pagar(valor))