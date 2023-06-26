import pygame
from pygame.locals import *
from GUI_button import *
from GUI_slider import *
from GUI_textbox import *
from GUI_label import *
from GUI_form import *
from GUI_button_image import *
from GUI_form_configuracion import *
from GUI_picture_box import *

class FormPrueba(Form):
    def __init__(self,screen,x,y,w,h,active, path_img):
        super().__init__(screen,x,y,w,h,active)
        
        self.render()

        aux_imagen = pygame.image.load(path_img)
        aux_imagen = pygame.transform.scale(aux_imagen,(w,h))
        
        self._slave = aux_imagen
        
        self.btn_config = Button_Image(self._slave,x,y,340,450,50,50,"PROYECTO PYGAME\\Recursos\\Interfaz\\1.png",self.btn_config_click,"None")
        self.picture_pausa = PictureBox(self._slave, 180, 50, 130, 70,"PROYECTO PYGAME\Recursos\Interfaz\8.png")
        self.btn_continuar = Button_Image(self._slave,x,y, 195, 455, 115, 45,"PROYECTO PYGAME\\Recursos\\Interfaz\\7.png",self.btn_continuar_click,"None")
        self.picture_btn_pausa = PictureBox(self._slave, 120,450,50,50,"PROYECTO PYGAME\\Recursos\\Interfaz\\6.png")
        self.picture_personaje = PictureBox(self._slave, 80,150,200,250,"PROYECTO PYGAME\\Recursos\\0.png")
        self.picture_boss = PictureBox(self._slave, 230,150,200,250,"PROYECTO PYGAME\Recursos\8.png")


        ### AGREGO CONTROLES A LA LISTA
        self.lista_widgets.append(self.btn_config)
        self.lista_widgets.append(self.picture_pausa)
        self.lista_widgets.append(self.btn_continuar)
        self.lista_widgets.append(self.picture_btn_pausa)
        self.lista_widgets.append(self.picture_boss)
        self.lista_widgets.append(self.picture_personaje)
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

                


