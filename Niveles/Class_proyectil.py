from Niveles.configuraciones import *
import random 

class Proyectil:
    def __init__(self, tamaño, posicion_inicial, velocidad, limite, animaciones,direccion):
        self.ancho = tamaño[0]
        self.alto = tamaño[1]

        self.contador_pasos = 0
        self.que_hace = direccion
        self.animaciones = animaciones
        self.reescalar_animaciones()

        rectangulo = self.animaciones["Derecha"][0].get_rect()
        rectangulo.x = posicion_inicial[0]
        rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulos(rectangulo)

        self.velocidad = velocidad
        self.limite_x = limite

    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave],self.ancho,self.alto)

    def animar(self, pantalla, que_animacion: str):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
        self.contador_pasos += 1
    
    def mover_proyectil(self,lista_plataformas,pantalla, personaje,boss):
        if self.que_hace == "Derecha":
            self.lados["main"].x += self.velocidad
            self.animar(pantalla,"Derecha")
        elif self.que_hace == "Izquierda":
            self.lados["main"].x -= self.velocidad
            self.animar(pantalla,"Izquierda")        
        if self.lados["main"].x < 0 or self.lados["main"].x > self.limite_x:
            self.desaparecer_municion()
        if self.lados["main"].x < 0:
            self.desaparecer_municion()
        elif self.lados["main"].x > self.limite_x:
            self.desaparecer_municion()
        for lado in self.lados:
            if lado != "main":
                self.lados[lado].x = self.lados["main"].x
        for plataforma in lista_plataformas:
            if self.lados["main"].colliderect(plataforma.lados["main"]):
                self.desaparecer_municion() 
        if self.lados["main"].colliderect(personaje.lados["main"]):
            personaje.que_hace = "Dañado"
            personaje.sonido_colision.play()
            personaje.vida -= 1
            self.desaparecer_municion()
        if self.lados["main"].colliderect(boss.lados["main"]):
            boss.que_hace = "Dañado"
            boss.vida -= 1
            self.desaparecer_municion()    


    def desaparecer_municion(self):
        self.lados["main"].x = random.randrange(0,4440,60)
        self.lados["main"].y = random.randrange(-1000, 0, 60)            