import customtkinter as ctk
from assets.icons.icone import iconLupa
from PIL import Image
from widgets.widgetChamado import WidgetChamado
from crud import chamadoCRUD, atendimentoCRUD
from models.model import Privilegio

class TelaGerenciarChamados(ctk.CTkFrame):
    def __init__(self, master, root):
        super().__init__(master)
        self.root = root
        self.todosChamados = []
        self.todosAtendimentos = []
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
        config_radioButton_filtro = {'font':ctk.CTkFont("Inter", weight='normal', size=12),'text_color':'#333333'}
        icon_lupa = ctk.CTkImage(Image.open(iconLupa), size=(24,24))
        
        self.frMain = ctk.CTkFrame(self, bg_color='transparent', fg_color='transparent')
        self.frPesquisa = ctk.CTkFrame(self.frMain, bg_color='transparent', fg_color='transparent')
        self.frFiltroStatus = ctk.CTkFrame(self.frPesquisa, bg_color='transparent', fg_color='transparent')
        self.frBusca = ctk.CTkFrame(self.frPesquisa, fg_color='transparent', height=50, border_color='black', 
                                    border_width=2, corner_radius=25)
    
        self.frConteudo = ctk.CTkFrame(self.frMain, bg_color='transparent', fg_color='transparent')
        self.frFiltroCategoria = ctk.CTkFrame(self.frConteudo, bg_color='transparent', fg_color='transparent', width=100)
        self.frChamados = ctk.CTkScrollableFrame(self.frConteudo, bg_color='transparent', fg_color='transparent')
        self.frChamados.master = self.frChamados._parent_canvas
        
        self.lbTitulo = ctk.CTkLabel(self.frMain, text='Gerenciar Chamados', font=ctk.CTkFont("Inter", weight='bold', size=30),
                                     **config_label)
        
        self.lbFiltroStatus = ctk.CTkLabel(self.frPesquisa, text="Prioridade", font=ctk.CTkFont("Inter", weight='bold', size=15),
                                     text_color='gray')
        
        self.vbFiltroStatus = ctk.StringVar()
        self.vbFiltroCategoria = ctk.StringVar()
            
        self.rbPendente = ctk.CTkRadioButton(self.frFiltroStatus, text='Pendênte',**config_radioButton_filtro,
                                             value='Pendente', variable=self.vbFiltroStatus, command=self.filtrar_chamados_status)
        self.rbConcluido = ctk.CTkRadioButton(self.frFiltroStatus, text='Concluido', **config_radioButton_filtro,
                                              value='Concluido', variable=self.vbFiltroStatus, command=self.filtrar_chamados_status)
        
        self.lbImagemLupa = ctk.CTkLabel(self.frBusca, text='', image=icon_lupa)
        self.entryBusca = ctk.CTkEntry(self.frBusca, placeholder_text="Digite aqui o título do chamado", height=40,
                                       font=ctk.CTkFont('Inter', weight='normal', size=15), text_color='black', fg_color='transparent',
                                       bg_color='transparent', border_color='white')
        self.lbFiltroCategoria = ctk.CTkLabel(self.frFiltroCategoria, text="Categoria", font=ctk.CTkFont("Inter", weight='bold', size=15),
                                     text_color='gray') 
        self.btFiltroSistema = ctk.CTkRadioButton(self.frFiltroCategoria, text='Sistema', **config_radioButton_filtro,
                                              value='Sistema', variable=self.vbFiltroCategoria, command=self.filtrar_chamados_categoria)
        self.btFiltroEquipamento = ctk.CTkRadioButton(self.frFiltroCategoria, text='Equipamento', **config_radioButton_filtro,
                                              value='Equipamento', variable=self.vbFiltroCategoria, command=self.filtrar_chamados_categoria)
        self.btFiltroSoftware = ctk.CTkRadioButton(self.frFiltroCategoria, text='Software', **config_radioButton_filtro,
                                              value='Software', variable=self.vbFiltroCategoria, command=self.filtrar_chamados_categoria)
        self.btFiltroRede = ctk.CTkRadioButton(self.frFiltroCategoria, text='Internet', **config_radioButton_filtro,
                                              value='Internet', variable=self.vbFiltroCategoria, command=self.filtrar_chamados_categoria)
        
        self.consultar_chamados()
        
    def carregar_widgets(self):
        self.frMain.pack(fill=ctk.BOTH, expand=True)
        self.lbTitulo.pack(pady=(20,5))
        self.frPesquisa.pack(fill=ctk.X)
        self.frPesquisa.pack_propagate(0)
        self.lbFiltroStatus.pack()
        self.frFiltroStatus.pack()
        self.rbPendente.pack(side=ctk.LEFT)
        self.rbPendente.pack_propagate(0)
        self.rbConcluido.pack(side=ctk.LEFT, padx=10)
        self.rbConcluido.pack_propagate(0)
        self.frBusca.pack(fill=ctk.X, pady=10, padx=20)
        self.frBusca.pack_propagate(0)
        self.frConteudo.pack(fill=ctk.BOTH, expand=True)
        self.frFiltroCategoria.pack(fill=ctk.Y, side=ctk.LEFT)
        self.frChamados.pack(fill=ctk.BOTH, expand=True, side=ctk.LEFT)

        self.lbImagemLupa.pack(side=ctk.LEFT, padx=(15,10), pady=10)
        self.entryBusca.pack(fill=ctk.BOTH,expand=True, side=ctk.LEFT, padx=(0,15), pady=10)
        
        self.lbFiltroCategoria.pack(anchor=ctk.W, padx=5)
        self.btFiltroSistema.pack(padx=10, pady=(5,0))
        self.btFiltroEquipamento.pack(padx=10, pady=(5,0))
        self.btFiltroSoftware.pack(padx=10,pady=(5,0))
        self.btFiltroRede.pack(padx=10,pady=5)
        
        self.carregar_chamados()
        
    def consultar_chamados(self):
        self.todosChamados= []
        self.MeusChamadoAtendidos = []
        chamados = chamadoCRUD.selecionar_todos_chamados()
        atendimentos = atendimentoCRUD.selecionar_todos_atendimentos()
        for chamado in chamados:
            self.todosChamados.append(WidgetChamado(self.frChamados, self.root, chamado))
            
        for atendimento in atendimentos:
            self.todosAtendimentos.append(WidgetChamado(self.frChamados, self.root, atendimento.chamado))
            
    def carregar_chamados(self):
        if self.rbPendente.cget('state') == 'disabled':
            self.rbPendente.configure(state=ctk.NORMAL)
        if self.rbConcluido.cget('state') == 'disabled':
            self.rbConcluido.configure(state=ctk.NORMAL)
        self.vbFiltroStatus.set('')
        self.vbFiltroCategoria.set('')
        
        if self.frChamados.winfo_children():
            self.ocultar_chamados()
            
        for chamado in self.todosChamados:
            chamado.carregar_tela()
                
        
    def limpar_frChamados(self):
        for w in self.frChamados.winfo_children():
            w.destroy()
            
    def ocultar_chamados(self):
        for chamado in self.todosChamados:
            if chamado.winfo_viewable():
                chamado.pack_forget()
    
    def filtrar_chamados_categoria(self):
        categoria = self.vbFiltroCategoria.get()
        status = self.vbFiltroStatus.get()
                        
        for chamado in self.todosChamados:
            if chamado.winfo_viewable():
                print(status)
                if not ((chamado.chamado.get_categoria() == categoria and chamado.chamado.get_status() == status) if \
                    not(status == '') else chamado.chamado.get_categoria() == categoria):
                        chamado.pack_forget()
            else:
                if (chamado.chamado.get_categoria() == categoria and chamado.chamado.get_status() == status) if \
                    not(status == '') else (chamado.chamado.get_categoria() == categoria):
                        chamado.carregar_tela()
                        
        if len(self.frChamados.winfo_children()) == 0:
            ctk.CTkLabel(self.frChamados, text='Nenhum Chamado Existente!', font=ctk.CTkFont("Inter", weight='bold', size=25),
                         text_color='gray').pack(anchor=ctk.S)
        
    def filtrar_chamados_status(self):
        categoria = self.vbFiltroCategoria.get()
        status = self.vbFiltroStatus.get()
                        
        for chamado in self.todosChamados:
            if chamado.winfo_viewable():
                if not (chamado.chamado.get_categoria() == categoria and chamado.chamado.get_status() == status if \
                    not (categoria == '') else chamado.chamado.get_status() == status):
                    chamado.pack_forget()
            else:
                if chamado.chamado.get_categoria() == categoria and chamado.chamado.get_status() == status if\
                    not (categoria == '') else chamado.chamado.get_status() == status:
                    chamado.carregar_tela()
        

        if len(self.frChamados.winfo_children()) == 0:
            ctk.CTkLabel(self.frChamados, text='Nenhum Chamado Existente!', font=ctk.CTkFont("Inter", weight='bold', size=25),
                         text_color='gray').pack(anchor=ctk.S)
            
    def limpar_frChamados(self):
        for w in self.frChamados.winfo_children():
            w.destroy()
        
    def carregar_tela(self):
        self.pack(fill=ctk.BOTH, expand=True)
