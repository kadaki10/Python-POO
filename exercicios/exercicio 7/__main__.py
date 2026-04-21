from rich import print, inspect
from classes import Pessoa, Aluno, Professor, Funcionario

def main():
    a1 = Aluno("José", 17, "Informatica", "TO1")
    a1.fazer_aniversario()
    a1.fazer_matricula()
    inspect(a1, methods= True)

    p1 = Professor("Luiz", 23, "Finanças", "Estagiario")
    p1.fazer_aniversario()
    inspect(p1, methods= True)


    f1 = Funcionario("Claudia", 27, "Secretaria", "Secretaria")
    f1.fazer_aniversario()
    f1.bater_ponto()
    inspect(f1, methods=True)

    a1.estudar()
    p1.estudar()
    f1.estudar()

if __name__ == '__main__':
    main()