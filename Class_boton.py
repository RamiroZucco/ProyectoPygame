import pygame
from pygame.locals import *
class Boton:
    def __init__(self, imagen_path, posicion):
        self.imagen = pygame.image.load(imagen_path)
        self.rect = self.imagen.get_rect()
        self.rect.bottomright = posicion

    def dibujar(self, screen):
        screen.blit(self.imagen, self.rect)

    def verificar_clic(self, event):
        if event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            return True
        return False