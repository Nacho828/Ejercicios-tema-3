
import pygame
import sys

class Piedra:
    def __init__(self, ancho, color):
        self.ancho = ancho
        self.color = color

    def dibujar(self, pantalla, x, y, altura):
        pygame.draw.rect(pantalla, self.color, (x - self.ancho // 2, y - altura, self.ancho, altura))