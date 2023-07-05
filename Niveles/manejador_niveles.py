from pygame.locals import *
from Niveles.Class_nivel_uno import NivelUno
from Niveles.Class_nivel_dos import NivelDos
from Niveles.Class_nivel_tres import NivelTres

class Manejador_niveles:
    def __init__(self,pantalla):
        self._slave = pantalla
        self.niveles = {"nivel_uno": NivelUno, "nivel_dos": NivelDos, "nivel_tres": NivelTres}

    def get_nivel(self, nombre_nivel):
        return self.niveles[nombre_nivel](self._slave)

