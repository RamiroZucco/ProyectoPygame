import pygame
from Niveles.nivel import Nivel
from Niveles.Class_personaje import Personaje
from Niveles.Class_superficie import Superficie
from Niveles.Class_enemigo import Enemigo
from Niveles.Class_item import Item
from Niveles.configuraciones import *

class NivelTres(Nivel):
    def __init__(self, pantalla: pygame.Surface):
        W = pantalla.get_width()
        H = pantalla.get_height()

        fondo = pygame.image.load("PROYECTO PYGAME\\Recursos\\Fondos_Imagenes\\1.png")
        fondo = pygame.transform.scale(fondo, (W,H))

        posicion_inicial = (H/2 - 300, 680)
        tamaño = (55, 75)

        tiempo_total = 30000
        tiempo_restante = tiempo_total * 20
        fuente = pygame.font.match_font('consolas')

        diccionario_animaciones = {}
        diccionario_animaciones["Quieto_Izquierda"] = personaje_quieto_izquierda
        diccionario_animaciones["Quieto_Derecha"] = personaje_quieto_derecha
        diccionario_animaciones["Salta_Izquierda"] = personaje_salta_izquierda
        diccionario_animaciones["Salta_Derecha"] = personaje_salta_derecha
        diccionario_animaciones["Izquierda"] = personaje_camina_izquierda
        diccionario_animaciones["Derecha"] = personaje_camina_derecha
        diccionario_animaciones["Dañado"] = personaje_dañado

        diccionario_animaciones_enemigo = {}
        diccionario_animaciones_enemigo["Derecha"] = mono_derecha
        diccionario_animaciones_enemigo["Izquierda"] = mono_izquierda

        diccionario_animaciones_enemigo_dos = {}
        diccionario_animaciones_enemigo_dos["Izquierda"] = mosquito_izquierda
        diccionario_animaciones_enemigo_dos["Derecha"] = mosquito_derecha

        personaje = Personaje(tamaño,diccionario_animaciones,posicion_inicial,12,W,3)

        plataforma_piso = Superficie((W, 20), (0, personaje.lados["main"].bottom),"PROYECTO PYGAME\Recursos\Superficie\pngwing.com (1).png")
        plataforma = Superficie((125,40),(500,680),"PROYECTO PYGAME\\Recursos\\Superficie\\base (2).png")
        plataforma_dos = Superficie((125,40),(1200,680),"PROYECTO PYGAME\\Recursos\\Superficie\\base (2).png")
        plataforma_tres = Superficie((125,40),(610,580),"PROYECTO PYGAME\\Recursos\\Superficie\\base (2).png")
        plataforma_cuatro = Superficie((125,40),(1080,420),"PROYECTO PYGAME\\Recursos\\Superficie\\base (2).png")
        plataforma_cinco = Superficie((125,40),(200,580),"PROYECTO PYGAME\\Recursos\\Superficie\\base (2).png")
        plataforma_seis = Superficie((125,40),(1280,300),"PROYECTO PYGAME\\Recursos\\Superficie\\base (2).png")
        plataforma_ocho = Superficie((125,40),(100,470),"PROYECTO PYGAME\\Recursos\\Superficie\\base (2).png")
        plataforma_nueve = Superficie((125,40),(1680,300),"PROYECTO PYGAME\\Recursos\\Superficie\\base (2).png")

        enemigo_dos = Enemigo((55,55),diccionario_animaciones_enemigo_dos, (1800, 360),11,W)
        enemigo_tres = Enemigo((65,75),diccionario_animaciones_enemigo, (1000, 680),11,W)
        enemigo_cuatro = Enemigo((55,55),diccionario_animaciones_enemigo_dos, (200, 235),11,W)

        municion = Item((30,25), (3000,3000),"PROYECTO PYGAME\\Recursos\\Disparo\\23.png")
        vida = Item((30, 25), (plataforma.lados["main"].centerx - 15, plataforma.lados["main"].y - 30), "PROYECTO PYGAME\\Recursos\\Vida\\pngegg.png")
        item_score = Item((30,25),(plataforma_ocho.lados["main"].centerx - 15, plataforma_ocho.lados["main"].y - 30),"PROYECTO PYGAME\\Recursos\\Score\\0.png")
        item_score_dos = Item((30,25),(1550,520),"PROYECTO PYGAME\\Recursos\\Score\\0.png")
        item_score_tres = Item((30,25),(plataforma_dos.lados["main"].centerx - 15, plataforma_dos.lados["main"].y - 30),"PROYECTO PYGAME\\Recursos\\Score\\0.png")

        lista_plataformas = [plataforma_piso, plataforma, plataforma_dos, plataforma_tres, plataforma_cuatro,plataforma_cinco, plataforma_seis,plataforma_ocho,plataforma_nueve]
        lista_obstaculos = []
        lista_municiones = [municion]
        lista_vidas = [vida]
        lista_enemigos = [enemigo_dos,enemigo_tres,enemigo_cuatro]
        lista_score = [item_score,item_score_dos,item_score_tres]
        
        super().__init__(pantalla, personaje, lista_plataformas, lista_obstaculos, lista_municiones, lista_vidas, lista_enemigos, fondo, tiempo_restante,lista_score,1)
