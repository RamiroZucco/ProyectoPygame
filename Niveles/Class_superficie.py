import pygame
from Niveles.configuraciones import *
class Superficie:
    def __init__(self,tamaño, posicion_inicial,path_img):
        self.imagen = pygame.image.load(path_img)
        self.imagen = pygame.transform.scale(self.imagen,tamaño)

        rectangulo = self.imagen.get_rect()
        rectangulo.x = posicion_inicial[0]
        rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulos(rectangulo)