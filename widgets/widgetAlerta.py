import customtkinter as ctk
import time
from assets.icons.icone import iconAlerta, iconErro, iconInfo, iconSucesso
from PIL import Image
class WidgetAlerta(ctk.CTkFrame):
    def __init__(self, master, mensagem, tipo='alerta'):
        self.master=master
        self.tipo = tipo
        self.mensagem = mensagem
        self.TIPOS = {'alerta':{'fg_color':'#ffc107', 'bg_color':'#ffc107'},
                 'sucesso':{'fg_color':'#198754', 'bg_color':'#198754'},
                 'info':{'fg_color':'#0dcaf0', 'bg_color':'#0dcaf0'},
                 'erro':{'fg_color':'#dc3545', 'bg_color':'#dc3545'}}
        self.ICON = {'alerta':ctk.CTkImage(Image.open(iconAlerta), size=(32,32)),
                'sucesso':ctk.CTkImage(Image.open(iconSucesso), size=(32,32)),
                'info':ctk.CTkImage(Image.open(iconInfo), size=(32,32)),
                'erro':ctk.CTkImage(Image.open(iconErro), size=(32,32))}
        super().__init__(self.master, **self.TIPOS[self.tipo], height=50, corner_radius=0, border_width=0)
        self.criar_widgets()
        self.carregar_widgets()
        self.carregar_tela()
    
    def criar_widgets(self):
        self.lbIcon = ctk.CTkLabel(self, text='', image=self.ICON[self.tipo])
        self.lbMensagem = ctk.CTkLabel(self, text=self.mensagem, font=ctk.CTkFont('Inter', size=15),
                                       text_color='black')
        
    def carregar_widgets(self):
        self.lbIcon.pack(side=ctk.LEFT, padx=(10,0))
        self.lbMensagem.pack(side=ctk.LEFT, padx=10, pady=15)
        
    def carregar_tela(self):
        self.place(rely=1, anchor=ctk.SW, relwidth=1)
        time.sleep(3)
        self.destroy()
        
        
        
