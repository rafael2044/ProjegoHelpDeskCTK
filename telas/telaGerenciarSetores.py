import customtkinter as ctk
from assets.icons.icone import iconLupa
from PIL import Image
from crud import setorCRUD
from widgets.widgetSetor import WidgetSetor

class TelaGerenciarSetor(ctk.CTkScrollableFrame):
    def __init__(self, master, root):
        super().__init__(master)
        self.master= self._parent_canvas
        self.root = root
        self.todosSetores = []
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
    
        self.frSetores = ctk.CTkFrame(self.frMain, bg_color='transparent', fg_color='transparent')

        self.lbTitulo = ctk.CTkLabel(self.frMain, text='Gerenciar Setores', font=ctk.CTkFont("Inter", weight='bold', size=30),
                                     **config_label)
        
        self.lbImagemLupa = ctk.CTkLabel(self.frBusca, text='', image=icon_lupa)
        self.entryBusca = ctk.CTkEntry(self.frBusca, placeholder_text="Digite o nome do setor", height=40,
                                       font=ctk.CTkFont('Inter', weight='normal', size=15), text_color='black', fg_color='transparent',
                                       bg_color='transparent', border_color='white')
        
        self.carregar_dados_setores()
        
    def carregar_widgets(self):
        self.frMain.pack(expand=True, fill=ctk.BOTH, padx=10, pady=10)
        self.lbTitulo.pack(pady=(20,5))
        self.frBusca.pack(fill=ctk.X, pady=10, padx=20)
        self.frSetores.pack(fill=ctk.BOTH, expand=True)

        self.lbImagemLupa.pack(side=ctk.LEFT, padx=(15,10), pady=10)
        self.entryBusca.pack(fill=ctk.BOTH,expand=True, side=ctk.LEFT, padx=(0,15), pady=10)
        

        self.carregar_setores()

    
    def carregar_dados_setores(self):
        setores = setorCRUD.selecionar_todos_setores()
        for setor in setores:
            self.todosSetores.append(WidgetSetor(self.frSetores, self.root, setor))
        
            
    def carregar_setores(self):
        if len(self.todosSetores)!=0:
            for setor in self.todosSetores:
                setor.carregar_tela()
                
        
    def carregar_tela(self):
        self.pack(fill=ctk.BOTH, expand=True)
