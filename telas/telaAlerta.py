import customtkinter as ctk

class TelaAlerta(ctk.CTkToplevel):
    def __init__(self, root, titulo_alerta, mensagem_alerta, acao_ok=None, tipo='alerta'):
        super().__init__(master=root, fg_color='#f2f2f2')
        self.root=root
        self.titulo_alerta = titulo_alerta
        self.mensagem_alerta = mensagem_alerta
        self.acao_ok = acao_ok
        self.configurar_tela()
        self.criar_widgets()
        self.carregar_widgets()
        self.centralizar_tela()
        
    def configurar_tela(self):
        self.configure(height=100)
        self.title(self.titulo_alerta)
    
    def centralizar_tela(self):
        WIN_WIDTH = self.winfo_screenwidth()
        WIN_HEIGHT = self.winfo_screenheight()
        self.update()
        WIDTH = self.winfo_width()
        HEIGHT = self.winfo_height()
        POS_X = int((WIN_WIDTH/2)-(WIDTH / 2 ))
        POS_Y = int((WIN_HEIGHT/2)-(HEIGHT/2))
        self.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")
        self.update()
        self.focus_force()
        
    def criar_widgets(self):
        self.lbMensagem = ctk.CTkLabel(self, text=self.mensagem_alerta, wraplength=300, 
                                       font=ctk.CTkFont('Inter', size=20), text_color='black')
        
        self.frButtons = ctk.CTkFrame(self, bg_color='transparent', fg_color='transparent')
        self.btCancelar = ctk.CTkButton(self.frButtons, text='Cancelar', font=ctk.CTkFont('Inter', weight='bold', size=20),
                                        command=self.fechar_alerta, fg_color='#0d6efd')
        self.btSim = ctk.CTkButton(self.frButtons, text='Ok', font=ctk.CTkFont('Inter', weight='bold', size=20),
                                   command=self.acao_ok if self.acao_ok is not None else self.destroy, fg_color='#0d6efd')
    
    def carregar_widgets(self):
        self.lbMensagem.pack(fill=ctk.X, padx=20, pady=20)
        self.frButtons.pack()
        self.btSim.pack(side=ctk.LEFT, fill=ctk.X,padx=(20,10), pady=(0,20))
        self.btCancelar.pack(side=ctk.LEFT, fill=ctk.X, padx=(0,20), pady=(0,20))
    
    def fechar_alerta(self):
        self.destroy()
        
     
    