class Matriz3x3:
    def __init__(self, matriz):
        if len(matriz) != 3 or any(len(fila) != 3 for fila in matriz):
            raise ValueError("La matriz debe ser de 3x3.")
        self.matriz = matriz

    def determinante_recursivo(self):
        def determinante(m):
            if len(m) == 2:
                # Determinante de una matriz 2x2
                return m[0][0] * m[1][1] - m[0][1] * m[1][0]
            det = 0
            for i in range(len(m)):
                submatriz = [fila[:i] + fila[i+1:] for fila in m[1:]]
                det += ((-1) ** i) * m[0][i] * determinante(submatriz)
            return det

        return determinante(self.matriz)

    def determinante_iterativo(self):
        a, b, c = self.matriz[0]
        d, e, f = self.matriz[1]
        g, h, i = self.matriz[2]
        # Fórmula del determinante de una matriz 3x3
        return (a * e * i + b * f * g + c * d * h) - (c * e * g + b * d * i + a * f * h)
