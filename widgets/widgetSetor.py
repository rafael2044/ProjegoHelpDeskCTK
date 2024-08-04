import customtkinter as ctk
from telas.telaAtualizarChamado import TelaAtualizarChamado
from telas.telaAtenderChamado import TelaAtenderChamado

class WidgetSetor(ctk.CTkFrame):
    def __init__(self, master,root, setor):
        super().__init__(master=master, cursor='hand2')
        self.setor = setor
        self.root=root
        self.configurar_tela()
        self.criar_widgets()
        self.carregar_widgets()
        self.bind('<Motion>', self.aplicar_hover_color)
        self.bind("<Leave>", self.aplicar_hover_color)
        

        
    def configurar_tela(self):
        self.configure(fg_color='#f2f2f2')
        self.configure(corner_radius=20)
        
    def criar_widgets(self):
        
        config_label_campos = {'text_color':'gray', 'font':ctk.CTkFont('Inter', weight='normal', size=15), 'bg_color':'transparent'}
        config_label_dados = {'text_color':'black', 'font':ctk.CTkFont('Inter', weight='normal', size=18)}
        config_frame = {'fg_color':'transparent', 'bg_color':'transparent'}
        self.frId = ctk.CTkFrame(self, **config_frame)
        self.frNomeSetor = ctk.CTkFrame(self, **config_frame)
        self.frComandos = ctk.CTkFrame(self, **config_frame)
        
        
        self.lbCampoId = ctk.CTkLabel(self.frId, text='ID', **config_label_campos)
        self.lbCampoNomeSetor = ctk.CTkLabel(self.frNomeSetor, text='Nome do Setor', **config_label_campos)
        
        self.lbDadosId = ctk.CTkLabel(self.frId, text=self.setor.id, **config_label_dados)
        self.lbDadosNomeSetor = ctk.CTkLabel(self.frNomeSetor, text=self.setor.nome, **config_label_dados)
        
        self.btEditar = ctk.CTkButton(self.frComandos, text='Editar')
        self.btExcluir = ctk.CTkButton(self.frComandos, text='Excluir')
            
        
    def carregar_widgets(self):
        config_pack = {'padx':5, 'pady':5, 'fill':ctk.X, 'side':ctk.LEFT}
        self.frId.pack(**config_pack)
        self.frNomeSetor.pack(expand=True,**config_pack)
        self.frComandos.pack(**config_pack)
        
        config_pack_label = {'padx':5, 'pady':5, 'anchor':ctk.W}
        self.lbCampoId.pack(**config_pack_label)
        self.lbDadosId.pack(**config_pack_label)
        self.lbCampoNomeSetor.pack(**config_pack_label)
        self.lbDadosNomeSetor.pack(**config_pack_label)
        
        self.btEditar.pack(padx=5,pady=5)
        self.btExcluir.pack(padx=5, pady=5)
    
                
    def aplicar_hover_color(self, event):

        mouse_x, mouse_y = self.winfo_pointerxy()
    
        frame_x = self.winfo_rootx()
        frame_y = self.winfo_rooty()
        
        frame_width = self.winfo_width()
        frame_height = self.winfo_height()
        
        if frame_x <= mouse_x < frame_x + frame_width and \
        frame_y <= mouse_y < frame_y + frame_height:
            self.configure(fg_color='#f3f6f4')
        else:
            self.configure(fg_color="#f2f2f2")
            
    def carregar_tela(self):
        self.pack(fill=ctk.X, padx=5, pady=(5))
        