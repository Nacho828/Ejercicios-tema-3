from piedra import Piedra
import pygame
import sys


class Lanzador:
    def __init__(self, pantalla, columnas, reloj):
        self.pantalla = pantalla
        self.columnas = columnas
        self.reloj = reloj
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