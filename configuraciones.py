import pygame

def girar_imagenes(lista_original, flip_x, flip_y):
    lista_girada = []
    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))
    return lista_girada    

def reescalar_imagenes(lista_imagenes, W, H):    
    for i in range(len(lista_imagenes)):
        lista_imagenes[i] = pygame.transform.scale(lista_imagenes[i],(W, H))

def obtener_rectangulos(principal: pygame.Rect):
    diccionario = {}
    ancho_extra = 10  

    # main - bottom - left - top - right
    diccionario["main"] = principal
    diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom - 10, principal.width, 10)
    diccionario["right"] = pygame.Rect(principal.right - ancho_extra, principal.top, 2 + ancho_extra, principal.height)
    diccionario["left"] = pygame.Rect(principal.left - ancho_extra, principal.top, 2 + ancho_extra, principal.height)
    diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 10)       

    return diccionario


personaje_quieto = [ 
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Quieto\\3.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Quieto\\h.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Quieto\\i.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Quieto\\j.png"),
]

personaje_camina = [
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Camina\\4.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Camina\\5.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Camina\\6.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Camina\\7.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Camina\\8.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Camina\\9.png")
]

personaje_camina_izquierda = girar_imagenes(personaje_camina, True, False)

personaje_salta = [
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Salta\\13.png")
]

personaje_dañado = [
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Dañado\\15.png")
]

personaje_muerto = [
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Dañado\\14.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Dañado\\15.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Dañado\\16.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Dañado\\17.png")
]

perro_derecha = [
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Perro\\0.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Perro\\1.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Perro\\2.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Perro\\3.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Perro\\4.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Perro\\5.png")
]

perro_izquierda = girar_imagenes(perro_derecha,True,False)

pajaro_derecha = [
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Pajaro\\0.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Pajaro\\1.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Pajaro\\2.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Pajaro\\3.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Pajaro\\4.png")
]

pajaro_izquierda = girar_imagenes(pajaro_derecha,True,False)

diccionario_animaciones = {}
diccionario_animaciones["Quieto"] = personaje_quieto
diccionario_animaciones["Salta"] = personaje_salta
diccionario_animaciones["Izquierda"] = personaje_camina_izquierda
diccionario_animaciones["Derecha"] = personaje_camina
diccionario_animaciones["Dañado"] = personaje_dañado
diccionario_animaciones["Muerto"] = personaje_muerto

diccionario_animaciones_enemigo = {}
diccionario_animaciones_enemigo["Derecha"] = perro_derecha
diccionario_animaciones_enemigo["Izquierda"] = perro_izquierda

diccionario_animaciones_enemigo_dos = {}
diccionario_animaciones_enemigo_dos["Izquierda"] = pajaro_izquierda
diccionario_animaciones_enemigo_dos["Derecha"] = pajaro_derecha

def mostrar_cronometro(pantalla, fuente, texto, x, y):
    tipo_letra = pygame.font.Font(fuente, 40)
    superficie_texto = tipo_letra.render(texto, True, (255, 255, 255))
    rectangulo_texto = superficie_texto.get_rect()
    rectangulo_texto.midleft = (x, y)

    imagen_reloj = pygame.image.load("PROYECTO PYGAME/Recursos/Reloj/pngegg.png")
    imagen_reloj = pygame.transform.scale(imagen_reloj, (30, 30))
    rectangulo_reloj = imagen_reloj.get_rect()
    rectangulo_reloj.midleft = (rectangulo_texto.right + 10, y-3)

    pantalla.blit(superficie_texto, rectangulo_texto)
    pantalla.blit(imagen_reloj, rectangulo_reloj)






