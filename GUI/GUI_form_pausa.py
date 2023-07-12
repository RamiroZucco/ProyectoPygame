import pygame
from pygame.locals import *
from GUI.GUI_button import *
from GUI.GUI_slider import *
from GUI.GUI_textbox import *
from GUI.GUI_label import *
from GUI.GUI_form import *
from GUI.GUI_button_image import *
from GUI.GUI_form_configuracion import *
from GUI.GUI_picture_box import *

class FormPausa(Form):
    def __init__(self,screen,x,y,w,h,active, path_img):
        super().__init__(screen,x,y,w,h,active)
        
        self.render()

        aux_imagen = pygame.image.load(path_img)
        aux_imagen = pygame.transform.scale(aux_imagen,(w,h))
        
        self._slave = aux_imagen
        
        self.btn_config = Button_Image(self._slave,x,y,340,450,50,50,"PROYECTO PYGAME copy\\Recursos\\Interfaz\\1.png",self.btn_config_click,"None")
        self.btn_continuar = Button_Image(self._slave,x,y, 195, 455, 115, 45,"PROYECTO PYGAME copy\\Recursos\\Interfaz\\5.png",self.btn_continuar_click,"None")
        
        ### AGREGO CONTROLES A LA LISTA
        self.lista_widgets.append(self.btn_config)
        self.lista_widgets.append(self.btn_continuar)
        ###

        self.render()
    
    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
        else:
            self.hijo.update(lista_eventos)     
 
    
    def btn_config_click(self,texto):
        form_configuracion = FormConfiguracion(self._master,650,55,500,550,True,"PROYECTO PYGAME\Recursos\Interfaz\pngegg.png")
        self.show_dialog(form_configuracion)

    def btn_continuar_click(self,param):
        self.end_dialog() 

                


