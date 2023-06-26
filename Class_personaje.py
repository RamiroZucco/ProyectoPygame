from configuraciones import *
class Personaje:
    def __init__(self, tamaño, animaciones, posicion_inicial,velocidad, limite_x, vida):
        self.ancho = tamaño[0]
        self.alto = tamaño[1]

        self.gravedad = 1
        self.potencia_salto = -15
        self.limite_velocidad_caida = 15
        self.esta_saltando = False

        self.contador_pasos = 0
        self.que_hace = "Quieto"
        self.animaciones = animaciones
        self.reescalar_animaciones()
        
        rectangulo = self.animaciones["Derecha"][0].get_rect()
        rectangulo.x = posicion_inicial[0]
        rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulos(rectangulo)
        self.velocidad = velocidad
        self.desplazamiento_y = 0
        self.limite_x = limite_x

        self.vida = vida
        self.colisionado = False
        self.DURACION_DANADO = 1
        self.tiempo_colision = 0
        self.tiempo_danado = 0

        self.municion = 0 

        self.imagen_vida = pygame.image.load("PROYECTO PYGAME\\Recursos\\Vida\\pngegg.png")
        self.imagen_vida = pygame.transform.scale(self.imagen_vida, (50, 50))
        self.posicion_vidas = (300, 830)

        self.sonido_colision = pygame.mixer.Sound("PROYECTO PYGAME\\Recursos\\SonidoPerderVida\\27425__hello_flowers__nu_glch_mplez_4i.wav")
        self.sonido_colision.set_volume(0.5)

    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave],self.ancho,self.alto)

    def aplicar_gravedad(self, pantalla, lista_plataformas):
        if self.esta_saltando:
            self.animar(pantalla, "Salta")
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
        if self.vida > 0:    
            if self.que_hace == "Derecha":
                if not self.esta_saltando:
                    self.animar(pantalla,"Derecha")
                self.mover(self.velocidad, self.limite_x)
            elif self.que_hace == "Izquierda":
                if not self.esta_saltando:
                    self.animar(pantalla,"Izquierda")
                self.mover(self.velocidad *-1, self.limite_x)
            elif self.que_hace == "Salta":
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
            elif self.que_hace == "Quieto":
                if not self.esta_saltando:
                    self.animar(pantalla, "Quieto")
            elif self.que_hace == "Dañado":
                if not self.esta_saltando:
                    self.animar(pantalla, "Dañado")
                    tiempo_actual = pygame.time.get_ticks()
                    duracion_colision = tiempo_actual - self.tiempo_colision
                    print(self.tiempo_colision)
                    print(self.DURACION_DANADO)
                    print(tiempo_actual)
                    print(duracion_colision)
                    if duracion_colision >= self.DURACION_DANADO:
                        self.vida -= 1 
                        self.tiempo_colision = 0
                        self.mover(self.velocidad, 200)                   
            
            self.aplicar_gravedad(pantalla,piso)
                          
    
    def verificar_colision_obstaculo(self, lista_obstaculos):
        for obstaculo in lista_obstaculos:
            if self.lados["main"].colliderect(obstaculo.lados["main"]):
                self.que_hace = "Dañado"
                self.sonido_colision.play()
                self.colisionado = True
                self.tiempo_colision = pygame.time.get_ticks()

    def verificar_colision_enemigo(self, lista_enemigos):
        for enemigo in lista_enemigos:
            if self.lados["main"].colliderect(enemigo.lados["main"]):
                self.que_hace = "Dañado"
                self.sonido_colision.play()
                self.colisionado = True
                self.tiempo_colision = pygame.time.get_ticks()            

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

        imagen_municion = pygame.image.load("PROYECTO PYGAME\\Recursos\\Disparo\\23.png")
        imagen_municion = pygame.transform.scale(imagen_municion, (30, 30))
        rectangulo_imagen = imagen_municion.get_rect()
        rectangulo_imagen.left = rectangulo_texto.right + 10
        rectangulo_imagen.centery = rectangulo_texto.centery

        pantalla.blit(superficie_texto, rectangulo_texto)
        pantalla.blit(imagen_municion, rectangulo_imagen)
                   
                
              
    
