import pygame
from Niveles.modo import *
from Niveles.configuraciones import *
from GUI.GUI_form_game_over import *
from GUI.GUI_form_nivel_completado import *
class Nivel:
    def __init__(self, pantalla, personaje_principal, lista_plataformas, lista_obstaculos, lista_municiones, lista_vidas, lista_enemigos, imagen_fondo,tiempo,lista_score,municiones_necesarias):
        self._slave = pantalla
        self.personaje = personaje_principal
        self.plataformas = lista_plataformas
        self.obstaculos = lista_obstaculos
        self.municiones = lista_municiones
        self.municiones_necesarias = municiones_necesarias
        self.vidas = lista_vidas
        self.score = lista_score
        self.enemigos = lista_enemigos
        self.img_fondo = imagen_fondo
        self.fuente = pygame.font.match_font('consolas')
        self.tiempo_restante = tiempo

    def update(self, lista_eventos):
        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    cambiar_modo()
        if(self.personaje.municion < self.municiones_necesarias and self.tiempo_restante == 0) or self.personaje.vida == 0:
            form_gameover = FormGameOver(self._slave, 0, 0, self._slave.get_width(), self._slave.get_height(), True, "PROYECTO PYGAME\Recursos\Interfaz\game_over.png")
            form_gameover.update(lista_eventos)
            form_gameover.show_dialog(form_gameover)
        elif self.personaje.municion == self.municiones_necesarias:
            form_nivel_completado = FormNivelCompletado(self._slave, 0, 0, self._slave.get_width(), self._slave.get_height(), True, "PROYECTO PYGAME\\Recursos\\Interfaz\\nivel_superado.png")
            form_nivel_completado.update(lista_eventos)
            form_nivel_completado.show_dialog(form_nivel_completado)
        else:
            self.leer_inputs()
            self.personaje.verificar_colision_obstaculo(self.obstaculos)
            self.personaje.verificar_colision_enemigo(self.enemigos)
            self.actualizar_pantalla()
            self.dibujar_rectangulos()
        
                    
    def leer_inputs(self):
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_RIGHT]):
            self.personaje.que_hace = "Derecha"
        elif (keys[pygame.K_LEFT]):
            self.personaje.que_hace = "Izquierda"
        elif (keys[pygame.K_UP]) and self.personaje.ultima_accion == "Derecha":
            self.personaje.que_hace = "Salta_Derecha"
        elif (keys[pygame.K_UP]) and self.personaje.ultima_accion == "Izquierda":
            self.personaje.que_hace = "Salta_Izquierda"
        elif self.personaje.ultima_accion == "Derecha":
            self.personaje.que_hace = "Quieto_Derecha"
        elif self.personaje.ultima_accion == "Izquierda":
            self.personaje.que_hace = "Quieto_Izquierda"    


    def dibujar_rectangulos(self):
        if get_mode():
            for lado in self.personaje.lados:
                pygame.draw.rect(self._slave, "Blue", self.personaje.lados[lado], 2)
            for plataforma in self.plataformas:
                for lado in plataforma.lados:
                    pygame.draw.rect(self._slave, "Green", plataforma.lados[lado], 2) 
            for obstaculo in self.obstaculos:         
                for lado in obstaculo.lados:
                    pygame.draw.rect(self._slave, "Orange", obstaculo.lados[lado], 2)
            for enemigo in self.enemigos:
                for lado in enemigo.lados:
                    pygame.draw.rect(self._slave, "Black", enemigo.lados[lado], 2)

    def actualizar_pantalla(self): 
        self._slave.blit(self.img_fondo, (0, 0))
            
        for plataforma in self.plataformas:
            self._slave.blit(plataforma.imagen, (plataforma.lados["main"].x, plataforma.lados["main"].y))
            
        for obstaculo in self.obstaculos:
            self._slave.blit(obstaculo.imagen, (obstaculo.lados["main"].x, obstaculo.lados["main"].y))

        for vida in self.vidas:
            self._slave.blit(vida.imagen, (vida.lados["main"].x, vida.lados["main"].y))
            vida.aplicar_vida(self.personaje)   
            
        for enemigo in self.enemigos:
            enemigo.mover_enemigo(self._slave,self.plataformas,self.enemigos)
            enemigo.verificar_colision_personaje(self.personaje)

        for municion in self.municiones:
            self._slave.blit(municion.imagen, (municion.lados["main"].x, municion.lados["main"].y))
            municion.aplicar_efecto(self.personaje)

        for score in self.score:
            self._slave.blit(score.imagen, (score.lados["main"].x, score.lados["main"].y))
            score.aumentar_score(self.personaje)
            
        self.personaje.update(self._slave, self.plataformas)
        self.personaje.mostrar_vidas(self._slave)
        self.personaje.mostrar_municion(self._slave, self.fuente, str(self.personaje.municion) + "/" + str(len(self.municiones)), "White", 40, 650, 850)
        self.personaje.mostrar_score(self._slave, self.fuente, "SCORE:" + str(self.personaje.score), "White", 40, 1500, 850)
        
        mostrar_cronometro(self._slave, self.fuente,"00:"+str(self.tiempo_restante//20).zfill(2), 1100, 850)

        self.tiempo_restante -= 1
        if self.tiempo_restante <= 0:
            self.tiempo_restante = 0


