import pygame
from Niveles.nivel import Nivel
from Niveles.Class_personaje import Personaje
from Niveles.Class_superficie import Superficie
from Niveles.Class_enemigo import Enemigo
from Niveles.Class_item import Item
from Niveles.configuraciones import *
from Niveles.Class_Boss import Boss

class NivelTres(Nivel):
    def __init__(self, pantalla: pygame.Surface):
        W = pantalla.get_width()
        H = pantalla.get_height()
        
        fondo = pygame.image.load("PROYECTO PYGAME copy\\Recursos\\Fondos_Imagenes\\1.png")
        fondo = pygame.transform.scale(fondo, (W,H))

        posicion_inicial = (H/2 - 300, 680)
        tamaño = (55, 75)   
        
        tiempo_total = 50
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

        diccionario_animaciones_enemigo = {}
        diccionario_animaciones_enemigo["Derecha"] = mono_derecha
        diccionario_animaciones_enemigo["Izquierda"] = mono_izquierda
        
        diccionario_animaciones_enemigo_enojado = {}
        diccionario_animaciones_enemigo_enojado["Derecha"] = mono_enojado
        diccionario_animaciones_enemigo_enojado["Izquierda"] = mono_enojado
        

        diccionario_animaciones_enemigo_dos = {}
        diccionario_animaciones_enemigo_dos["Izquierda"] = mosquito_izquierda
        diccionario_animaciones_enemigo_dos["Derecha"] = mosquito_derecha

        personaje = Personaje(tamaño,diccionario_animaciones,posicion_inicial,12,W,3)
        boss = Boss((95,95),diccionario_animaciones_boss,(1500,620),12,W,7) 

        plataforma_piso = Superficie((W, 20), (0, personaje.lados["main"].bottom),"PROYECTO PYGAME copy\Recursos\Superficie\pngwing.com (1).png")
        plataforma = Superficie((185,45),(500,680),"PROYECTO PYGAME copy\\Recursos\\Superficie\\base (2).png") 
        plataforma_dos = Superficie((185,45),(1200,680),"PROYECTO PYGAME copy\\Recursos\\Superficie\\base (2).png") 
        plataforma_tres = Superficie((185,45),(500,480),"PROYECTO PYGAME copy\\Recursos\\Superficie\\base (2).png") 
        plataforma_cuatro = Superficie((185,45),(1500,580),"PROYECTO PYGAME copy\\Recursos\\Superficie\\base (2).png") 
        plataforma_cinco = Superficie((185,45),(200,580),"PROYECTO PYGAME copy\\Recursos\\Superficie\\base (2).png") 
        plataforma_seis = Superficie((185,45),(1500,380),"PROYECTO PYGAME copy\\Recursos\\Superficie\\base (2).png") 
        plataforma_ocho = Superficie((185,45),(200,380),"PROYECTO PYGAME copy\\Recursos\\Superficie\\base (2).png") 
        plataforma_nueve = Superficie((185,45),(1200,480),"PROYECTO PYGAME copy\\Recursos\\Superficie\\base (2).png")
        plataforma_diez = Superficie((185,45),(1200,280),"PROYECTO PYGAME copy\\Recursos\\Superficie\\base (2).png")
        plataforma_once = Superficie((185,45),(1500,180),"PROYECTO PYGAME copy\\Recursos\\Superficie\\base (2).png")
        plataforma_doce = Superficie((185,45),(200,180),"PROYECTO PYGAME copy\\Recursos\\Superficie\\base (2).png")
        plataforma_trece = Superficie((185,45),(500,280),"PROYECTO PYGAME copy\\Recursos\\Superficie\\base (2).png")
        plataforma_catorce = Superficie((185,45),(850,360),"PROYECTO PYGAME copy\\Recursos\\Superficie\\base (2).png")   
        
        item_score = Item((30,25),(plataforma_doce.lados["main"].centerx - 15, plataforma_doce.lados["main"].y - 30),"PROYECTO PYGAME copy\\Recursos\\Score\\0.png")
        municion = Item((30,25), (3000,3000),"PROYECTO PYGAME copy\\Recursos\\Disparo\\23.png")
        vida = Item((30, 25), (plataforma_catorce.lados["main"].centerx-10, 680), "PROYECTO PYGAME copy\\Recursos\\Vida\\pngegg.png")
        item_score_dos = Item((30,25),(plataforma_catorce.lados["main"].centerx-20,180),"PROYECTO PYGAME copy\\Recursos\\Score\\0.png")
        item_score_tres = Item((30,25),(plataforma_once.lados["main"].centerx - 15, plataforma_once.lados["main"].y - 30),"PROYECTO PYGAME copy\\Recursos\\Score\\0.png")
        
        enemigo_dos = Enemigo((55,55),diccionario_animaciones_enemigo_dos, (1800, 425),11,W)
        enemigo_tres = Enemigo((65,75),diccionario_animaciones_enemigo, (1000, 680),7,W)
        enemigo_cuatro = Enemigo((55,55),diccionario_animaciones_enemigo_dos, (200, 225),11,W)
        enemigo_cinco = Enemigo((55,55),diccionario_animaciones_enemigo_dos, (800, 125),11,W)
        enemigo_seis = Enemigo((85,80),diccionario_animaciones_enemigo_enojado,(plataforma_catorce.lados["main"].centerx - 40, plataforma_catorce.lados["main"].y - 65),0,W)

        lista_plataformas = [plataforma_piso, plataforma, plataforma_dos, plataforma_tres, plataforma_cuatro,plataforma_cinco, plataforma_seis,plataforma_ocho,plataforma_nueve,plataforma_diez, plataforma_once, plataforma_doce, plataforma_trece,plataforma_catorce]
        lista_obstaculos = []
        lista_municiones = [municion]
        lista_vidas = [vida]
        lista_enemigos = [enemigo_dos,enemigo_tres,enemigo_cuatro,enemigo_cinco,enemigo_seis]
        lista_score = [item_score,item_score_dos,item_score_tres]
        
        super().__init__(pantalla, personaje, lista_plataformas, lista_obstaculos, lista_municiones, lista_vidas, lista_enemigos, fondo, tiempo_restante,lista_score,1,boss)
