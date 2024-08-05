import customtkinter as ctk
from assets.icons.icone import iconLupa
from PIL import Image
from crud import usuarioCRUD
from widgets.widgetUsuario import WidgetUsuario
import threading

class TelaGerenciarUsuarios(ctk.CTkFrame):
    def __init__(self, master, root):
        super().__init__(master)
        self.root = root
        self.todosUsuarios = []
        self.configurar_tela()
        self.criar_widgets()
        self.carregar_widgets()
        self.carregar_tela()
        # thead = threading.Thread(target=self.atualizar_dados)
        # thead.start()
        
        
    def configurar_tela(self):
        self.configure(bg_color='transparent')
        self.configure(fg_color='white')
        self.configure(corner_radius=0)
        
    def criar_widgets(self):
        config_label = {'text_color':'black'}
        icon_lupa = ctk.CTkImage(Image.open(iconLupa), size=(24,24))
        
        
        self.frMain = ctk.CTkFrame(self, bg_color='transparent', fg_color='transparent')
        self.frBusca = ctk.CTkFrame(self.frMain, fg_color='transparent', height=50, border_color='black', 
                                    border_width=2, corner_radius=25)
    
        self.frUsuarios = ctk.CTkScrollableFrame(self.frMain, bg_color='transparent', fg_color='transparent')
        self.frUsuarios.master = self.frUsuarios._parent_canvas
        self.lbTitulo = ctk.CTkLabel(self.frMain, text='Gerenciar Usuarios', font=ctk.CTkFont("Inter", weight='bold', size=30),
                                     **config_label)
        
        self.lbImagemLupa = ctk.CTkLabel(self.frBusca, text='', image=icon_lupa)
        self.entryBusca = ctk.CTkEntry(self.frBusca, placeholder_text="Digite o nome do usuario", height=40,
                                       font=ctk.CTkFont('Inter', weight='normal', size=15), text_color='black', fg_color='transparent',
                                       bg_color='transparent', border_color='white')
        
        self.consultar_usuarios()
        
    def carregar_widgets(self):
        self.frMain.pack(expand=True, fill=ctk.BOTH, padx=10, pady=10)
        self.lbTitulo.pack(pady=(20,5))
        self.frBusca.pack(fill=ctk.X, pady=10, padx=20)
        self.frUsuarios.pack(fill=ctk.BOTH, expand=True)


        self.lbImagemLupa.pack(side=ctk.LEFT, padx=(15,10), pady=10)
        self.entryBusca.pack(fill=ctk.BOTH,expand=True, side=ctk.LEFT, padx=(0,15), pady=10)
        

        self.carregar_widgetUsuario()
        
        
    def consultar_usuarios(self):
        if len(self.todosUsuarios) > 0:
            self.todosUsuarios = []
        
        for usuario in usuarioCRUD.selecionar_todos_usuarios():
            self.todosUsuarios.append(WidgetUsuario(self.frUsuarios, self.root, usuario))
        
            
    def carregar_widgetUsuario(self):
        
        self.ocultar_widgetUsuario()
        
        if len(self.todosUsuarios)>0:
            for usuario in self.todosUsuarios:
                usuario.carregar_tela()
             
    def ocultar_widgetUsuario(self):
        if len(self.todosUsuarios)>0:
            for usuario in self.todosUsuarios:
                if usuario.winfo_viewable():
                    usuario.pack_fortet()
                    
    # def atualizar_dados(self):
    #     while True:
    #         if len(self.todosUsuarios) != usuarioCRUD.quantidade_usuarios():
    #             self.consultar_usuarios()
    #             self.carregar_widgetUsuario()

    def carregar_tela(self):
        self.pack(fill=ctk.BOTH, expand=True)
