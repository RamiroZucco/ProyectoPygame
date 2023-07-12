from Niveles.configuraciones import *
from Niveles.Class_proyectil import Proyectil
import time

class Personaje:
    def __init__(self, tamaño, animaciones, posicion_inicial,velocidad, limite_x,vida):
        self.ancho = tamaño[0]
        self.alto = tamaño[1]

        self.gravedad = 1
        self.potencia_salto = -15
        self.limite_velocidad_caida = 15
        self.esta_saltando = False

        self.contador_pasos = 0
        self.que_hace = "Quieto_Derecha"
        self.animaciones = animaciones
        self.reescalar_animaciones()
        
        rectangulo = self.animaciones["Derecha"][0].get_rect()
        rectangulo.x = posicion_inicial[0]
        rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulos(rectangulo)
        self.velocidad = velocidad
        self.desplazamiento_y = 0
        self.limite_x = limite_x

        self.score = 0
        self.municion = 0 

        self.vida = vida
        self.imagen_vida = pygame.image.load("PROYECTO PYGAME copy\\Recursos\\Vida\\pngegg.png")
        self.imagen_vida = pygame.transform.scale(self.imagen_vida, (50, 50))
        self.posicion_vidas = (100, 830)

        self.sonido_colision = pygame.mixer.Sound("PROYECTO PYGAME copy\\Recursos\\SonidoPerderVida\\27425__hello_flowers__nu_glch_mplez_4i.wav")
        self.sonido_colision.set_volume(0.5)

        self.sonido_disparo = pygame.mixer.Sound("PROYECTO PYGAME copy\\Recursos\\SonidoDisparo\\270542__littlerobotsoundfactory__laser_02.wav")
        self.sonido_disparo.set_volume(0.1)

        self.ultima_accion = "Derecha"

        self.proyectiles = []
        self.tiempo_ultimo_disparo = 0
        self.intervalo_disparo = 1 

    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave],self.ancho,self.alto)

    def aplicar_gravedad(self, pantalla, lista_plataformas):
        if self.esta_saltando:
            if self.ultima_accion == "Derecha":
                self.animar(pantalla, "Salta_Derecha")
            else:
                self.animar(pantalla, "Salta_Izquierda")    
            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y = self.desplazamiento_y + self.gravedad                  
        for plataforma in lista_plataformas:
            if self.lados["bottom"].colliderect(plataforma.lados["top"]):
                self.esta_saltando = False
                self.desplazamiento_y = 0
                self.lados["main"].bottom = plataforma.lados["main"].top + 5
                break
            else:
                self.esta_saltando = True        

    def mover(self, velocidad,W):
        nueva_posicion_x = self.lados["main"].x + velocidad
        if nueva_posicion_x < 0:
            nueva_posicion_x = 0
        elif nueva_posicion_x > W - self.ancho:
            nueva_posicion_x = W - self.ancho
        for lado in self.lados:
            self.lados[lado].x = nueva_posicion_x

    def animar(self, pantalla, que_animacion:str):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
        self.contador_pasos += 1
    
    def update(self, pantalla, piso):
        if self.que_hace == "Derecha":
            if not self.esta_saltando:
                self.animar(pantalla,"Derecha")
            self.mover(self.velocidad, self.limite_x)
            self.ultima_accion = "Derecha"
        elif self.que_hace == "Izquierda":
            if not self.esta_saltando:
                self.animar(pantalla,"Izquierda")
            self.mover(self.velocidad *-1, self.limite_x)
            self.ultima_accion = "Izquierda"
        elif self.que_hace == "Salta_Derecha":
            if not self.esta_saltando:
                self.animar(pantalla,"Salta_Derecha")
                self.esta_saltando = True
                self.desplazamiento_y = self.potencia_salto
        elif self.que_hace == "Salta_Izquierda":
            if not self.esta_saltando:
                self.animar(pantalla,"Salta_Izquierda")
                self.esta_saltando = True
                self.desplazamiento_y = self.potencia_salto        
        elif self.que_hace == "Quieto_Derecha":
            if not self.esta_saltando:
                self.animar(pantalla, "Quieto_Derecha")
        elif self.que_hace == "Quieto_Izquierda":
            if not self.esta_saltando:
                self.animar(pantalla, "Quieto_Izquierda")
        elif self.que_hace == "Dañado":
            self.sonido_colision.play()
            if not self.esta_saltando:
                self.animar(pantalla, "Dañado")
        elif self.que_hace == "Dispara_Izquierda":
            if not self.esta_saltando:
                self.animar(pantalla, "Dispara_Izquierda")
        elif self.que_hace == "Dispara_Derecha":
            if not self.esta_saltando:
                self.animar(pantalla, "Dispara_Derecha")                 
        self.aplicar_gravedad(pantalla,piso)
    
    def verificar_colision_obstaculo(self, lista_obstaculos):
        for obstaculo in lista_obstaculos:
            if self.lados["main"].colliderect(obstaculo.lados["main"]):
                self.que_hace = "Dañado"
                self.mover(self.velocidad, 200)
                self.vida -= 1
                

    def verificar_colision_enemigo(self, lista_enemigos):
        for enemigo in lista_enemigos:
            if self.lados["main"].colliderect(enemigo.lados["main"]):
                self.que_hace = "Dañado"
                self.mover(self.velocidad, 200)
                self.vida -= 1
                
    
    def verificar_colision_boss(self, boss):
        if self.lados["main"].colliderect(boss.lados["main"]):
            if boss.que_hace == "Muerto":
                self.municion += 1
                self.score += 300 
            else:
                self.que_hace = "Dañado"
                self.mover(self.velocidad, 200)
                self.vida -= 2
                             

    def mostrar_vidas(self, pantalla):
        for i in range(self.vida):
            x = self.posicion_vidas[0] + i * (self.imagen_vida.get_width() + 5)
            y = self.posicion_vidas[1]
            pantalla.blit(self.imagen_vida, (x, y))

    def mostrar_municion(self, pantalla, fuente, texto, color, tamaño, x, y):
        tipo_letra = pygame.font.Font(fuente, tamaño)
        superficie_texto = tipo_letra.render(texto, True, color)
        rectangulo_texto = superficie_texto.get_rect()
        rectangulo_texto.left = x
        rectangulo_texto.centery = y

        imagen_municion = pygame.image.load("PROYECTO PYGAME copy\\Recursos\\Disparo\\23.png")
        imagen_municion = pygame.transform.scale(imagen_municion, (30, 30))
        rectangulo_imagen = imagen_municion.get_rect()
        rectangulo_imagen.left = rectangulo_texto.right + 10
        rectangulo_imagen.centery = rectangulo_texto.centery

        pantalla.blit(superficie_texto, rectangulo_texto)
        pantalla.blit(imagen_municion, rectangulo_imagen)

    def mostrar_score(self, pantalla, fuente, texto, color, tamaño, x, y):
        tipo_letra = pygame.font.Font(fuente, tamaño)
        superficie_texto = tipo_letra.render(texto, True, color)
        rectangulo_texto = superficie_texto.get_rect()
        rectangulo_texto.left = x
        rectangulo_texto.centery = y
        pantalla.blit(superficie_texto, rectangulo_texto)
    
    def lanzar_proyectil(self, lista_plataformas,pantalla, personaje, boss):
        diccionario_proyectil = {}
        diccionario_proyectil["Izquierda"] = proyectil_cientifico_izquierda
        diccionario_proyectil["Derecha"] = proyectil_cientifico_derecha    
        if self.que_hace == "Dispara_Derecha":
            tiempo_actual = time.time()
            if tiempo_actual - self.tiempo_ultimo_disparo >= self.intervalo_disparo:
                posicion_inicial = (self.lados["main"].right, self.lados["main"].centery-30)
                proyectil = Proyectil((30, 20), posicion_inicial, 12, self.limite_x,diccionario_proyectil,"Derecha")
                self.proyectiles.append(proyectil)
                self.sonido_disparo.play()
                self.tiempo_ultimo_disparo = tiempo_actual
        elif self.que_hace == "Dispara_Izquierda":
            tiempo_actual = time.time()
            if tiempo_actual - self.tiempo_ultimo_disparo >= self.intervalo_disparo:
                posicion_inicial = (self.lados["main"].left-25, self.lados["main"].centery-30)
                proyectil = Proyectil((30, 20), posicion_inicial, 12, self.limite_x,diccionario_proyectil,"Izquierda")
                self.proyectiles.append(proyectil)
                self.sonido_disparo.play()
                self.tiempo_ultimo_disparo = tiempo_actual 
        for proyectil in self.proyectiles:
            proyectil.mover_proyectil(lista_plataformas,pantalla,personaje,boss)
            
                



                   
                
              
    
