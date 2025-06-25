import pygame
from .recursos import *

def dibujar_backups(pantalla, ancho_pantalla, ancho_contenedor, alto_contenedor, margen_superior=20) -> None:
    '''
    
    '''
    ESPACIO = ancho_pantalla // 7

    for i in range(1, 5):  # índices del 1 al 4 porque el 0 va a ser el mazo.
        x = i * ESPACIO + (ESPACIO - ancho_contenedor) // 2
        y = margen_superior
        pygame.draw.rect(pantalla, GRIS, (x, y, ancho_contenedor, alto_contenedor))

