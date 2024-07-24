import customtkinter as ctk
from assets.icons.icone import iconLupa
from PIL import Image
from models.usuario import Usuario
from widgets.widgetUsuario import WidgetUsuario

class TelaGerenciarUsuarios(ctk.CTkScrollableFrame):
    def __init__(self, master, root):
        super().__init__(master)
        self.master= self._parent_canvas
        self.root = root
        self.todosUsuarios = []
        self.configurar_tela()
        self.criar_widgets()
        self.carregar_widgets()
        self.carregar_tela()
        
        
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
    
        self.frUsuarios = ctk.CTkFrame(self.frMain, bg_color='transparent', fg_color='transparent')

        self.frRodape = ctk.CTkFrame(self.frMain, bg_color='transparent', fg_color='transparent')
        
        self.lbNomeSistema = ctk.CTkLabel(self.frRodape, text="helpdesk", font=ctk.CTkFont("Inter", weight='bold', size=20),
                                     text_color='#0d6efd')
        self.lbCopyright = ctk.CTkLabel(self.frRodape, text="© 2024 Rafael. Todos os direitos reservados", font=ctk.CTkFont("Inter", weight='normal', size=17),
                                     text_color='gray')
        
        self.lbTitulo = ctk.CTkLabel(self.frMain, text='Gerenciar Usuarios', font=ctk.CTkFont("Inter", weight='bold', size=30),
                                     **config_label)
        
        self.lbImagemLupa = ctk.CTkLabel(self.frBusca, text='', image=icon_lupa)
        self.entryBusca = ctk.CTkEntry(self.frBusca, placeholder_text="Digite o nome do usuario", height=40,
                                       font=ctk.CTkFont('Inter', weight='normal', size=15), text_color='black', fg_color='transparent',
                                       bg_color='transparent', border_color='white')
        
        self.carregar_dados_usuarios()
        
    def carregar_widgets(self):
        self.frMain.pack(expand=True, fill=ctk.BOTH, padx=10, pady=10)
        self.lbTitulo.pack(pady=(20,5))
        self.frBusca.pack(fill=ctk.X, pady=10, padx=20)
        self.frUsuarios.pack(fill=ctk.BOTH, expand=True)
        self.frRodape.pack(fill=ctk.X)

        self.lbImagemLupa.pack(side=ctk.LEFT, padx=(15,10), pady=10)
        self.entryBusca.pack(fill=ctk.BOTH,expand=True, side=ctk.LEFT, padx=(0,15), pady=10)
        

        self.carregar_usuarios()
        
        self.lbNomeSistema.pack(padx=5, pady=5, anchor=ctk.W)
        ctk.CTkFrame(self.frRodape, height=2, fg_color='gray').pack(fill=ctk.X, padx=5)
        self.lbCopyright.pack(padx=5, anchor=ctk.W)
        
        
    def carregar_dados_usuarios(self):
        query_usuario = Usuario.select()
        for usuario in query_usuario:
            self.todosUsuarios.append(WidgetUsuario(self.frUsuarios, self.root, usuario))
        
            
    def carregar_usuarios(self):
        if len(self.todosUsuarios)!=0:
            for usuario in self.todosUsuarios:
                usuario.carregar_tela()
                
        
    def carregar_tela(self):
        self.pack(fill=ctk.BOTH, expand=True)
