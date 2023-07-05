import pygame
from pygame.locals import * 
from GUI.GUI_form import *
from GUI.GUI_button_image import *
from GUI.GUI_label import *
from GUI.GUI_slider import *
from GUI.GUI_picture_box import *
from Niveles.manejador_niveles import *
from GUI.GUI_form_contenedor_niveles import *
class FormGameOver(Form):
    def __init__(self,screen,x,y,w,h,active, path_img):
        super().__init__(screen,x,y,w,h,active)
        aux_imagen = pygame.image.load(path_img)
        aux_imagen = pygame.transform.scale(aux_imagen,(w,h))
        
        self.render()

        self._slave = aux_imagen
        
        self._btn_home = Button_Image(self._slave,master_x = x,master_y=y,x=200,y=200,w=100,h=100,color_background=(255,0,0),color_border=(255,0,255),onclick=self.btn_home_click,onclick_param="",text="",font="Verdana",font_size=15,font_color=(0,255,0),path_image="PROYECTO PYGAME\Recursos\Disparo\municion2.png")   
        self.lista_widgets.append(self._btn_home)
    
    def btn_home_click(self,parametro):
        self.end_dialog()

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
        else:
            self.hijo.update(lista_eventos)

        

    
            
                      