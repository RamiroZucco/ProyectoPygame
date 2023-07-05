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
    
    # main - bottom - left - top - right
    diccionario["main"] = principal
    diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom - 10, principal.width, 10)
    diccionario["right"] = pygame.Rect(principal.right - 10, principal.top, 10, principal.height)
    diccionario["left"] = pygame.Rect(principal.left, principal.top, 10, principal.height)
    diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 6)      
    return diccionario

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

personaje_quieto_izquierda = [ 
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Quieto\\11.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Quieto\\12.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Quieto\\13.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Quieto\\14.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Quieto\\15.png")
    ]

personaje_quieto_derecha = girar_imagenes(personaje_quieto_izquierda, True, False)

personaje_camina_izquierda = [
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Camina\\0.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Camina\\1.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Camina\\2.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Camina\\3.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Camina\\4.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Camina\\5.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Camina\\6.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Camina\\7.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Camina\\8.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Camina\\9.png")
    ]

personaje_camina_derecha = girar_imagenes(personaje_camina_izquierda, True, False)

personaje_salta_izquierda = [
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Salta\\7.png")
    ]

personaje_salta_derecha = girar_imagenes(personaje_salta_izquierda,True,False)

personaje_dañado = [
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Dañado\\1.png")
    ]

perro_derecha = [
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Enemigo\\0.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Enemigo\\1.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Enemigo\\2.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Enemigo\\3.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Enemigo\\4.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Enemigo\\5.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Enemigo\\6.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Enemigo\\7.png")
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

araña_izquierda = [
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Araña\\0.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Araña\\1.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Araña\\2.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Araña\\3.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Araña\\4.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Araña\\5.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Araña\\6.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Araña\\7.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Araña\\8.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Araña\\9.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Araña\\10.png")
    ]

araña_derecha = girar_imagenes(araña_izquierda,True,False)

pez_volador_izquierda = [
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Pez_Volador\\0.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Pez_Volador\\1.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Pez_Volador\\2.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Pez_Volador\\3.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Pez_Volador\\4.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Pez_Volador\\5.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Pez_Volador\\6.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Pez_Volador\\7.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Pez_Volador\\8.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Pez_Volador\\9.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Pez_Volador\\10.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Pez_Volador\\11.png")
    ]

pez_volador_derecha = girar_imagenes(pez_volador_izquierda,True,False)

mono_izquierda = [
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Mono\\6.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Mono\\7.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Mono\\8.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Mono\\9.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Mono\\10.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Mono\\11.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Mono\\12.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Mono\\13.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Mono\\14.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Mono\\15.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Mono\\16.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Mono\\17.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Mono\\18.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Mono\\19.png")
    ]

mono_derecha = girar_imagenes(mono_izquierda,True,False)

mosquito_izquierda = [
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Mosquito\\0.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Mosquito\\1.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Mosquito\\2.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Mosquito\\3.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Mosquito\\4.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Mosquito\\5.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Mosquito\\6.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Mosquito\\7.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Mosquito\\8.png"),
    pygame.image.load("PROYECTO PYGAME\\Recursos\\Movimiento_Mosquito\\9.png")
    ]

mosquito_derecha = girar_imagenes(mosquito_izquierda,True,False)

