import pygame
import sys
#from pygame import mixer
from paquete.recursos import *
from paquete.dibujar import *
from paquete.cartas import *
from paquete.tablero import *
from paquete.muestra import *


# Inicialización
pygame.init()

#mixer.init()

pantalla = pygame.display.set_mode((ANCHO, ALTO)) # Crear la ventana principal

#mixer.music.load("./solitario/recursos/sonidos/.mp3")
#mixer.music.play()
#mixer.music.set_volume(0.5)

pygame.display.set_caption("Solitario") # Nombre de la ventana

reloj = pygame.time.Clock()


img = pygame.image.load("icono.jpg") # Cargar imagen para icon
pygame.display.set_icon(img) # Icono de la ventana

# Dibujar una pantalla
pantalla.fill(VERDE)

# Dibujar los backups
dibujar_backups(pantalla, ANCHO, ANCHO_CARTA, ALTO_CARTA)

#carta = crear_carta("./cartas/2 de copa.jpg", 500, 500, "copa", 2)

mazo = crear_mazo()
mazo_barajado = barajar_mazo(mazo)
print(mazo)
tablero = crear_tablero()

pantalla.blit(mazo_barajado[0]["superficie"], mazo_barajado[0]["rect_pos"])


jugando = True
while jugando:
    
    reloj.tick(FPS)

    # Gestionar eventos (por ej, cerrar la ventana)
    for evento in pygame.event.get():

       if evento.type == pygame.QUIT:
            pygame.quit()
            ejecutar = False

    # Actualizar la pantalla
    pygame.display.update()

pygame.quit()
sys.exit()