from Matriz3x3 import Matriz3x3

# Ejemplo de uso
if __name__ == "__main__":
    matriz = [
        [2, 3, 1],
        [4, 5, 6],
        [7, 8, 9]
    ]
    matriz_obj = Matriz3x3(matriz)

    print("Determinante (Recursivo):", matriz_obj.determinante_recursivo())
    print("Determinante (Iterativo):", matriz_obj.determinante_iterativo())