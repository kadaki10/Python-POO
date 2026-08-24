from rich import print, inspect
from desafios.desafio29.classes29 import Diario

def main():
    meudiario = Diario()
    meudiario.escrever("Essa e a primeira mensagem")
    meudiario.escrever("Estou aprendendo Python")

    try:
        meudiario.ler('CeV!@')
    except Exception as e:
        print(f"[red]ERRO: {e}")

    #inspect(meudiario, private=True)


if __name__ == "__main__":
    main()