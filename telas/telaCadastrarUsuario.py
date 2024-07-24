import customtkinter as ctk
from widgets.widgetAlerta import WidgetAlerta
import threading
from models.privilegio import Privilegio
from models.usuario import Usuario

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
        HEIGHT = 500
        POS_X = int((self.root.winfo_screenwidth() - WIDTH) / 2)
        POS_Y = int((self.root.winfo_screenheight() - HEIGHT) /2)
        self.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")
        
    def criar_widgets(self):
        config_label = {'text_color':'black', 'font':ctk.CTkFont('Inter', size=20)}
        config_entry = {'text_color':'black', 'font':ctk.CTkFont('Inter', weight='normal', size=20), 'fg_color':'#f2f2f2',
                              'border_color':'#f2f2f2', 'height':40}
        config_button = {'fg_color':'#0d6efd', 'font':ctk.CTkFont('Inter',weight='bold', size=20), 'height':40}
        
        config_combobox_chamado = {'height':40, 'fg_color':'#f2f2f2','font':ctk.CTkFont('Inter', weight='normal', size=15),
                                'text_color':'black', 'border_color':'#f2f2f2', 'state':'readonly',
                                'width':250,'button_color':'#0d6efd', 'dropdown_font':ctk.CTkFont('Inter', weight='normal', size=15)}
        
        
        self.carregar_dados()
        self.varPrivilegio= ctk.StringVar()
        self.varPrivilegio.set(self.privilegios[0])
   
        
        self.frMain  = ctk.CTkScrollableFrame(self, fg_color='white', bg_color='transparent', border_width=1, border_color='black', corner_radius=0)
        self.frMain.master = self.frMain._parent_canvas
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
        self.entryLoginUsuario.pack(padx=20, pady=(0,10), fill=ctk.BOTH, expand=True)
        self.lbSenhaUsuario.pack(anchor=ctk.W, padx=20, pady=(0,10))
        self.entrySenhaUsuario.pack(fill=ctk.X, padx=20, pady=0)
        self.lbPrivilegioChamado.pack(anchor=ctk.W, padx=20, pady=(0,10))
        self.cbPrivilegioChamado.pack(fill=ctk.X, padx=20, pady=(0,10))
        self.btCriar.pack(side=ctk.RIGHT, padx=20, pady=30)
        self.btCancelar.pack(side=ctk.RIGHT, padx=10, pady=30)
    
    def carregar_dados(self):
        self.privilegios = None
        try:
            self.privilegios = [x.nome_privilegio for x in Privilegio.select()]
        except Exception as e:
            print(f"Erro ao carregar dados do database: {e}")
    
    def criar_usuario(self):
        nome_usuario = self.entryNomeUsuario.get()
        login_usuario = self.entryLoginUsuario.get()
        senha_usuario = self.entrySenhaUsuario.get()
        privilegio_usuario = Privilegio.get(Privilegio.nome_privilegio == self.cbPrivilegioChamado.get())
        
        try:
            query = 1
            try:
                query = not(Usuario.get(Usuario.login_usuario == login_usuario))
            except Exception as e:
                pass
            if query:
                novo_usuario = Usuario(nome_usuario = nome_usuario, login_usuario=login_usuario,
                                   senha_usuario = senha_usuario, privilegio_usuario = privilegio_usuario)
                novo_usuario.save()
                try:
                    thead = threading.Thread(target=lambda : WidgetAlerta(self.root.frConteudo, f'Usuario {login_usuario} cadastrado com sucesso!', 'sucesso'))
                    thead.start()
                except Exception as e:
                    pass
                self.limpar_campos()
            else:
                try:
                    thead = threading.Thread(target=lambda : WidgetAlerta(self.root.frConteudo, f'O Usuario {login_usuario} já existe!', 'aviso'))
                    thead.start()
                except Exception as e:
                    pass
            
        except Exception as e:
                thead = threading.Thread(target=lambda : WidgetAlerta(self,'Ocorreu um erro ao cadastrar o usuarios!', 'erro'))
                thead.start()
            
    def limpar_campos(self):
        self.entryNomeUsuario.delete('0', ctk.END)
        self.entryLoginUsuario.delete('0', ctk.END)
        self.entrySenhaUsuario.delete('0', ctk.END)
    
    def fechar_tela(self):
        self.destroy()

        
        
        
        