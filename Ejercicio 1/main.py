import pygame
import sys

# Clase para representar una piedra preciosa (TDA)
class Piedra:
    def __init__(self, ancho, color):
        self.ancho = ancho
        self.color = color

    def dibujar(self, pantalla, x, y, altura):
        pygame.draw.rect(pantalla, self.color, (x - self.ancho // 2, y - altura, self.ancho, altura))

# Clase para representar una columna
class Columna:
    def __init__(self, x, y, altura):
        self.x = x
        self.y = y
        self.altura = altura
        self.piedras = []

    def agregar_piedra(self, piedra):
        if not self.piedras or piedra.ancho < self.piedras[-1].ancho:
            self.piedras.append(piedra)
        else:
            raise ValueError("No se puede colocar una piedra más grande sobre una más pequeña.")

    def quitar_piedra(self):
        if self.piedras:
            return self.piedras.pop()
        return None

    def dibujar(self, pantalla):
        # Dibujar la columna
        pygame.draw.rect(pantalla, (200, 200, 200), (self.x - 10, self.y - self.altura, 20, self.altura))
        # Dibujar las piedras
        altura_piedra = 20
        for i, piedra in enumerate(reversed(self.piedras)):
            piedra.dibujar(pantalla, self.x, self.y - i * altura_piedra, altura_piedra)

# Clase para manejar la aplicación con Pygame
class Aplicacion:
    def __init__(self, ancho, alto):
        pygame.init()
        self.ancho = ancho
        self.alto = alto
        self.pantalla = pygame.display.set_mode((ancho, alto))
        pygame.display.set_caption("Puzzle de la Pirámide de Piedras Preciosas")
        self.reloj = pygame.time.Clock()

        # Crear columnas
        self.columnas = [
            Columna(200, 500, 300),
            Columna(400, 500, 300),
            Columna(600, 500, 300)
        ]

        # Crear piedras y agregarlas a la primera columna
        colores = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]
        for i in range(5, 0, -1):
            piedra = Piedra(i * 30, colores[i % len(colores)])
            self.columnas[0].agregar_piedra(piedra)

        self.seleccionada = None

    def ejecutar(self):
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    self.seleccionar_columna(evento.pos)
                elif evento.type == pygame.MOUSEBUTTONUP:
                    self.soltar_piedra(evento.pos)

            # Dibujar en la pantalla
            self.pantalla.fill((0, 0, 0))  # Fondo negro
            for columna in self.columnas:
                columna.dibujar(self.pantalla)
            pygame.display.flip()
            self.reloj.tick(30)

    def seleccionar_columna(self, posicion):
        for columna in self.columnas:
            if columna.x - 50 < posicion[0] < columna.x + 50:
                if not self.seleccionada:
                    self.seleccionada = columna.quitar_piedra()
                break

    def soltar_piedra(self, posicion):
        if self.seleccionada:
            for columna in self.columnas:
                if columna.x - 50 < posicion[0] < columna.x + 50:
                    try:
                        columna.agregar_piedra(self.seleccionada)
                        self.seleccionada = None
                        return
                    except ValueError:
                        pass
            # Si no se pudo colocar, devolver la piedra a su columna original
            for columna in self.columnas:
                if not columna.piedras or self.seleccionada.ancho < columna.piedras[-1].ancho:
                    columna.agregar_piedra(self.seleccionada)
                    self.seleccionada = None
                    return

# Crear y ejecutar la aplicación
if __name__ == "__main__":
    app = Aplicacion(800, 600)
    app.ejecutar()