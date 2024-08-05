import customtkinter as ctk
from tkinter import PhotoImage
from CTkMenuBar import CTkMenuBar, CustomDropdownMenu
from telas.telaNovoChamado import TelaNovoChamado
from telas.telaMeusChamados import TelaMeusChamados
from telas.telaGerenciarUsuarios import TelaGerenciarUsuarios
from telas.telaGerenciarSetores import TelaGerenciarSetor
from telas.telaGerenciarChamados import TelaGerenciarChamados
from telas.telaUsuario import TelaUsuario
from telas.telaMenuUsuario import TelaMenuUsuario
from telas.telaLogin import TelaLogin
from telas.telaCadastrarUsuario import TelaCadastrarUsuario
from telas.telaCadastrarSetor import TelaCadastrarSetor
from assets.icons.icone import iconMenu
from telas.telaAlerta import TelaAlerta
from models.model import Privilegio
from PIL import Image


class TelaPrincipal(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode('dark')
        self.telaLogin = None
        self.telaMenuUsuario = None
    
        
        self.PRIVILEGIO = None
        self.configurar_tela()
        self.exibir_telaLogin()
        self.bind('<Button-1>', self.fechar_menuUsuario)
        self.protocol("WM_DELETE_WINDOW", self.fechar_programa)
        self.mainloop()
        
    def fechar_programa(self):
        self.telaAlerta = TelaAlerta(self, 'Aviso - Fechamento do Programa',
                                     'Você clicou no botão de fechar o Programa! se você clicar em OK o programa será fechado',
                                     self.destroy)
        self.telaAlerta.grab_set()
        
    def configurar_tela(self):
        #DEFINIÇÃO DO TAMANHO MINIMO DA TELA
        WIDTH_MIN = self.winfo_screenwidth()-200
        HEIGHT_MIN = self.winfo_screenheight()-200
        self.minsize(WIDTH_MIN, HEIGHT_MIN)
        #MAXIMIZAÇÃO DA TELA
        self.after(0, lambda:self.state('zoomed'))
        #TITULO DA TELA
        self.title("HelpDesk")
        self.wm_iconbitmap('icone.ico')
    
    def criar_widgets(self):
        
        if self.PRIVILEGIO == 'Administrador':
            self.criar_menuAdmin()
        
        #VARIAVEIS RESPONSAVEIS POR MONITORAR O FUNCIONAMENTO DAS TELAS
        self.telaNovoChamado = None
        self.telaMeusChamados = None
        self.telaGerenciarChamados = None
        self.telaGerenciarUsuario = None
        self.telaGerenciarSetor = None
        self.telaUsuario = None
        #self.telaLoading = None
        
        #VARIAVEL RESPONSAVEL POR QUARDADOS OS DADOS DO USUARIO LOGADO
        self.usuario_logado = None
        
        #ESPECIFICAÇÃO DE ATRIBUTOS PADRÕES PARA BOTÕES
        config_button = {'fg_color':'transparent', 'bg_color':'transparent', 'hover_color':'#0d6efd',
                         'height':50, 'corner_radius':0, 'text_color':'black'}
        #CARREGAMENTO DO ICON MENU
        icon_menu = ctk.CTkImage(Image.open(iconMenu), size=(24,24))
        
        
        #CRIAÇÃO DOS FRAMES
        self.frMain = ctk.CTkFrame(self)
        self.frMain.grid_columnconfigure(0, weight=1)
        self.frMain.grid_columnconfigure(1, weight=100)
        self.frMain.grid_rowconfigure(0, weight=100)
        self.frMain.grid_rowconfigure(1, weight=0)
        
        self.frMenu = ctk.CTkFrame(self.frMain, fg_color='#0d6efd', bg_color='#0d6efd', corner_radius=0,
                                   width=350)
        self.frTituloMenu = ctk.CTkFrame(self.frMenu, fg_color='transparent', bg_color='transparent', corner_radius=0)
        #CRIAÇÃO DOS LABELS E BOTOÕES
        self.lbTituto = ctk.CTkLabel(self.frTituloMenu, text='helpdesk',
                                     font=ctk.CTkFont('Inter', weight='bold', size=30),
                                     text_color='black')
        
        self.btMenuUsuario = ctk.CTkButton(self.frTituloMenu, text='', corner_radius=0, image=icon_menu,
                                           width=40, height=40, bg_color='transparent', fg_color='transparent',
                                           hover=False,command= self.exibir_telaMenuUsuario)

        self.btMeusChamados = ctk.CTkButton(self.frMenu, text="Meus Chamados",
                                        font=ctk.CTkFont('Inter', size=20), **config_button, command=self.exibir_telaMeusChamados,
                                        anchor=ctk.W)
        self.btNovoChamado = ctk.CTkButton(self.frMenu, text='Abrir Novo Chamado', height=50, fg_color='#212529',
                                           font=ctk.CTkFont('Inter', weight='bold', size=22), command=self.exibir_telaNovoChamado)
        #CRIAÇÃO DO FRAME QUE CARREGARA OS DEMAIS CONTEUDOS DAS OUTRAS TELAS
        self.frConteudo = ctk.CTkFrame(self.frMain, fg_color='white',corner_radius=0, bg_color='white')
        self.frRodape = ctk.CTkFrame(self.frMain, bg_color='white', fg_color='white', height=100)
        
        self.lbNomeSistema = ctk.CTkLabel(self.frRodape, text="helpdesk", font=ctk.CTkFont("Inter", weight='bold', size=20),
                                     text_color='#0d6efd')
        self.lbCopyright = ctk.CTkLabel(self.frRodape, text="© 2024 Rafael. Todos os direitos reservados", font=ctk.CTkFont("Inter", weight='normal', size=17),
                                     text_color='gray')
        
        #CRIAÇÃO DO MENU DE USUARIO COM PRIVILEGIO SUPORTE OU ADMINISTRADOR
        if self.PRIVILEGIO in (Privilegio.get_privilegios_name()[:2]):
            self.btGerenciarChamados = ctk.CTkButton(self.frMenu, text="Gerenciar Chamados", **config_button,
                                        anchor=ctk.W,font=ctk.CTkFont('Inter', size=20),  command=lambda:self.exibir_telaGerenciarChamados())
        
    def carregar_widgets(self):
        self.frMain.pack(fill=ctk.BOTH, expand=True)
        self.frMenu.grid(column=0, row=0, rowspan=2, sticky=(ctk.W,ctk.E,ctk.S, ctk.N))
        self.frMenu.grid_propagate(0)
        self.frTituloMenu.pack(fill=ctk.X)
        self.frConteudo.grid(column=1, row=0, sticky=(ctk.W,ctk.E,ctk.S, ctk.N))
        self.frRodape.grid(row=1, column=1, sticky=(ctk.W,ctk.E,ctk.S, ctk.N))
        self.frRodape.grid_propagate(0)
        self.lbNomeSistema.pack(padx=5, pady=5, anchor=ctk.W)
        ctk.CTkFrame(self.frRodape, height=2, fg_color='gray').pack(fill=ctk.X, padx=5)
        self.lbCopyright.pack(padx=5, anchor=ctk.W)

        self.lbTituto.pack(pady=20, padx=(30,0), side=ctk.LEFT, anchor=ctk.W)
        self.btMenuUsuario.pack(side=ctk.RIGHT, anchor=ctk.E, padx=(0,30))
        self.btMenuUsuario.pack_propagate(0)
        if self.PRIVILEGIO not in ('Administrador', 'Suporte'):
            self.btMeusChamados.pack(fill=ctk.X, padx=30)
            self.btNovoChamado.pack(fill=ctk.X, padx=10,pady=10,side=ctk.BOTTOM)
            
        #CARREGAMENTO DO MENU DE USUARIO SUPORTE OU ADMINISTRADOR
        if self.PRIVILEGIO in (Privilegio.get_privilegios_name()[:2]):
            self.btGerenciarChamados.pack(fill=ctk.X, padx=30)
  
            
        
    def criar_menuAdmin(self):
        
        self.menu_adm = CTkMenuBar(self)
        self.menu_cadastrar = self.menu_adm.add_cascade('Cadastrar')
        self.menu_gerenciar = self.menu_adm.add_cascade('Gerenciar')
        self.menu_relatorio = self.menu_adm.add_cascade('Relatório')
                
        self.dropdown_cadastrar = CustomDropdownMenu(widget=self.menu_cadastrar)
        self.dropdown_cadastrar.add_option(option='Cadastrar Setor', command=self.exibir_telaCadastrarSetor)
        self.dropdown_cadastrar.add_option(option='Cadastrar Usuario', command=self.exibir_telaCadastrarUsuario)
        self.dropdown_gerenciar= CustomDropdownMenu(widget=self.menu_gerenciar)
        self.dropdown_gerenciar.add_option(option="Setores", command=self.exibir_telaGerenciarSetor)
        self.dropdown_gerenciar.add_option(option="Usuarios", command=self.exibir_telaGerenciarUsuario)
        self.dropdown_gerenciar.add_separator()
        self.dropdown_gerenciar.add_option(option='Deletar Chamado')

    
    def exibir_telaCadastrarUsuario(self):
        TelaCadastrarUsuario(self)
    
    def exibir_telaCadastrarSetor(self):
        TelaCadastrarSetor(self)
        
    def exibir_telaGerenciarUsuario(self, event=None):
        
        if self.telaGerenciarUsuario is None or not self.telaGerenciarUsuario.winfo_exists():
            self.limpar_frConteudo()
            self.telaGerenciarUsuario = TelaGerenciarUsuarios(self.frConteudo, self)
    
    def exibir_telaGerenciarSetor(self, event=None):
        
        if self.telaGerenciarSetor is None or not self.telaGerenciarSetor.winfo_exists():
            self.limpar_frConteudo()
            self.telaGerenciarSetor = TelaGerenciarSetor(self.frConteudo, self)
    
    def exibir_telaGerenciarChamados(self, event=None):
        
        if self.telaGerenciarChamados is None or not self.telaGerenciarChamados.winfo_exists():
            self.limpar_frConteudo()
            self.telaGerenciarChamados = TelaGerenciarChamados(self.frConteudo, self)
    
    def exibir_telaMeusChamados(self, event=None):
        
        if self.telaMeusChamados is None or not self.telaMeusChamados.winfo_exists():
            self.limpar_frConteudo()
            self.telaMeusChamados = TelaMeusChamados(self.frConteudo, self)
        #self.telaChamados = TelaMeusChamados(self.frConteudo, self, tipo)
        
            # process_thread = threading.Thread(target=self.criar_tela_chamado)
            # process_thread.start()
            # self.telaLoading = TelaLoading(self.frConteudo, self)
            #time.sleep(5)
            #self.telaLoading.stop_animation()
            #self.telaLoading.destroy()
            #self.telaChamados = TelaMeusChamados(self.frConteudo, self)
    # def criar_tela_chamado(self):
    #     time.sleep(3)
    #     self.telaLoading.destroy()
    #     self.telaChamados.carregar_tela()
           
    def exibir_telaNovoChamado(self):
        if self.telaNovoChamado is None or not self.telaNovoChamado.winfo_exists():
            self.limpar_frConteudo()
            self.telaNovoChamado = TelaNovoChamado(self.frConteudo, self)
        
    
    def exibir_telaLogin(self):

        if self.telaLogin is None:
            self.telaLogin = TelaLogin(self)
        elif not self.telaLogin.winfo_exists():
            
            for w in self.winfo_children():
                try:
                    w.destroy()
                except Exception as e:
                     pass
            self.telaLogin = TelaLogin(self)
           
            
    def exibir_telaUsuario(self):
        self.limpar_frConteudo()
        TelaUsuario(self.frConteudo, self, self.usuario_logado)

    def exibir_telaMenuUsuario(self):
        if self.telaMenuUsuario is None or not self.telaMenuUsuario.winfo_exists():
            self.telaMenuUsuario = TelaMenuUsuario(self, self.btMenuUsuario)
        

    def fechar_menuUsuario(self, event):
        if not(self.telaMenuUsuario is None) and self.telaMenuUsuario.winfo_exists() and event.widget != self.telaMenuUsuario:
            if self.telaMenuUsuario.winfo_viewable():
                self.telaMenuUsuario.destroy()
    
    def limpar_frConteudo(self):
        for tela in self.frConteudo.winfo_children():
            tela.destroy()