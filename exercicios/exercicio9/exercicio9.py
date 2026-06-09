class Avaliacao:

    def __init__(self, nome, disciplina, nota):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota

    # Metodos Acessores
    def get_nota(self): # Metodo Getter
        return self._nota

    def set_nota(self, valor): # Metodo Setter
        if  0 <= valor <= 10:
            self._nota = valor
        else:
            print("Nota invalida!")







