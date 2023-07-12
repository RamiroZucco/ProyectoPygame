from Niveles.Class_personaje import Personaje
from Niveles.configuraciones import *
from Niveles.Class_proyectil import Proyectil
import time
import random
class Boss(Personaje):
    def __init__(self, tamaño, animaciones, posicion_inicial, velocidad, limite_x,vida):
        super().__init__(tamaño, animaciones, posicion_inicial, velocidad, limite_x,vida)
        self.que_hace = "Quieto_Izquierda"
        self.tiempo_inicio_movimiento = 0
        self.duracion_movimiento = 1
        self.salto_realizado = False
        self.tiempo_inicio_disparo = 0
        self.disparo_iniciado = False
        self.se_movio = False

    def realizar_comportamiento(self,lista_municiones):
        if self.vida > 0:
            tiempo_actual = time.time()
            if self.tiempo_inicio_movimiento == 0:
                self.tiempo_inicio_movimiento = tiempo_actual
            if tiempo_actual - self.tiempo_inicio_movimiento <= self.duracion_movimiento:
                self.que_hace = "Izquierda"
            else:
                self.que_hace = "Quieto_Izquierda"
                if not self.salto_realizado:
                    self.tiempo_inicio_salto = tiempo_actual
                if tiempo_actual - self.tiempo_inicio_salto <= 0.2:
                    self.que_hace = "Salta_Izquierda"
                    self.salto_realizado = True
                elif not self.disparo_iniciado:
                    self.tiempo_inicio_disparo = tiempo_actual
                    self.disparo_iniciado = True
                elif tiempo_actual - self.tiempo_inicio_disparo <= 5.0:
                    self.que_hace = "Dispara_Izquierda"
                elif tiempo_actual - self.tiempo_inicio_salto <= 6.2 and self.salto_realizado == True:
                    self.que_hace = "Salta_Derecha"
                    self.mover(11, self.limite_x)
                elif tiempo_actual - self.tiempo_inicio_salto <= 6.7 and self.salto_realizado == True:
                    self.que_hace = "Salta_Izquierda"
                    self.mover(-19, self.limite_x)    
                elif tiempo_actual - self.tiempo_inicio_disparo <= 15.0:
                    self.que_hace = "Dispara_Izquierda"
                elif tiempo_actual - self.tiempo_inicio_salto <= 16.3 and self.salto_realizado == True:
                    self.que_hace = "Salta_Derecha"
                    self.mover(10, self.limite_x)
                elif tiempo_actual - self.tiempo_inicio_salto <= 16.8 and self.salto_realizado == True:
                    self.que_hace = "Salta_Izquierda"
                    self.mover(-19, self.limite_x)
                elif tiempo_actual - self.tiempo_inicio_disparo <= 22.0:
                    self.que_hace = "Dispara_Izquierda"
                elif tiempo_actual - self.tiempo_inicio_disparo <= 25.0:
                    self.que_hace = "Quieto_Izquierda"
                elif tiempo_actual - self.tiempo_inicio_disparo <= 30.0:
                    self.que_hace = "Dispara_Izquierda"
                elif tiempo_actual - self.tiempo_inicio_disparo <= 35.0:
                    self.que_hace = "Quieto_Izquierda"
                elif tiempo_actual - self.tiempo_inicio_disparo <= 49.0:
                    self.que_hace = "Dispara_Izquierda"
        else:
            self.que_hace = "Muerto"
            if self.que_hace == "Muerto" and self.se_movio == False:
                self.mover_municion(lista_municiones)
                self.se_movio == True
            else:
                self.desaparecer_boss()                                                

    def lanzar_proyectil(self, lista_plataformas, pantalla, personaje, boss):
        diccionario_proyectil = {}
        diccionario_proyectil["Izquierda"] = proyectil_boss_izquierda
        diccionario_proyectil["Derecha"] = proyectil_boss_derecha   
        if self.que_hace == "Dispara_Derecha":
            tiempo_actual = time.time()
            if tiempo_actual - self.tiempo_ultimo_disparo >= self.intervalo_disparo:
                posicion_inicial = (self.lados["main"].right+25, self.lados["main"].centery-20)
                proyectil = Proyectil((30, 20), posicion_inicial, 12, self.limite_x,diccionario_proyectil,"Derecha")
                self.proyectiles.append(proyectil)
                self.tiempo_ultimo_disparo = tiempo_actual
        elif self.que_hace == "Dispara_Izquierda":
            tiempo_actual = time.time()
            if tiempo_actual - self.tiempo_ultimo_disparo >= self.intervalo_disparo:
                posicion_inicial = (self.lados["main"].left-25, self.lados["main"].centery-20)
                proyectil = Proyectil((30, 20), posicion_inicial, 12, self.limite_x,diccionario_proyectil,"Izquierda")
                self.proyectiles.append(proyectil)
                self.tiempo_ultimo_disparo = tiempo_actual      
        for proyectil in self.proyectiles:
            proyectil.mover_proyectil(lista_plataformas,pantalla, personaje,boss)
    
    def desaparecer_boss(self):
        self.lados["main"].x = random.randrange(0,740,60)
        self.lados["main"].y = random.randrange(-1000, 0, 60)

    def mover_municion(self,lista_municiones):
        for municion in lista_municiones:
            municion.lados["main"].x = self.lados["main"].x
            municion.lados["main"].y = self.lados["main"].y

