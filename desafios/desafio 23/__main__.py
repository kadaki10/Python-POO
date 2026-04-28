from rich import print, inspect
from poligono import Quadrado, Circulo

def main():
    q = Quadrado(20)

    print(f"Um quadrado de lado {q.lado} tem perimetro de {q.perimetro()}cm")
    print(f"Um quadrado de lado {q.lado} tem area de {q.area()}cm2")


    c = Circulo(12)
    print(f"Um circulo de raio {c.raio}cm tem perimetro de {c.perimetro():.1f}cm")
    print(f"Um circulo de raio {c.raio}cm tem area de {c.area():.1f}cm2")
    inspect(c, methods=True)


if __name__ == "__main__":
    main()

