import pygame
from Niveles.nivel import Nivel
from Niveles.Class_personaje import Personaje
from Niveles.Class_superficie import Superficie
from Niveles.Class_enemigo import Enemigo
from Niveles.Class_item import Item
from Niveles.Class_obstaculo import Obstaculo
from Niveles.configuraciones import *

class NivelUno(Nivel):
    def __init__(self, pantalla: pygame.Surface):
        W = pantalla.get_width()
        H = pantalla.get_height()

        fondo = pygame.image.load("PROYECTO PYGAME\Recursos\Fondos_Imagenes\Fondo.png")
        fondo = pygame.transform.scale(fondo, (W,H))

        posicion_inicial = (H/2 - 300, 490)
        tamaño = (55, 75)

        tiempo_total = 30
        tiempo_restante = tiempo_total * 20

        diccionario_animaciones = {}
        diccionario_animaciones["Quieto_Izquierda"] = personaje_quieto_izquierda
        diccionario_animaciones["Quieto_Derecha"] = personaje_quieto_derecha
        diccionario_animaciones["Salta_Izquierda"] = personaje_salta_izquierda
        diccionario_animaciones["Salta_Derecha"] = personaje_salta_derecha
        diccionario_animaciones["Izquierda"] = personaje_camina_izquierda
        diccionario_animaciones["Derecha"] = personaje_camina_derecha
        diccionario_animaciones["Dañado"] = personaje_dañado

        diccionario_animaciones_enemigo = {}
        diccionario_animaciones_enemigo["Derecha"] = perro_derecha
        diccionario_animaciones_enemigo["Izquierda"] = perro_izquierda

        diccionario_animaciones_enemigo_dos = {}
        diccionario_animaciones_enemigo_dos["Izquierda"] = pajaro_izquierda
        diccionario_animaciones_enemigo_dos["Derecha"] = pajaro_derecha

        personaje = Personaje(tamaño,diccionario_animaciones,posicion_inicial,12,W,3)

        plataforma_piso = Superficie((W, 20), (0, personaje.lados["main"].bottom),"PROYECTO PYGAME\Recursos\Superficie\pngwing.com (1).png")
        plataforma = Superficie((200,55),(500,450),"PROYECTO PYGAME\\Recursos\\Superficie\\0.png")
        plataforma_dos = Superficie((200,55),(800,350),"PROYECTO PYGAME\\Recursos\\Superficie\\0.png")
        plataforma_tres = Superficie((200,55),(450,250),"PROYECTO PYGAME\\Recursos\\Superficie\\0.png")
        plataforma_cuatro = Superficie((200,55),(1100,450),"PROYECTO PYGAME\\Recursos\\Superficie\\0.png")

        obstaculo = Obstaculo((50, 20),(plataforma.lados["main"].left, plataforma.lados["main"].top - 20), "PROYECTO PYGAME\\Recursos\\Superficie\\22.png")
        obstaculo_dos = Obstaculo((50, 20), (plataforma.lados["main"].right - obstaculo.ancho, plataforma.lados["main"].top - 20), "PROYECTO PYGAME\\Recursos\\Superficie\\22.png")
        obstaculo_tres = Obstaculo((50, 20), (plataforma_dos.lados["main"].centerx - obstaculo.ancho / 2, plataforma_dos.lados["main"].y - obstaculo.alto),"PROYECTO PYGAME\\Recursos\\Superficie\\22.png")
        obstaculo_cuatro = Obstaculo((50, 20), (plataforma_cuatro.lados["main"].left, plataforma_cuatro.lados["main"].top - 20),"PROYECTO PYGAME\\Recursos\\Superficie\\22.png")
        obstaculo_cinco = Obstaculo((50, 20), (plataforma_cuatro.lados["main"].right - obstaculo.ancho, plataforma_cuatro.lados["main"].top - 20),"PROYECTO PYGAME\\Recursos\\Superficie\\22.png")
        obstaculo_seis = Obstaculo((50, 20), (plataforma_cuatro.lados["main"].centerx - obstaculo.ancho / 2, plataforma_cuatro.lados["main"].y - obstaculo.alto),"PROYECTO PYGAME\\Recursos\\Superficie\\22.png")

        enemigo = Enemigo((55,55),diccionario_animaciones_enemigo, (H/2, 510),10,W)
        enemigo_dos = Enemigo((55,55),diccionario_animaciones_enemigo_dos, (1000, 150),11,W)

        municion = Item((30,25), (obstaculo.lados["main"].right + 35 ,plataforma.lados["main"].top - 28),"PROYECTO PYGAME\\Recursos\\Disparo\\23.png")
        municion_dos = Item((30,25),(1000, 520),"PROYECTO PYGAME\\Recursos\\Disparo\\23.png")
        municion_tres = Item((30,25),(plataforma_dos.lados["main"].right - obstaculo.ancho, plataforma_dos.lados["main"].top - 28),"PROYECTO PYGAME\\Recursos\\Disparo\\23.png")
        municion_cuatro = Item((30,25),(plataforma_dos.lados["main"].left + 20, plataforma_dos.lados["main"].top - 28),"PROYECTO PYGAME\\Recursos\\Disparo\\23.png")
        municion_cinco = Item((30,25),(1180, 280),"PROYECTO PYGAME\\Recursos\\Disparo\\23.png")
        vida = Item((30,25), (obstaculo.lados["main"].right -10 ,plataforma_tres.lados["main"].top - 28),"PROYECTO PYGAME\\Recursos\\Vida\\pngegg.png")
        item_score = Item((30,25),(230,300),"PROYECTO PYGAME\\Recursos\\Score\\0.png")
        item_score_dos = Item((30,25),(1500,520),"PROYECTO PYGAME\\Recursos\\Score\\0.png")
        item_score_tres = Item((30,25),(880,470),"PROYECTO PYGAME\\Recursos\\Score\\0.png")


        lista_plataformas = [plataforma_piso, plataforma, plataforma_dos, plataforma_tres, plataforma_cuatro]
        lista_obstaculos = [obstaculo, obstaculo_dos, obstaculo_tres, obstaculo_cuatro, obstaculo_cinco, obstaculo_seis]
        lista_municiones = [municion,municion_dos, municion_tres, municion_cuatro, municion_cinco]
        lista_vidas = [vida]
        lista_enemigos = [enemigo,enemigo_dos]
        lista_score = [item_score,item_score_dos,item_score_tres]
        
        super().__init__(pantalla, personaje, lista_plataformas, lista_obstaculos, lista_municiones, lista_vidas, lista_enemigos, fondo, tiempo_restante,lista_score,5)
        