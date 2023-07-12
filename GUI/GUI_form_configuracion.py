import pygame
from pygame.locals import * 
from GUI.GUI_form import *
from GUI.GUI_button_image import *
from GUI.GUI_label import *
from GUI.GUI_slider import *
from GUI.GUI_picture_box import *
class FormConfiguracion(Form):
    def __init__(self,screen,x,y,w,h,active, path_img):
        super().__init__(screen,x,y,w,h,active)
        
        aux_imagen = pygame.image.load(path_img)
        aux_imagen = pygame.transform.scale(aux_imagen,(w,h))
        
        self.render()

        self._slave = aux_imagen
        
        self._btn_home = Button_Image(screen=self._slave,x=w-250,y=h-130,master_x = x,master_y=y,w=200,h=40,color_background=(255,0,0),color_border=(255,0,255),onclick=self.btn_home_click,onclick_param="",text="",font="Verdana",font_size=15,font_color=(0,255,0),path_image="PROYECTO PYGAME copy\Recursos\Superficie\pngwing.com (1).png")   
        self.lista_widgets.append(self._btn_home)
        self.btn_play = Button_Image(self._slave,x,y,1220,480,110,110,"PROYECTO PYGAME copy\Recursos\Superficie\pngwing.com (1).png", self.btn_play_click,"None")
        self.lista_widgets.append(self.btn_play)

        self.volumen = 0.2
        self.flag_play = True

        self.label_volumen = Label(self._slave, 1220, 380, 100, 50, "20%","Comic Sans",15,"Black","PROYECTO PYGAME copy\Recursos\Interfaz\inter (1).png")
        self.slider_volumen = Slider(self._slave,x,y, 680, 400,500,20,self.volumen,"White","Black")
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.slider_volumen)

        pygame.mixer.music.load("PROYECTO PYGAME copy\Recursos\SonidoDeFondo\donkey-kong-country.mp3")
        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)

        pygame.mixer.init()
    
    
    def btn_home_click(self,parametro):
        self.end_dialog()     

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                self.update_volumen(lista_eventos)
        else:
            self.hijo.update(lista_eventos)      
            
    def btn_play_click(self, texto):
        if self.flag_play:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
        self.flag_play = not self.flag_play

    def update_volumen(self,lista_eventos):
        self.volumen = self.slider_volumen.value
        self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)                       