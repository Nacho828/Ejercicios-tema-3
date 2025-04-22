from Piedra import Piedra
import pygame
import sys

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
