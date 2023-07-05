import pygame
import sys
from pygame.locals import *
from GUI.GUI_form_principal import *

W,H = 1900,900
TAMAÑO_PANTALLA = (W,H)
FPS = 18
pygame.init()    
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode(TAMAÑO_PANTALLA)
icono = pygame.image.load("PROYECTO PYGAME\\Recursos\\Dispara\\16.png")
pygame.display.set_icon(icono)
form_principal = FormPrincipal(PANTALLA,0,0,PANTALLA.get_width(),PANTALLA.get_height(),True,"PROYECTO PYGAME\\Recursos\\Interfaz\\1.png")
while True:
    RELOJ.tick(FPS)
    eventos = pygame.event.get()
    PANTALLA.fill("Black")
    for evento in eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    form_principal.update(eventos)                  
    pygame.display.update()                     