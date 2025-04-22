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
            piedra = Piedra(i * 30, colores[i % len(colores)])
            self.columnas[0].agregar_piedra(piedra)

        self.seleccionada = None