from desafios.desafio36.classe36 import *

def main():

    finalizar_compra(Pix(), 1500)
    finalizar_compra(CartaoCredito(), 9540.84)
    finalizar_compra(Boleto(), 439.23)

if __name__ == "__main__":
    main()