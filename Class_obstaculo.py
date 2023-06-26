from configuraciones import *
from Class_superficie import Superficie 
class Obstaculo(Superficie):
    def __init__(self, tamaño, posicion_inicial, path_img):
        super().__init__(tamaño, posicion_inicial, path_img)
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        rectangulo = self.imagen.get_rect()
        rectangulo.x = posicion_inicial[0]
        rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulos(rectangulo)