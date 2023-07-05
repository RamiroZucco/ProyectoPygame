import pygame
from pygame.locals import * 
from GUI.GUI_form import *
from GUI.GUI_button_image import *
from GUI.GUI_label import *
from GUI.GUI_slider import *
from GUI.GUI_picture_box import *
from Niveles.manejador_niveles import *
from GUI.GUI_form_contenedor_niveles import *
class FormNiveles(Form):
    def __init__(self,screen,x,y,w,h,active, path_img):
        super().__init__(screen,x,y,w,h,active)
        self.manejador_niveles = Manejador_niveles(self._master)
        aux_imagen = pygame.image.load(path_img)
        aux_imagen = pygame.transform.scale(aux_imagen,(w,h))
        
        self.render()

        self._slave = aux_imagen
        
        self._btn_home = Button_Image(screen=self._slave,x=w-250,y=h-130,master_x = x,master_y=y,w=200,h=40,color_background=(255,0,0),color_border=(255,0,255),onclick=self.btn_home_click,onclick_param="",text="",font="Verdana",font_size=15,font_color=(0,255,0),path_image="PROYECTO PYGAME\Recursos\Superficie\pngwing.com (1).png")
        self._btn_nivel_uno = Button_Image(screen=self._slave,x=860,y=255,master_x = x,master_y=y,w=170,h=170,onclick=self.entrar_nivel,onclick_param="nivel_uno",path_image="PROYECTO PYGAME\Recursos\Superficie\pngwing.com (1).png") 
        self._btn_nivel_dos = Button_Image(screen=self._slave,x=860,y=455,master_x = x,master_y=y,w=170,h=170,onclick=self.entrar_nivel,onclick_param="nivel_dos",path_image="PROYECTO PYGAME\Recursos\Superficie\pngwing.com (1).png")
        self._btn_nivel_tres = Button_Image(screen=self._slave,x=860,y=655,master_x = x,master_y=y,w=170,h=170,onclick=self.entrar_nivel,onclick_param="nivel_tres",path_image="PROYECTO PYGAME\Recursos\Superficie\pngwing.com (1).png")   
        self.lista_widgets.append(self._btn_home)
        self.lista_widgets.append(self._btn_nivel_uno)
        self.lista_widgets.append(self._btn_nivel_dos)
        self.lista_widgets.append(self._btn_nivel_tres)
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
        else:
            self.hijo.update(lista_eventos)

    def entrar_nivel(self, nombre_nivel):
        nivel = self.manejador_niveles.get_nivel(nombre_nivel)
        form_contenedor_nivel = FormContenedorNivel(self._master, nivel)
        self.show_dialog(form_contenedor_nivel)
            
                      