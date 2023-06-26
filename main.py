import pygame
import sys
from pygame.locals import *
from configuraciones import *
from Class_personaje import Personaje
from Class_superficie import Superficie
from Class_obstaculo import Obstaculo
from Class_enemigo import Enemigo
from Class_item import Item
from modo import *
from GUI_form_prueba import FormPrueba
from Class_boton import Boton

####salto hacia la izquierda, que mire hacia la izquierda,, generar enemigos aleatorios, plataformas colision por derecha y por debajo, ver el self.colisionado 

def actualizar_pantalla(pantalla, personaje: Personaje, fondo, lista_plataformas, lista_obstaculos, lista_items, lista_enemigos,lista_vidas):
        
        pantalla.blit(fondo, (0, 0))
        
        for plataforma in lista_plataformas:
            pantalla.blit(plataforma.imagen, (plataforma.lados["main"].x, plataforma.lados["main"].y))
        
        for obstaculo in lista_obstaculos:
            pantalla.blit(obstaculo.imagen, (obstaculo.lados["main"].x, obstaculo.lados["main"].y))

        for vida in lista_vidas:
            pantalla.blit(vida.imagen, (vida.lados["main"].x, vida.lados["main"].y))
            vida.aplicar_vida(personaje)   
        
        for enemigo in lista_enemigos:
            enemigo.mover_enemigo(pantalla)

        for item in lista_items:
            pantalla.blit(item.imagen, (item.lados["main"].x, item.lados["main"].y))
            item.aplicar_efecto(personaje)    
        
        personaje.update(pantalla, lista_plataformas)
        personaje.mostrar_vidas(pantalla)
        personaje.mostrar_municion(PANTALLA, consolas, str(personaje.municion) + "/" + str(len(lista_municiones)), "White", 40, 800, 850)

    
       
W, H = 1900, 900
FPS = 18

RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((W,H))

fondo = pygame.image.load("PROYECTO PYGAME\Recursos\Fondo.png")
fondo = pygame.transform.scale(fondo, (W,H))
PANTALLA.blit(fondo,(0,0))

icono = pygame.image.load("PROYECTO PYGAME\\Recursos\\0.png")
pygame.display.set_icon(icono)

consolas = pygame.font.match_font('consolas')

pygame.init()

pygame.mixer.music.load("PROYECTO PYGAME\Recursos\SonidoDeFondo\donkey-kong-country.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

posicion_inicial = (H/2 - 300, 490)
tamaño = (55, 75)

tiempo_total = 30 
tiempo_restante = tiempo_total * 20

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

enemigo = Enemigo((55,55),diccionario_animaciones_enemigo, (H/2, 520),10,W)
enemigo_dos = Enemigo((55,55),diccionario_animaciones_enemigo_dos, (1000, 150),11,W)

municion = Item((30,25), (obstaculo.lados["main"].right + 35 ,plataforma.lados["main"].top - 28),"PROYECTO PYGAME\\Recursos\\Disparo\\23.png")
municion_dos = Item((30,25),(1000, 520),"PROYECTO PYGAME\\Recursos\\Disparo\\23.png")
municion_tres = Item((30,25),(plataforma_dos.lados["main"].right - obstaculo.ancho, plataforma_dos.lados["main"].top - 28),"PROYECTO PYGAME\\Recursos\\Disparo\\23.png")
municion_cuatro = Item((30,25),(plataforma_dos.lados["main"].left + 20, plataforma_dos.lados["main"].top - 28),"PROYECTO PYGAME\\Recursos\\Disparo\\23.png")
municion_cinco = Item((30,25),(1180, 280),"PROYECTO PYGAME\\Recursos\\Disparo\\23.png")
vida = Item((30,25), (obstaculo.lados["main"].right -10 ,plataforma_tres.lados["main"].top - 28),"PROYECTO PYGAME\\Recursos\\Vida\\pngegg.png")

lista_plataformas = [plataforma_piso, plataforma, plataforma_dos, plataforma_tres, plataforma_cuatro]
lista_obstaculos = [obstaculo, obstaculo_dos, obstaculo_tres, obstaculo_cuatro, obstaculo_cinco, obstaculo_seis]
lista_municiones = [municion,municion_dos, municion_tres, municion_cuatro, municion_cinco]
lista_vidas = [vida]
lista_enemigos = [enemigo,enemigo_dos]

form_prueba = FormPrueba(PANTALLA,650,55,500,550,True,"PROYECTO PYGAME\Recursos\Interfaz\pngegg.png")

boton = Boton("PROYECTO PYGAME\\Recursos\\Interfaz\\6.png", (PANTALLA.get_width() - 10, PANTALLA.get_height() - 10))
mostrar_formulario = False
juego_pausado = False

while True:
    RELOJ.tick(FPS)
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()

    keys = pygame.key.get_pressed()

    if(keys[pygame.K_RIGHT]):
        personaje.que_hace = "Derecha"
    elif (keys[pygame.K_LEFT]):
        personaje.que_hace = "Izquierda"
    elif (keys[pygame.K_UP]):
        personaje.que_hace = "Salta"        
    else:
        personaje.que_hace = "Quieto"
    
    if boton.verificar_clic(evento):
        mostrar_formulario = True
        juego_pausado = True

    if mostrar_formulario:
        form_prueba.update(eventos)
        boton.imagen =  pygame.image.load("PROYECTO PYGAME\\Recursos\\Interfaz\\0.png")

    if not juego_pausado:
        personaje.verificar_colision_obstaculo(lista_obstaculos)
        personaje.verificar_colision_enemigo(lista_enemigos)

        actualizar_pantalla(PANTALLA, personaje, fondo, lista_plataformas,lista_obstaculos,lista_municiones,lista_enemigos,lista_vidas)
        mostrar_cronometro(PANTALLA, consolas,"00:"+str(tiempo_restante//20).zfill(2), 1200, 850)

        tiempo_restante -= 1
        if tiempo_restante <= 0:
            tiempo_restante = 0
            personaje.vida = 0      
    
    boton.dibujar(PANTALLA) 

    if get_mode():
        for lado in personaje.lados:
            pygame.draw.rect(PANTALLA, "Blue", personaje.lados[lado], 2)
        for lado in plataforma_piso.lados:
            pygame.draw.rect(PANTALLA, "Green", plataforma_piso.lados[lado], 2) 
        for lado in plataforma.lados:
            pygame.draw.rect(PANTALLA, "Yellow", plataforma.lados[lado], 2) 
        for lado in obstaculo.lados:
            pygame.draw.rect(PANTALLA, "Orange", obstaculo.lados[lado], 2)
        for lado in enemigo_dos.lados:
            pygame.draw.rect(PANTALLA, "Black", enemigo_dos.lados[lado], 2)                    

    pygame.display.update() 