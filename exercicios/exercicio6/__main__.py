from rich import print, inspect
from aluno import Aluno
from professor import Professor
from funcionario import Funcionario


a1 = Aluno("José", 17, "Informatica", "T01")
a1.fazer_aniversario()
inspect(a1, methods= True)

p1 = Professor("Luiz", 23, "Finanças", "Estagiario")
a1.fazer_aniversario()
inspect(p1, methods= True)



f1 = Funcionario("Claudia", 27, "Secretaria", "Secretaria")
f1.fazer_aniversario()
f1.bater_ponto()
inspect(f1, methods=True)