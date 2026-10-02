from desafios.desafio38.classe38 import *

def main():
    p1 = Produto("Notebook", 8_500)
    p2 = Produto("Mouse", 250)
    p3 = Produto("Fone de ouvido", 450.35)

    c1 = Carrinho()
    c2 = Carrinho()

    c1 = c1 + p1
    c1 = c1 + p2
    c1 = c1 + p3

    c2 = c2 + c1

    print(c1)
    print(c2)

if __name__ == "__main__":
    main()

