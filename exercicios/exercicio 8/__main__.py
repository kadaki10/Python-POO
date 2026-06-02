from exercicio08 import ContaBancaria

def main():
    c1 = ContaBancaria(111, "Maria", 5_000)
    c1.depositar(1_000)
    c1._titular = "Pedr" #Ele deixa, mas não mexa pois 'Adultos estão consetindo'...

    c1._ContaBancaria__saldo = 0
    print(c1)

if __name__ == "__main__":
    main()