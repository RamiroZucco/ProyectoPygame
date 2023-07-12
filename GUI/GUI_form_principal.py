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
from GUI.GUI_form_niveles import *
from GUI.GUI_form_ranking import *
import sys

class FormPrincipal(Form):
    def __init__(self,screen,x,y,w,h,active, path_img):
        super().__init__(screen,x,y,w,h,active)
        
        self.render()

        aux_imagen = pygame.image.load(path_img)
        aux_imagen = pygame.transform.scale(aux_imagen,(w,h))
        
        self._slave = aux_imagen
        self.fuente = pygame.font.match_font('consolas')
        
        self.btn_config = Button_Image(self._slave,x,y,570,500,800,50,"PROYECTO PYGAME copy\Recursos\Superficie\pngwing.com (1).png",self.btn_config_click,"None")
        self.btn_continuar = Button_Image(self._slave,x,y, 800, 430,300,50,"PROYECTO PYGAME copy\Recursos\Superficie\pngwing.com (1).png",self.btn_continuar_click,"None")
        self.btn_salir = Button_Image(self._slave,x,y, 800, 660,300,50,"PROYECTO PYGAME copy\Recursos\Superficie\pngwing.com (1).png",self.btn_salir_click,"None")
        self.btn_ranking = Button_Image(self._slave,x,y, 740, 580,420,50,"PROYECTO PYGAME copy\Recursos\Superficie\pngwing.com (1).png",self.btn_ranking_click,"None")
        self.textbox_usuario = TextBox(self._slave,x,y,1020,325,300,50,"White","White","Yellow","Yellow",3,self.fuente,50,"Black")

        ### AGREGO CONTROLES A LA LISTA
        self.lista_widgets.append(self.btn_config)
        self.lista_widgets.append(self.btn_continuar)
        self.lista_widgets.append(self.textbox_usuario)
        self.lista_widgets.append(self.btn_salir)
        self.lista_widgets.append(self.btn_ranking)
        ###

        self.render()

        self.volumen = 0.2
        pygame.mixer.music.load("PROYECTO PYGAME copy\Recursos\SonidoDeFondo\donkey-kong-country.mp3")
        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)

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
        form_configuracion = FormConfiguracion(self._master,0,0,self._slave.get_width(),self._slave.get_height(),True,"PROYECTO PYGAME copy\Recursos\Interfaz\config.png")
        self.show_dialog(form_configuracion)

    def btn_continuar_click(self,param):
        form_niveles = FormNiveles(self._master,0,0,self._slave.get_width(),self._slave.get_height(),True,"PROYECTO PYGAME copy\\Recursos\\Interfaz\\2.png")
        self.show_dialog(form_niveles)

    def btn_salir_click(self,param):
        pygame.quit()
        sys.exit(0)

    def btn_ranking_click(self,param):
        form_ranking = FormRanking(self._master,0,0,self._slave.get_width(),self._slave.get_height(),True,"PROYECTO PYGAME copy\\Recursos\\Interfaz\\4.png")
        self.show_dialog(form_ranking)
            

                


