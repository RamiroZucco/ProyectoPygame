import pygame
from Niveles.nivel import Nivel
from Niveles.Class_personaje import Personaje
from Niveles.Class_superficie import Superficie
from Niveles.Class_enemigo import Enemigo
from Niveles.Class_item import Item
from Niveles.configuraciones import *
from Niveles.Class_Boss import Boss


class NivelDos(Nivel):
    def __init__(self, pantalla: pygame.Surface):
        W = pantalla.get_width()
        H = pantalla.get_height()

        fondo = pygame.image.load("PROYECTO PYGAME copy\Recursos\Fondos_Imagenes\—Pngtree—business city blue technology city_1320031.jpg")
        fondo = pygame.transform.scale(fondo, (W,H))

        posicion_inicial = (H/2 - 300, 690)
        tamaño = (55, 75)

        tiempo_total = 25
        tiempo_restante = tiempo_total * 20

        diccionario_animaciones = {}
        diccionario_animaciones["Quieto_Izquierda"] = personaje_quieto_izquierda
        diccionario_animaciones["Quieto_Derecha"] = personaje_quieto_derecha
        diccionario_animaciones["Salta_Izquierda"] = personaje_salta_izquierda
        diccionario_animaciones["Salta_Derecha"] = personaje_salta_derecha
        diccionario_animaciones["Izquierda"] = personaje_camina_izquierda
        diccionario_animaciones["Derecha"] = personaje_camina_derecha
        diccionario_animaciones["Dañado"] = personaje_dañado
        diccionario_animaciones["Dispara_Izquierda"] = personaje_dispara_izquierda
        diccionario_animaciones["Dispara_Derecha"] = personaje_dispara_derecha

        diccionario_animaciones_enemigo = {}
        diccionario_animaciones_enemigo["Derecha"] = araña_derecha
        diccionario_animaciones_enemigo["Izquierda"] = araña_izquierda

        diccionario_animaciones_enemigo_dos = {}
        diccionario_animaciones_enemigo_dos["Izquierda"] = pez_volador_izquierda
        diccionario_animaciones_enemigo_dos["Derecha"] = pez_volador_derecha

        diccionario_animaciones_boss = {}
        diccionario_animaciones_boss["Quieto_Izquierda"] = boss_quieto_izquierda
        diccionario_animaciones_boss["Quieto_Derecha"] = boss_quieto_derecha
        diccionario_animaciones_boss["Salta_Izquierda"] = boss_salta_izquierada
        diccionario_animaciones_boss["Salta_Derecha"] = boss_salta_derecha
        diccionario_animaciones_boss["Izquierda"] = boss_camina_izquierda
        diccionario_animaciones_boss["Derecha"] = boss_camina_derecha
        diccionario_animaciones_boss["Dañado"] = boss_dañado
        diccionario_animaciones_boss["Dispara_Izquierda"] = boss_dispara_izquierda
        diccionario_animaciones_boss["Dispara_Derecha"] = boss_dispara_derecha
        diccionario_animaciones_boss["Muerto"] = boss_muerto

        personaje = Personaje(tamaño,diccionario_animaciones,posicion_inicial,12,W,3)

        plataforma_piso = Superficie((W, 20), (0, personaje.lados["main"].bottom),"PROYECTO PYGAME copy\Recursos\Superficie\pngwing.com (1).png")
        plataforma = Superficie((95,95),(500,680),"PROYECTO PYGAME copy\Recursos\Superficie\piedra1.png")
        plataforma_dos = Superficie((200,55),(830,490),"PROYECTO PYGAME copy\\Recursos\\Superficie\\base (1).png")
        plataforma_tres = Superficie((200,55),(610,580),"PROYECTO PYGAME copy\\Recursos\\Superficie\\base (1).png")
        plataforma_cuatro = Superficie((200,55),(1080,420),"PROYECTO PYGAME copy\\Recursos\\Superficie\\base (1).png")
        plataforma_cinco = Superficie((200,55),(200,580),"PROYECTO PYGAME copy\\Recursos\\Superficie\\base (1).png")
        plataforma_seis = Superficie((200,55),(1280,300),"PROYECTO PYGAME copy\\Recursos\\Superficie\\base (1).png")
        plataforma_ocho = Superficie((200,55),(100,470),"PROYECTO PYGAME copy\\Recursos\\Superficie\\base (1).png")
        plataforma_nueve = Superficie((200,55),(1680,300),"PROYECTO PYGAME copy\\Recursos\\Superficie\\base (1).png")

        enemigo = Enemigo((55,55),diccionario_animaciones_enemigo, (1700, 710),10,W)
        enemigo_dos = Enemigo((55,55),diccionario_animaciones_enemigo_dos, (1800, 360),11,W)
        enemigo_tres = Enemigo((55,55),diccionario_animaciones_enemigo, (1000, 710),11,W)
        enemigo_cuatro = Enemigo((55,55),diccionario_animaciones_enemigo_dos, (200, 235),11,W)

        municion = Item((30,25), (plataforma_cuatro.lados["main"].centerx - 15, plataforma_cuatro.lados["main"].y - 30),"PROYECTO PYGAME copy\\Recursos\\Disparo\\23.png")
        municion_dos = Item((30,25),(1000, 695),"PROYECTO PYGAME copy\\Recursos\\Disparo\\23.png")
        municion_tres = Item((30,25),(1700,695),"PROYECTO PYGAME copy\\Recursos\\Disparo\\23.png")
        municion_cuatro = Item((30,25),(plataforma_nueve.lados["main"].centerx - 15, plataforma_nueve.lados["main"].y - 30),"PROYECTO PYGAME copy\\Recursos\\Disparo\\23.png")
        municion_cinco = Item((30,25),(plataforma_seis.lados["main"].centerx - 15, plataforma_seis.lados["main"].y - 30),"PROYECTO PYGAME copy\\Recursos\\Disparo\\23.png")
        municion_seis = Item((30,25),(plataforma_cinco.lados["main"].centerx - 15, plataforma_cinco.lados["main"].y - 30),"PROYECTO PYGAME copy\\Recursos\\Disparo\\23.png")
        vida = Item((30, 25), (plataforma.lados["main"].centerx - 15, plataforma.lados["main"].y - 30), "PROYECTO PYGAME copy\\Recursos\\Vida\\pngegg.png")
        item_score = Item((30,25),(plataforma_ocho.lados["main"].centerx - 15, plataforma_ocho.lados["main"].y - 30),"PROYECTO PYGAME copy\\Recursos\\Score\\0.png")
        item_score_dos = Item((30,25),(1550,520),"PROYECTO PYGAME copy\\Recursos\\Score\\0.png")
        item_score_tres = Item((30,25),(plataforma_dos.lados["main"].centerx - 15, plataforma_dos.lados["main"].y - 30),"PROYECTO PYGAME copy\\Recursos\\Score\\0.png")

        lista_plataformas = [plataforma_piso, plataforma, plataforma_dos, plataforma_tres, plataforma_cuatro,plataforma_cinco, plataforma_seis,plataforma_ocho,plataforma_nueve]
        lista_obstaculos = []
        lista_municiones = [municion,municion_dos, municion_tres, municion_cuatro, municion_cinco, municion_seis]
        lista_vidas = [vida]
        lista_enemigos = [enemigo,enemigo_dos,enemigo_tres,enemigo_cuatro]
        lista_score = [item_score,item_score_dos,item_score_tres]
        boss = Boss((95,95),diccionario_animaciones_boss,(3000,3000),12,W,7)
        
        super().__init__(pantalla, personaje, lista_plataformas, lista_obstaculos, lista_municiones, lista_vidas, lista_enemigos, fondo, tiempo_restante,lista_score,6,boss)
