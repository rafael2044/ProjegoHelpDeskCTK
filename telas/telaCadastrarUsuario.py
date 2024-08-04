import customtkinter as ctk
from widgets.widgetAlerta import WidgetAlerta
from models.model import Privilegio
import threading
from crud import usuarioCRUD

class TelaCadastrarUsuario(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.root = master
        self.wm_overrideredirect(True)
        self.configurar_tela()
        self.criar_widgets()
        self.carregar_widgets()
        self.grab_set()
        
    def configurar_tela(self):
        self.configure(bg_color='transparent')
        self.update()
        WIDTH = 600
        HEIGHT = 600
        POS_X = int((self.root.winfo_screenwidth() - WIDTH) / 2)
        POS_Y = int((self.root.winfo_screenheight() - HEIGHT) /2)
        self.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")
        
    def criar_widgets(self):
        config_label = {'text_color':'black', 'font':ctk.CTkFont('Inter', size=20)}
        config_entry = {'text_color':'black', 'font':ctk.CTkFont('Inter', weight='normal', size=20), 'fg_color':'#f2f2f2',
                              'border_color':'#f2f2f2', 'height':40}
        config_button = {'fg_color':'#0d6efd', 'font':ctk.CTkFont('Inter',weight='bold', size=20), 'height':40}
        
        config_combobox_chamado = {'height':40, 'fg_color':'#f2f2f2','font':ctk.CTkFont('Inter', weight='normal', size=20),
                                'text_color':'black', 'border_color':'#f2f2f2', 'state':'readonly',
                                'width':250,'button_color':'#0d6efd', 'dropdown_font':ctk.CTkFont('Inter', weight='normal', size=20)}
        
        
        self.privilegios = Privilegio.get_privilegios_name()
        self.varPrivilegio= ctk.StringVar()
        self.varPrivilegio.set(self.privilegios[0])
   
        
        self.frMain  = ctk.CTkFrame(self, fg_color='white', bg_color='transparent', border_width=1, border_color='black', corner_radius=0)
        self.frTitulo = ctk.CTkFrame(self.frMain, fg_color='transparent', bg_color='transparent', height=20)
        
        self.btFechar = ctk.CTkButton(self.frTitulo, text='X',width=30, height=30, fg_color='transparent', bg_color='transparent',
                                      hover_color='gray', command=self.fechar_tela, border_color='black', border_width=2,
                                      text_color='black', font=ctk.CTkFont('Inter',weight='bold', size=20))
        
        self.lbTitulo = ctk.CTkLabel(self.frTitulo, text='Cadastrar Usuario', **config_label)
        self.lbNomeUsuario = ctk.CTkLabel(self.frMain, text='Nome do Usuario', **config_label)
        self.entryNomeUsuario  =ctk.CTkEntry(self.frMain,**config_entry)
    
        self.lbLoginUsuario = ctk.CTkLabel(self.frMain, text='Login do Usuario', **config_label)
        self.entryLoginUsuario = ctk.CTkEntry(self.frMain, **config_entry)
        
        self.lbSenhaUsuario = ctk.CTkLabel(self.frMain, text='Senha do Usuario', **config_label)
        self.entrySenhaUsuario = ctk.CTkEntry(self.frMain, **config_entry, show='*')

        self.lbPrivilegioChamado = ctk.CTkLabel(self.frMain, text='Privilégio do Usuario', **config_label)
        self.cbPrivilegioChamado = ctk.CTkComboBox(self.frMain, **config_combobox_chamado,values=self.privilegios, variable=self.varPrivilegio)
        
        self.btCancelar = ctk.CTkButton(self.frMain, text='Cancelar', command=self.fechar_tela, font= ctk.CTkFont('Inter',weight='bold', size=20),
                                        height=40, fg_color='white', hover_color='gray', text_color='black')
        self.btCriar = ctk.CTkButton(self.frMain, text='Criar', command=self.criar_usuario, **config_button)
        
    def carregar_widgets(self):
        self.frMain.pack(fill=ctk.BOTH, expand=True, padx=5, pady=5)
        self.frTitulo.pack(fill=ctk.X)
        self.lbTitulo.pack(side=ctk.LEFT,anchor=ctk.W, padx=20, pady=30, expand=True)
        self.btFechar.pack(side=ctk.LEFT, anchor=ctk.E, padx=10)
        self.btFechar.pack_propagate(0)
        self.lbNomeUsuario.pack(anchor=ctk.W, padx=20, pady=(0,10))
        self.entryNomeUsuario.pack(fill=ctk.X, padx=20, pady=(0,10))
        self.lbLoginUsuario.pack(anchor=ctk.W, padx=20, pady=(0,10), )
        self.entryLoginUsuario.pack(padx=20, pady=(0,10), fill=ctk.X)
        self.lbSenhaUsuario.pack(anchor=ctk.W, padx=20, pady=(0,10))
        self.entrySenhaUsuario.pack(fill=ctk.X, padx=20, pady=0)
        self.lbPrivilegioChamado.pack(anchor=ctk.W, padx=20, pady=(0,10))
        self.cbPrivilegioChamado.pack(fill=ctk.X, padx=20, pady=(0,10))
        self.btCriar.pack(side=ctk.RIGHT, padx=20, pady=30)
        self.btCancelar.pack(side=ctk.RIGHT, padx=10, pady=30)
    
    def criar_usuario(self):
        nome = self.entryNomeUsuario.get()
        usuario = self.entryLoginUsuario.get()
        senha = self.entrySenhaUsuario.get()
        privilegio = Privilegio.get_privilegio_id(self.cbPrivilegioChamado.get())
        
        try:
            retorno = usuarioCRUD.adicionar_usuario(nome, usuario, senha, privilegio)
            thead = threading.Thread(target=lambda : WidgetAlerta(self,retorno['mensagem'], retorno['tipo']))
            thead.start()
            if retorno['tipo'] == 'sucesso':
                self.entryNomeUsuario.delete('0', ctk.END)
                self.entryLoginUsuario.delete('0', ctk.END)
                self.entrySenhaUsuario.delete('0', ctk.END)
                
        except Exception as e:
                thead = threading.Thread(target=lambda : WidgetAlerta(self,'Ocorreu um erro ao cadastrar o usuarios!', 'erro'))
                thead.start()
            
    def limpar_campos(self):
        self.entryNomeUsuario.delete('0', ctk.END)
        self.entryLoginUsuario.delete('0', ctk.END)
        self.entrySenhaUsuario.delete('0', ctk.END)
    
    def fechar_tela(self):
        self.destroy()

        
        
        
        