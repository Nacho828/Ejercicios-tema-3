from Polinomio import Polinomio
#             for exp2, coef2 in otro.terminos.items():
# Ejemplo de uso
if __name__ == "__main__":
    p1 = Polinomio({2: 3, 1: 4, 0: -5})  # 3x^2 + 4x - 5
    p2 = Polinomio({1: 1, 0: -1})        # x - 1

    print("Polinomio 1:", p1)
    print("Polinomio 2:", p2)

    resta = p1.restar(p2)
    print("Resta:", resta)

    cociente, residuo = p1.dividir(p2)
    print("Cociente:", cociente)
    print("Residuo:", residuo)

    p1.eliminar_termino(1)
    print("Polinomio 1 después de eliminar término x^1:", p1)

    existe = p1.existe_termino(2)
    print("¿Existe el término x^2 en Polinomio 1?", existe)