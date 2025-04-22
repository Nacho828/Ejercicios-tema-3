class Polinomio:
    def __init__(self, terminos=None):
        """
        Inicializa un polinomio. Los términos se representan como un diccionario
        donde las claves son los exponentes y los valores son los coeficientes.
        """
        self.terminos = terminos if terminos else {}

    def __str__(self):
        """
        Representa el polinomio como una cadena legible.
        """
        if not self.terminos:
            return "0"
        terminos_str = []
        for exponente, coeficiente in sorted(self.terminos.items(), reverse=True):
            if coeficiente != 0:
                terminos_str.append(f"{coeficiente}x^{exponente}" if exponente != 0 else f"{coeficiente}")
        return " + ".join(terminos_str).replace("+ -", "- ")

    def restar(self, otro):
        """
        Resta otro polinomio del actual.
        """
        resultado = Polinomio(self.terminos.copy())
        for exponente, coeficiente in otro.terminos.items():
            resultado.terminos[exponente] = resultado.terminos.get(exponente, 0) - coeficiente
        return resultado

    def dividir(self, otro):
        """
        Divide el polinomio actual por otro polinomio. Devuelve el cociente y el residuo.
        """
        cociente = Polinomio()
        residuo = Polinomio(self.terminos.copy())

        while residuo.terminos and max(residuo.terminos) >= max(otro.terminos):
            exponente_residuo = max(residuo.terminos)
            exponente_otro = max(otro.terminos)
            coeficiente_residuo = residuo.terminos[exponente_residuo]
            coeficiente_otro = otro.terminos[exponente_otro]

            nuevo_exponente = exponente_residuo - exponente_otro
            nuevo_coeficiente = coeficiente_residuo / coeficiente_otro

            termino_division = Polinomio({nuevo_exponente: nuevo_coeficiente})
            cociente = cociente.sumar(termino_division)
            residuo = residuo.restar(termino_division.multiplicar(otro))

        return cociente, residuo

    def eliminar_termino(self, exponente):
        """
        Elimina un término del polinomio dado su exponente.
        """
        if exponente in self.terminos:
            del self.terminos[exponente]

    def existe_termino(self, exponente):
        """
        Determina si un término con el exponente dado existe en el polinomio.
        """
        return exponente in self.terminos

    def sumar(self, otro):
        """
        Suma otro polinomio al actual.
        """
        resultado = Polinomio(self.terminos.copy())
        for exponente, coeficiente in otro.terminos.items():
            resultado.terminos[exponente] = resultado.terminos.get(exponente, 0) + coeficiente
        return resultado

    def multiplicar(self, otro):
        """
        Multiplica el polinomio actual por otro polinomio.
        """
        resultado = Polinomio()
        for exp1, coef1 in self.terminos.items():
            for exp2, coef2 in otro.terminos.items():
                nuevo_exponente = exp1 + exp2
                nuevo_coeficiente = coef1 * coef2
                resultado.terminos[nuevo_exponente] = resultado.terminos.get(nuevo_exponente, 0) + nuevo_coeficiente
        return resultado
