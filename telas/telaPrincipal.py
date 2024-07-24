import customtkinter as ctk
from tkinter import PhotoImage
from CTkMenuBar import CTkMenuBar, CustomDropdownMenu
from telas.telaNovoChamado import TelaNovoChamado
from telas.telaMeusChamados import TelaMeusChamados
from telas.telaGerenciarUsuarios import TelaGerenciarUsuarios
from telas.telaUsuario import TelaUsuario
from telas.telaMenuUsuario import TelaMenuUsuario
from telas.telaLogin import TelaLogin
from telas.telaCadastrarUsuario import TelaCadastrarUsuario
from telas.telaCadastrarSetor import TelaCadastrarSetor
from assets.icons.icone import iconMenu
from telas.telaAlerta import TelaAlerta
from PIL import Image
from configure import PRIVILEGIOS

TIPOS_CHAMADOS = ((1,'Meus'), ('2', 'Todos'),
                  (3, 'NaoAtendidos'),(4,'AtendidosPorMim'))

class TelaPrincipal(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode('dark')
        self.telaLogin = None
        self.telaMenuUsuario = None
    
        
        self.PRIVILEGIO = None
        self.configurar_tela()
        self.carregar_tela_login()
        self.bind('<Button-1>', self.fechar_menu_usuario)
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
            self.criar_menu_admin()
        
        #VARIAVEIS RESPONSAVEIS POR MONITORAR O FUNCIONAMENTO DAS TELAS
        self.telaNovoChamado = None
        self.telaChamados = None
        self.telaGerenciarUsuario = None
        self.telaUsuario = None
        #self.telaLoading = None
        
        #VARIAVEL RESPONSAVEL POR QUARDADOS OS DADOS DO USUARIO LOGADO
        self.usuario_logado = None
        
        #ESPECIFICAÇÃO DE ATRIBUTOS PADRÕES PARA BOTÕES
        config_button = {'fg_color':'transparent', 'bg_color':'transparent', 'hover_color':'#A0B7D5',
                         'height':50, 'corner_radius':0, 'text_color':'black'}
        #CARREGAMENTO DO ICON MENU
        icon_menu = ctk.CTkImage(Image.open(iconMenu), size=(24,24))
        
        #CRIAÇÃO DOS FRAMES
        self.frMain = ctk.CTkFrame(self)
        self.frMenu = ctk.CTkFrame(self.frMain, fg_color='#A0B7D5', bg_color='#A0B7D5', corner_radius=0,
                                   width=350)
        self.frTituloMenu = ctk.CTkFrame(self.frMenu, fg_color='transparent', bg_color='transparent', corner_radius=0)
        #CRIAÇÃO DOS LABELS E BOTOÕES
        self.lbTituto = ctk.CTkLabel(self.frTituloMenu, text='helpdesk',
                                     font=ctk.CTkFont('Inter', weight='bold', size=30),
                                     text_color='black')
        
        self.btMenuUsuario = ctk.CTkButton(self.frTituloMenu, text='', corner_radius=0, image=icon_menu,
                                           width=40, height=40, bg_color='transparent', fg_color='transparent',
                                           hover=False,command= self.carregar_tela_menuUsuario)

        self.btChamados = ctk.CTkButton(self.frMenu, text="Meus Chamados",
                                        font=ctk.CTkFont('Inter', size=20), **config_button, command=self.carregar_tela_chamados,
                                        anchor=ctk.W)
        self.btNovoChamado = ctk.CTkButton(self.frMenu, text='Abrir Novo Chamado', height=40, fg_color='#0d6efd',
                                           font=ctk.CTkFont('Inter', weight='bold', size=20), command=self.carregar_tela_novo_chamado)
        #CRIAÇÃO DO FRAME QUE CARREGARA OS DEMAIS CONTEUDOS DAS OUTRAS TELAS
        self.frConteudo = ctk.CTkFrame(self.frMain, fg_color='#f2f2f2',corner_radius=0, bg_color='#f2f2f2')

        #CRIAÇÃO DO MENU DE USUARIO COM PRIVILEGIO SUPORTE OU ADMINISTRADOR
        if self.PRIVILEGIO in (PRIVILEGIOS[1], PRIVILEGIOS[2]):
            config_button_gerenciar = {'fg_color':'transparent', 'bg_color':'transparent', 'hover_color':'#A0B7D5',
                         'height':50, 'corner_radius':0, 'text_color':'black', 'font':ctk.CTkFont('Inter', size=17)}
            self.frMenuGerenciar = ctk.CTkFrame(self.frMenu, bg_color='transparent', fg_color='transparent',
                                                cursor='hand2')
            self.lbMenuGerenciar = ctk.CTkLabel(self.frMenuGerenciar, text='Gerenciar Chamados', font=ctk.CTkFont('inter', size=20),
                                                text_color='black')
            self.btTodosChamados = ctk.CTkButton(self.frMenuGerenciar, text="Todos", **config_button_gerenciar,
                                        anchor=ctk.W, command=lambda:self.carregar_tela_chamados(2))
            self.btChamadosNAtendidos = ctk.CTkButton(self.frMenuGerenciar, text="Não Atendidos",
                                        **config_button_gerenciar,
                                        anchor=ctk.W, command=lambda:self.carregar_tela_chamados(3))
            self.btChamadosAtendidos = ctk.CTkButton(self.frMenuGerenciar, text="Atendidos por mim",
                                        **config_button_gerenciar,
                                        anchor=ctk.W, command=lambda:self.carregar_tela_chamados(4))
        
    def carregar_widgets(self):
        self.frMain.pack(fill=ctk.BOTH, expand=True)
        self.frMenu.pack(fill=ctk.Y, side=ctk.LEFT)
        self.frMenu.pack_propagate(0)
        self.frTituloMenu.pack(fill=ctk.X)
        self.frConteudo.pack(fill=ctk.BOTH, expand=True, side=ctk.LEFT)

        self.lbTituto.pack(pady=20, padx=(30,0), side=ctk.LEFT, anchor=ctk.W)
        self.btMenuUsuario.pack(side=ctk.RIGHT, anchor=ctk.E, padx=(0,30))
        self.btMenuUsuario.pack_propagate(0)
        if self.PRIVILEGIO not in ('Administrador', 'Suporte'):
            self.btChamados.pack(fill=ctk.X, padx=30)
        
        #CARREGAMENTO DO MENU DE USUARIO SUPORTE OU ADMINISTRADOR
        if self.PRIVILEGIO in (PRIVILEGIOS[1], PRIVILEGIOS[2]):
            self.frMenuGerenciar.pack(fill=ctk.X, padx=0)
            self.lbMenuGerenciar.pack(anchor=ctk.W, padx=30)
            self.frMenuGerenciar.bind('<Button-1>', self.carregar_menu_gerenciarChamados)
            self.lbMenuGerenciar.bind('<Button-1>', self.carregar_menu_gerenciarChamados)
        if self.PRIVILEGIO not in ('Administrador', 'Suporte'):    
            self.btNovoChamado.pack(fill=ctk.X, padx=30,pady=10,side=ctk.BOTTOM)
        
    def criar_menu_admin(self):
        
        self.menu_adm = CTkMenuBar(self)
        self.menu_cadastrar = self.menu_adm.add_cascade('Cadastrar')
        self.menu_gerenciar = self.menu_adm.add_cascade('Gerenciar')
        self.menu_relatorio = self.menu_adm.add_cascade('Relatório')
                
        self.dropdown_cadastrar = CustomDropdownMenu(widget=self.menu_cadastrar)
        self.dropdown_cadastrar.add_option(option='Cadastrar Setor', command=self.carregar_tela_cadastrarSetor)
        self.dropdown_cadastrar.add_option(option='Cadastrar Usuario', command=self.carregar_tela_cadastrarUsuario)
        self.dropdown_gerenciar= CustomDropdownMenu(widget=self.menu_gerenciar)
        self.dropdown_gerenciar.add_option(option="Setores")
        self.dropdown_gerenciar.add_option(option="Usuarios", command=self.carregar_tela_gerenciarUsuarios)
        self.dropdown_gerenciar.add_separator()
        self.dropdown_gerenciar.add_option(option='Deletar Chamado')

    
    def carregar_tela_cadastrarUsuario(self):
        TelaCadastrarUsuario(self)
    
    def carregar_tela_cadastrarSetor(self):
        TelaCadastrarSetor(self)
        
    def carregar_tela_gerenciarUsuarios(self, event=None):
        
        if self.telaGerenciarUsuario is None or not self.telaGerenciarUsuario.winfo_exists():
            self.limpar_frConteudo()
            self.telaGerenciarUsuario = TelaGerenciarUsuarios(self.frConteudo, self)
    
    def carregar_tela_chamados(self, tipo_chamado=1):
        
        if self.telaChamados is None or not self.telaChamados.winfo_exists():
            self.limpar_frConteudo()
            self.telaChamados = TelaMeusChamados(self.frConteudo, self, tipo_chamado)
        elif self.telaChamados.winfo_viewable():
            if tipo_chamado != self.telaChamados.tipo_chamado:
                self.telaChamados.alterar_tipo_chamado(tipo_chamado)
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
           
    def carregar_tela_novo_chamado(self):
        if self.telaNovoChamado is None or not self.telaNovoChamado.winfo_exists():
            self.limpar_frConteudo()
            self.telaNovoChamado = TelaNovoChamado(self.frConteudo, self)
        
    
    def carregar_tela_login(self):

        if self.telaLogin is None:
            self.telaLogin = TelaLogin(self)
        elif not self.telaLogin.winfo_exists():
            
            for w in self.winfo_children():
                try:
                    w.destroy()
                except Exception as e:
                     pass
            self.telaLogin = TelaLogin(self)
           
            
    def carregar_tela_usuario(self):
        self.limpar_frConteudo()
        TelaUsuario(self.frConteudo, self, self.usuario_logado)

    def carregar_tela_menuUsuario(self):
        if self.telaMenuUsuario is None or not self.telaMenuUsuario.winfo_exists():
            self.telaMenuUsuario = TelaMenuUsuario(self, self.btMenuUsuario)
        

    def fechar_menu_usuario(self, event):
        if not(self.telaMenuUsuario is None) and self.telaMenuUsuario.winfo_exists() and event.widget != self.telaMenuUsuario:
            if self.telaMenuUsuario.winfo_viewable():
                self.telaMenuUsuario.destroy()
                
    def carregar_menu_gerenciarChamados(self,event):
        if not self.btTodosChamados.winfo_viewable():
            self.expandir_menu_gerenciar_chamados()
        else:
            self.ocultar_menu_gerenciar_chamados()
    
    def expandir_menu_gerenciar_chamados(self):
        self.btTodosChamados.pack(fill=ctk.X, padx=40)
        self.btChamadosNAtendidos.pack(fill=ctk.X, padx=40)
        self.btChamadosAtendidos.pack(fill=ctk.X, padx=40)
    
    def ocultar_menu_gerenciar_chamados(self):
        self.btTodosChamados.pack_forget()
        self.btChamadosNAtendidos.pack_forget()
        self.btChamadosAtendidos.pack_forget()
    
    def limpar_frConteudo(self):
        for tela in self.frConteudo.winfo_children():
            tela.destroy()