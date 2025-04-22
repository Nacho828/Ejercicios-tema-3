import pygame
import sys

from columna import Columna
from piedra import Piedra
from lanzador import Lanzador

# Crear y ejecutar la aplicación
if __name__ == "__main__":
    app = Aplicacion(800, 600)
    app.ejecutar()