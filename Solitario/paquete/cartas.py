import pygame
import random
from paquete.recursos import *


def crear_carta (ruta_imagen: str, palo: str, num: int, x: int = 0, y: int = 0)  -> dict:

    carta = {}
    carta["superficie"] = pygame.image.load(ruta_imagen)
    carta["superficie"] = pygame.transform.scale(carta["superficie"], (ANCHO_CARTA, ALTO_CARTA))
    carta["rect_pos"] = pygame.Rect(x, y, ANCHO_CARTA, ALTO_CARTA)
    carta["rect"] =  pygame.Rect((x + ANCHO / 2) - 10, y + 90, ANCHO_CARTA, ALTO_CARTA)
    carta["palo"] = palo
    carta["numero"] = num

    return carta


def crear_mazo() -> list:
    
    mazo = []

    for palo in PALOS:
        for n in range(1, 11):
            ruta = str(n) + " de " + palo + ".jpg"
            carta_nueva = crear_carta("./cartas/" + ruta, palo, n)
            mazo.append(carta_nueva)

    return mazo

def barajar_mazo(mazo: list) -> None:
    random.shuffle(mazo)
    return mazo