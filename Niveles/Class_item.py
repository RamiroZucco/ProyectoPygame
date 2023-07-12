import pygame
from Niveles.Class_superficie import Superficie
from Niveles.Class_personaje import Personaje
import random 
class Item(Superficie):
    def __init__(self, tamaño, posicion_inicial, path_img):
        super().__init__(tamaño, posicion_inicial, path_img)
        self.sonido_nueva_vida = pygame.mixer.Sound("PROYECTO PYGAME copy\\Recursos\\SonidoNuevaVida\\654251__strechy__item-pickup-sound.ogg")
        self.sonido_nueva_vida.set_volume(0.5)
        self.sonido_recoger_municion = pygame.mixer.Sound("PROYECTO PYGAME copy\\Recursos\\SonidoRecogerMunicion\\276160__littlerobotsoundfactory__coins_few_11.wav")
        self.sonido_recoger_municion.set_volume(0.5)
        self.sonido_score = pygame.mixer.Sound("PROYECTO PYGAME copy\\Recursos\\SonidoScore\\456693__combine2005__pickup_coin56.wav")
        self.sonido_score.set_volume(0.5)

    def aplicar_efecto(self, personaje: Personaje):
            if personaje.lados["main"].colliderect(self.lados["main"]):
                personaje.municion += 1
                self.sonido_recoger_municion.play()
                self.desaparecer_item()

    def aplicar_vida(self, personaje: Personaje):
        if personaje.lados["main"].colliderect(self.lados["main"]):
            self.sonido_nueva_vida.play()
            personaje.vida += 1   
            self.desaparecer_item() 
                    
    def aumentar_score(self, personaje: Personaje):
        if personaje.lados["main"].colliderect(self.lados["main"]):
            personaje.score += 100
            self.sonido_score.play()
            self.desaparecer_item()

    def desaparecer_item(self):
        self.lados["main"].x = 8000
        self.lados["main"].y = 8000       