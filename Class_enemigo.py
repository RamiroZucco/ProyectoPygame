from configuraciones import *
class Enemigo:
    def __init__(self, tamaño, animaciones, posicion_inicial,velocidad, limite_x):
        self.ancho = tamaño[0]
        self.alto = tamaño[1]

        self.contador_pasos = 0
        self.que_hace = "Derecha"
        self.animaciones = animaciones
        self.reescalar_animaciones()

        rectangulo = self.animaciones["Derecha"][0].get_rect()
        rectangulo.x = posicion_inicial[0]
        rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulos(rectangulo)
        self.velocidad = velocidad
        self.desplazamiento_y = 0
        self.limite_x = limite_x

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

    def cambiar_direccion(self):
        if self.velocidad > 0:
            self.que_hace = "Derecha"
        else:
            self.que_hace = "Izquierda"

    def mover_enemigo(self, pantalla):
        self.animar(pantalla, self.que_hace)
        self.lados["main"].x += self.velocidad

        if self.lados["main"].x < 0 or self.lados["main"].x > self.limite_x:
            self.velocidad *= -1
            self.cambiar_direccion()

        if self.lados["main"].x < 0:
            self.lados["main"].x = 0
            self.cambiar_direccion()
        elif self.lados["main"].x > self.limite_x:
            self.lados["main"].x = self.limite_x
            self.cambiar_direccion()

        for lado in self.lados:
            if lado != "main":
                self.lados[lado].x = self.lados["main"].x    



