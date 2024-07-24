import customtkinter as ctk
from assets.icons.icone import iconUsuario, iconSair
from PIL import Image


class TelaMenuUsuario(ctk.CTkFrame):
    def __init__(self, master, button):
        super().__init__(master, corner_radius=0, bg_color='#bed0e8', fg_color='#bed0e8')
        self.master=master
        self.button=button
        self.criar_widgets()
        self.carregar_widgets()
        self.carregar_tela()

        
    def criar_widgets(self):
    
        config_button = {'fg_color':'transparent', 'bg_color':'transparent', 'hover_color':'#A0B7D5',
                         'height':30, 'corner_radius':0, 'text_color':'black', 'font':ctk.CTkFont('Inter', weight='normal', size=15),
                         'anchor':ctk.W, 'width':250}
        icon_sair = ctk.CTkImage(Image.open(iconSair), size=(16,16))
        icon_usuario = ctk.CTkImage(Image.open(iconUsuario), size=(16,16))
        self.btPerfil = ctk.CTkButton(self, text='Meu Perfil',image=icon_usuario, compound=ctk.LEFT,
                                      command=self.master.carregar_tela_usuario ,**config_button)
        self.btSair = ctk.CTkButton(self, text='Sair', image=icon_sair, compound=ctk.LEFT,
                                    command=self.sair, **config_button)
    
    def sair(self):
        self.master.carregar_tela_login()
        self.destroy()
    def carregar_widgets(self):
        self.btPerfil.pack(pady=(20,0))
        self.btSair.pack(pady=(0,20))

    def carregar_tela(self):
        self.master.update()
        pos_x, pos_y = (self.button.winfo_x()+self.button.winfo_width()+100),(self.button.winfo_y() + self.button.winfo_height() - 10)
        self.place(x=pos_x, y=pos_y, anchor=ctk.NE)
        