from configuraciones import *
from Class_superficie import Superficie
from Class_personaje import Personaje
import random 
class Item(Superficie):
    def __init__(self, tamaño, posicion_inicial, path_img):
        super().__init__(tamaño, posicion_inicial, path_img)
        self.sonido_nueva_vida = pygame.mixer.Sound("PROYECTO PYGAME\\Recursos\\SonidoNuevaVida\\654251__strechy__item-pickup-sound.ogg")
        self.sonido_nueva_vida.set_volume(0.5)
        self.sonido_recoger_municion = pygame.mixer.Sound("PROYECTO PYGAME\\Recursos\\SonidoRecogerMunicion\\276160__littlerobotsoundfactory__coins_few_11.wav")
        self.sonido_recoger_municion.set_volume(0.5)

    def aplicar_efecto(self, personaje: Personaje):
            if personaje.lados["main"].colliderect(self.lados["main"]):
                personaje.municion += 1
                self.sonido_recoger_municion.play()
                self.desaparecer_item()

    def aplicar_vida(self, personaje: Personaje):
        if personaje.lados["main"].colliderect(self.lados["main"]):
            personaje.vida += 1
            self.sonido_nueva_vida.play()
            self.desaparecer_item()            
            
    def desaparecer_item(self):
        self.lados["main"].x = random.randrange(0,740,60)
        self.lados["main"].y = random.randrange(-1000, 0, 60)         