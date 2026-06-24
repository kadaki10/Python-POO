from desafios.desafio28.classes28 import *

def main():
    t = Termostato()
    try:
        t.temperatura = 22.2
        print(t.ftemperatura)
    except Exception as e:
        print(f"Houve um problema: {e}")

    print(f"A temperatura atual é de {t.ftemperatura}")

if __name__ == "__main__":
    main()