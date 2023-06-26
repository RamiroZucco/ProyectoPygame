import pygame
from pygame.locals import * 
from GUI_form import *
from GUI_button_image import *
from GUI_label import *
from GUI_slider import *
from GUI_picture_box import *
class FormConfiguracion(Form):
    def __init__(self,screen,x,y,w,h,active, path_img):
        super().__init__(screen,x,y,w,h,active)
        
        aux_imagen = pygame.image.load(path_img)
        aux_imagen = pygame.transform.scale(aux_imagen,(w,h))
        
        self.render()

        self._slave = aux_imagen
        
        self._btn_home = Button_Image(screen=self._slave,x=w-80,y=h-80,master_x = x,master_y=y,w=40,h=40,color_background=(255,0,0),color_border=(255,0,255),onclick=self.btn_home_click,onclick_param="",text="",font="Verdana",font_size=15,font_color=(0,255,0),path_image="PROYECTO PYGAME\home.png")   
        self.lista_widgets.append(self._btn_home)
        self.btn_play = Button_Image(self._slave,x,y,400,330,50,50,"PROYECTO PYGAME\Recursos\Interfaz\pngegg (1).png", self.btn_play_click,"None")
        self.lista_widgets.append(self.btn_play)

        self.volumen = 0.2
        self.flag_play = True

        self.picture_pausa = PictureBox(self._slave, 180, 50, 130, 70,"PROYECTO PYGAME\Recursos\Interfaz\8.png")
        self.label_volumen = Label(self._slave, 365, 270, 100, 50, "20%","Comic Sans",15,"Black","PROYECTO PYGAME\\Recursos\\Interfaz\\5.png")
        self.slider_volumen = Slider(self._slave,x,y,50,300,300,10,self.volumen,"White","Black")
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.picture_pausa)

        pygame.mixer.music.load("PROYECTO PYGAME\Recursos\SonidoDeFondo\donkey-kong-country.mp3")
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