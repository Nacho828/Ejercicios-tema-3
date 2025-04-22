import pygame
import sys
from Columna import Columna
from Piedra import Piedra


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
            color = colores[(i - 1) % len(colores)]
            piedra = Piedra(i * 30, color)
            self.columnas[0].agregar_piedra(piedra)

        self.seleccionada = None

    def ejecutar(self):
        """Método principal para ejecutar el bucle del juego."""
        corriendo = True
        while corriendo:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    corriendo = False

            # Limpiar la pantalla
            self.pantalla.fill((0, 0, 0))

            # Dibujar columnas y piedras
            for columna in self.columnas:
                columna.dibujar(self.pantalla)

            # Actualizar la pantalla
            pygame.display.flip()
            self.reloj.tick(60)

        pygame.quit()
        sys.exit()