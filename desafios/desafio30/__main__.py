from desafios.desafio30.classe30 import Credencial

def main():
    c = Credencial()
    c.senha = str(input("Digite sua senha: "))
    print(c.senha)

    c.validar('Kadaki')


if __name__ == "__main__":
    main()