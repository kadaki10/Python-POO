from desafios.desafio40.classe40 import *

def main():
    u = [Usuario("José", "jjsilva@hotmail.com"), Usuario("Ana", "aninha@gmail.com")]

    a = [Aluno("Maria", "Administração", "3 ano"), Aluno("Paulo", "Gastronomia", "1 ano")]

    exportar_dados(XML(), u)
    exportar_dados(JSON(), a)

if __name__ == "__main__":
    main()