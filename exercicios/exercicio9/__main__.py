from exercicios.exercicio9.exercicio9 import Avaliacao
from rich import print, inspect

def main():
    av1 = Avaliacao("Pedro", "Matematica", 9.5)
    av1.set_nota = (-2.5)
    inspect(av1, private=True)

if __name__ == "__main__":
    main()