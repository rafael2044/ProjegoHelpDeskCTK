import customtkinter as ctk
from assets.icons.icone import iconLupa
from PIL import Image
from models.chamado import Chamado
from models.categoria import Categoria
from models.situacao import Situacao
from widgets.widgetChamado import WidgetChamado
from configure import PRIVILEGIOS

class TelaMeusChamados(ctk.CTkScrollableFrame):
    def __init__(self, master, root, tipo_chamado=1):
        super().__init__(master)
        self.tipo_chamado = tipo_chamado
        self.TIPOS = {1:"Chamados Enviados Por Mim", 2:'Todos os Chamados', 3:'Chamados Não Atendidos',4:'Atendido Por Mim'}
        self.master= self._parent_canvas
        self.root = root
        self.todosChamados = []
        self.MeusChamado = []
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
        self.frFiltroSituacao = ctk.CTkFrame(self.frPesquisa, bg_color='transparent', fg_color='transparent')
        self.frBusca = ctk.CTkFrame(self.frPesquisa, fg_color='transparent', height=50, border_color='black', 
                                    border_width=2, corner_radius=25)
    
        self.frConteudo = ctk.CTkFrame(self.frMain, bg_color='transparent', fg_color='transparent')
        self.frFiltroCategoria = ctk.CTkFrame(self.frConteudo, bg_color='transparent', fg_color='transparent', width=100)
        self.frChamados = ctk.CTkFrame(self.frConteudo, bg_color='transparent', fg_color='transparent')
        self.frRodape = ctk.CTkFrame(self.frMain, bg_color='transparent', fg_color='transparent')
        
        self.lbNomeSistema = ctk.CTkLabel(self.frRodape, text="helpdesk", font=ctk.CTkFont("Inter", weight='bold', size=20),
                                     text_color='#0d6efd')
        self.lbCopyright = ctk.CTkLabel(self.frRodape, text="© 2024 Rafael. Todos os direitos reservados", font=ctk.CTkFont("Inter", weight='normal', size=17),
                                     text_color='gray')
        
        self.lbTitulo = ctk.CTkLabel(self.frMain, text=self.TIPOS[self.tipo_chamado], font=ctk.CTkFont("Inter", weight='bold', size=30),
                                     **config_label)
        
        self.lbFiltroSituacao = ctk.CTkLabel(self.frPesquisa, text="Prioridade", font=ctk.CTkFont("Inter", weight='bold', size=15),
                                     text_color='gray')
        
        self.vbFiltroSituacao = ctk.StringVar()
        self.vbFiltroCategoria = ctk.StringVar()
            
        self.rbPendente = ctk.CTkRadioButton(self.frFiltroSituacao, text='Pendênte',**config_radioButton_filtro,
                                             value='Pendente', variable=self.vbFiltroSituacao, command=self.filtrar_chamados_situacao)
        self.rbConcluido = ctk.CTkRadioButton(self.frFiltroSituacao, text='Concluido', **config_radioButton_filtro,
                                              value='Concluido', variable=self.vbFiltroSituacao, command=self.filtrar_chamados_situacao)
        
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
        
        self.carregar_dados_chamados()
        
    def carregar_widgets(self):
        self.frMain.pack(expand=True, fill=ctk.BOTH, padx=10, pady=10)
        self.lbTitulo.pack(pady=(20,5))
        self.frPesquisa.pack(fill=ctk.X)
        self.frPesquisa.pack_propagate(0)
        self.lbFiltroSituacao.pack()
        self.frFiltroSituacao.pack()
        self.rbPendente.pack(side=ctk.LEFT)
        self.rbPendente.pack_propagate(0)
        self.rbConcluido.pack(side=ctk.LEFT, padx=10)
        self.rbConcluido.pack_propagate(0)
        self.frBusca.pack(fill=ctk.X, pady=10, padx=20)
        self.frBusca.pack_propagate(0)
        self.frConteudo.pack(fill=ctk.BOTH, expand=True)
        self.frFiltroCategoria.pack(fill=ctk.Y, side=ctk.LEFT)
        self.frChamados.pack(fill=ctk.BOTH, expand=True, side=ctk.LEFT)
        self.frRodape.pack(fill=ctk.X)

        self.lbImagemLupa.pack(side=ctk.LEFT, padx=(15,10), pady=10)
        self.entryBusca.pack(fill=ctk.BOTH,expand=True, side=ctk.LEFT, padx=(0,15), pady=10)
        
        self.lbFiltroCategoria.pack(anchor=ctk.W, padx=5)
        self.btFiltroSistema.pack(padx=10, pady=(5,0))
        self.btFiltroEquipamento.pack(padx=10, pady=(5,0))
        self.btFiltroSoftware.pack(padx=10,pady=(5,0))
        self.btFiltroRede.pack(padx=10,pady=5)
        
        self.carregar_chamados()
        
        self.lbNomeSistema.pack(padx=5, pady=5, anchor=ctk.W)
        ctk.CTkFrame(self.frRodape, height=2, fg_color='gray').pack(fill=ctk.X, padx=5)
        self.lbCopyright.pack(padx=5, anchor=ctk.W)
        
    def alterar_tipo_chamado(self, novo_tipo):
        self.tipo_chamado = novo_tipo
        self.carregar_chamados()
        
    def carregar_dados_chamados(self):
        query_chamado = Chamado.select()
        if self.root.PRIVILEGIO in (PRIVILEGIOS[1], PRIVILEGIOS[2]):
            self.MeusChamadoAtendidos = []
        for chamado in query_chamado:
            widget_chamado = WidgetChamado(self.frChamados, self.root, chamado)
            self.todosChamados.append(widget_chamado)
            if chamado.usuario_solicitante.nome_usuario == self.root.usuario_logado.nome_usuario:
                self.MeusChamado.append(widget_chamado)
            if self.root.PRIVILEGIO in (PRIVILEGIOS[1], PRIVILEGIOS[2]):
                if chamado.suporte_atendimento.nome_usuario == self.root.usuario_logado.nome_usuario:
                    self.MeusChamadoAtendidos.append(widget_chamado)
            
    def carregar_chamados(self):
        if self.rbPendente.cget('state') == 'disabled':
            self.rbPendente.configure(state=ctk.NORMAL)
        if self.rbConcluido.cget('state') == 'disabled':
            self.rbConcluido.configure(state=ctk.NORMAL)
        self.vbFiltroSituacao.set('')
        self.vbFiltroCategoria.set('')
        if self.frChamados.winfo_children():
            self.ocultar_chamados()
            
        if self.tipo_chamado == 1:
            for chamado in self.MeusChamado:
                chamado.carregar_tela()
        
        if self.tipo_chamado == 2:
            for chamado in self.todosChamados:
                chamado.carregar_tela()
        
        if self.tipo_chamado == 3:
            self.vbFiltroSituacao.set('Pendente')
            self.rbConcluido.configure(state=ctk.DISABLED)
            for chamado in self.todosChamados:
                if  chamado.chamado.situacao.nome_situacao == self.vbFiltroSituacao.get():
                    chamado.carregar_tela()
                    
        if self.tipo_chamado == 4:
            self.vbFiltroSituacao.set('Concluido')
            self.rbPendente.configure(state=ctk.DISABLED)
            for chamado in self.MeusChamadoAtendidos:
                chamado.carregar_tela()    
                    
        
    
    def ocultar_chamados(self):
        for chamado in self.todosChamados:
            if chamado.winfo_viewable():
                chamado.pack_forget()
    
    def filtrar_chamados_categoria(self):
        categoria = self.vbFiltroCategoria.get()
        situacao = self.vbFiltroSituacao.get()
        if self.tipo_chamado == 1:
            for chamado in self.MeusChamado:
                if chamado.winfo_viewable():
                    if not (chamado.chamado.categoria.nome_categoria == categoria and chamado.chamado.situacao.nome_situacao == situacao if \
                        not(situacao == '') else chamado.chamado.categoria.nome_categoria == categoria):
                        chamado.pack_forget()
                else:
                    if (chamado.chamado.categoria.nome_categoria == categoria and chamado.chamado.situacao.nome_situacao == situacao) if \
                        not(situacao == '') else chamado.chamado.categoria.nome_categoria == categoria:
                        chamado.carregar_tela()
                        
        elif self.tipo_chamado == 2:
            for chamado in self.todosChamados:
                if chamado.winfo_viewable():
                    print(situacao)
                    if not ((chamado.chamado.categoria.nome_categoria == categoria and chamado.chamado.situacao.nome_situacao == situacao) if \
                        not(situacao == '') else chamado.chamado.categoria.nome_categoria == categoria):
                            chamado.pack_forget()
                else:
                    if (chamado.chamado.categoria.nome_categoria == categoria and chamado.chamado.situacao.nome_situacao == situacao) if \
                        not(situacao == '') else (chamado.chamado.categoria.nome_categoria == categoria):
                            chamado.carregar_tela()
        elif self.tipo_chamado == 3:
            
            for chamado in self.todosChamados:
                if chamado.winfo_viewable():
                    if not (chamado.chamado.categoria.nome_categoria == categoria and chamado.chamado.situacao.nome_situacao == situacao):
                        chamado.pack_forget()
                else:
                    if chamado.chamado.categoria.nome_categoria == categoria and chamado.chamado.situacao.nome_situacao == situacao:
                        chamado.carregar_tela()
        
        elif self.tipo_chamado == 4:
            
            for chamado in self.MeusChamadoAtendidos:
                if chamado.winfo_viewable():
                    if not (chamado.chamado.categoria.nome_categoria == categoria and chamado.chamado.situacao.nome_situacao == situacao):
                        chamado.pack_forget()
                else:
                    if chamado.chamado.categoria.nome_categoria == categoria and chamado.chamado.situacao.nome_situacao == situacao:
                        chamado.carregar_tela()
                        
        if len(self.frChamados.winfo_children()) == 0:
            ctk.CTkLabel(self.frChamados, text='Nenhum Chamado Existente!', font=ctk.CTkFont("Inter", weight='bold', size=25),
                         text_color='gray').pack(anchor=ctk.S)
        
    def filtrar_chamados_situacao(self):
        categoria = self.vbFiltroCategoria.get()
        situacao = self.vbFiltroSituacao.get()
        if self.tipo_chamado == 1:
            for chamado in self.MeusChamado:
                if chamado.winfo_viewable():
                    if not (chamado.chamado.categoria.nome_categoria == categoria and chamado.chamado.situacao.nome_situacao == situacao if \
                        not (categoria == '') else chamado.chamado.situacao.nome_situacao == situacao):
                        chamado.pack_forget()
                else:
                    if chamado.chamado.categoria.nome_categoria == categoria and chamado.chamado.situacao.nome_situacao == situacao if\
                        not (categoria == '') else chamado.chamado.situacao.nome_situacao == situacao:
                        chamado.carregar_tela()
                        
        elif self.tipo_chamado == 2:
            for chamado in self.todosChamados:
                if chamado.winfo_viewable():
                    if not (chamado.chamado.categoria.nome_categoria == categoria and chamado.chamado.situacao.nome_situacao == situacao if \
                        not (categoria == '') else chamado.chamado.situacao.nome_situacao == situacao):
                        chamado.pack_forget()
                else:
                    if chamado.chamado.categoria.nome_categoria == categoria and chamado.chamado.situacao.nome_situacao == situacao if\
                        not (categoria == '') else chamado.chamado.situacao.nome_situacao == situacao:
                        chamado.carregar_tela()
        
        elif self.tipo_chamado == 3:
            for chamado in self.todosChamados:
                if chamado.winfo_viewable():
                    if not (chamado.chamado.categoria.nome_categoria == categoria and chamado.chamado.situacao.nome_situacao == situacao if \
                        not (categoria == '') else chamado.chamado.situacao.nome_situacao == situacao):
                        chamado.pack_forget()
                else:
                    if chamado.chamado.categoria.nome_categoria == categoria and chamado.chamado.situacao.nome_situacao == situacao if\
                        not (categoria == '') else chamado.chamado.situacao.nome_situacao == situacao:
                        chamado.carregar_tela()
        
        elif self.tipo_chamado == 4:
        
            for chamado in self.MeusChamadoAtendidos:
                if chamado.winfo_viewable():
                    if not (chamado.chamado.categoria.nome_categoria == categoria and chamado.chamado.situacao.nome_situacao == situacao if \
                        not (categoria == '') else chamado.chamado.situacao.nome_situacao == situacao):
                        chamado.pack_forget()
                else:
                    if chamado.chamado.categoria.nome_categoria == categoria and chamado.chamado.situacao.nome_situacao == situacao if\
                        not (categoria == '') else chamado.chamado.situacao.nome_situacao == situacao:
                        chamado.carregar_tela()
                        
        if len(self.frChamados.winfo_children()) == 0:
            ctk.CTkLabel(self.frChamados, text='Nenhum Chamado Existente!', font=ctk.CTkFont("Inter", weight='bold', size=25),
                         text_color='gray').pack(anchor=ctk.S)
            
    def limpar_frChamados(self):
        for w in self.frChamados.winfo_children():
            w.destroy()
        
    def carregar_tela(self):
        self.pack(fill=ctk.BOTH, expand=True)
