import customtkinter as ctk
from widgets.widgetAlerta import WidgetAlerta
import threading
from crud import atendimentoCRUD
from models.model import Categoria, Prioridade
import pywinstyles

class TelaAtenderChamado(ctk.CTkToplevel):
    def __init__(self, master, chamado):
        super().__init__(master)
        self.root = master
        self.wm_overrideredirect(True)
        self.chamado = chamado
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
        config_entry = {'text_color':'black', 'font':ctk.CTkFont('Inter', weight='normal', size=20), 'fg_color':'white',
                        'height':40}
        config_button = {'fg_color':'#0d6efd', 'font':ctk.CTkFont('Inter',weight='bold', size=20), 'height':40}
        
        config_combobox_chamado = {'height':40, 'fg_color':'#f2f2f2','font':ctk.CTkFont('Inter', weight='normal', size=15),
                                'text_color':'black', 'state':'readonly',
                                'width':250,'button_color':'#0d6efd', 'dropdown_font':ctk.CTkFont('Inter', weight='normal', size=15)}
        
        config_textbox_chamado = {'fg_color':'white','font':ctk.CTkFont('Inter', weight='normal', size=15),
                                  'text_color':'black'}
        
        self.varCategoria = ctk.StringVar()
        self.varCategoria.set(self.chamado.get_categoria())
        self.varPrioridade = ctk.StringVar()
        self.varPrioridade.set(self.chamado.get_prioridade())
        
        self.frMain  = ctk.CTkFrame(self, fg_color='#ced4da', bg_color='#000001', corner_radius=20)
        self.frMain.pack(fill=ctk.BOTH, expand=True, padx=5, pady=5)
        pywinstyles.set_opacity(self.frMain, color='#000001')
        pywinstyles.apply_style(self, 'transparent')
        self.frConteudo = ctk.CTkScrollableFrame(self.frMain, fg_color='transparent', bg_color='transparent', corner_radius=0)
        self.frConteudo.master = self.frConteudo._parent_canvas
        self.frBottom = ctk.CTkFrame(self.frMain, fg_color='transparent', bg_color='transparent', height=40,corner_radius=0)
        self.frTitulo = ctk.CTkFrame(self.frMain, fg_color='transparent', bg_color='transparent', height=20,corner_radius=0)
        
        self.btFechar = ctk.CTkButton(self.frTitulo, text='X',width=30, height=30, fg_color='transparent', bg_color='transparent',
                                      hover_color='#dc3545', command=self.fechar_tela, border_color='black', border_width=2,
                                      text_color='black', font=ctk.CTkFont('Inter',weight='bold', size=20))
        
        self.lbTitulo = ctk.CTkLabel(self.frTitulo, text='Atender Chamado', **config_label)
        self.lbTituloChamado = ctk.CTkLabel(self.frConteudo, text='Titulo do Chamado', **config_label)
        self.entryTituloChamado  =ctk.CTkEntry(self.frConteudo,**config_entry)
        self.entryTituloChamado.insert('0', self.chamado.titulo)
        self.entryTituloChamado.configure(state=ctk.DISABLED)
        self.lbDetalhesChamado = ctk.CTkLabel(self.frConteudo, text='Detalhes do Chamado', **config_label)
        self.tbDetalhesChamado = ctk.CTkTextbox(self.frConteudo, **config_textbox_chamado)
        self.tbDetalhesChamado.insert('0.0', self.chamado.detalhes)
        self.tbDetalhesChamado.configure(state=ctk.DISABLED)
        self.lbCategoriaChamado = ctk.CTkLabel(self.frConteudo, text='Categoria do Chamado', **config_label)
        self.cbCategoriaChamado = ctk.CTkComboBox(self.frConteudo, **config_combobox_chamado,values=Categoria.get_categorias_name(), variable=self.varCategoria)
        self.cbCategoriaChamado.configure(state=ctk.DISABLED)
        self.lbPrioridadeChamado = ctk.CTkLabel(self.frConteudo, text='Prioridade do Chamado', **config_label)
        self.cbPrioridadeChamado = ctk.CTkComboBox(self.frConteudo, **config_combobox_chamado,values=Prioridade.get_prioridades_name(), variable=self.varPrioridade)
        self.cbPrioridadeChamado.configure(state=ctk.DISABLED)
        self.lbDetalhesAtendimento = ctk.CTkLabel(self.frConteudo, text='Detalhes do Atendimento', **config_label)
        self.tbDetalhesAtendimento = ctk.CTkTextbox(self.frConteudo, **config_textbox_chamado)
        
        self.btCancelar = ctk.CTkButton(self.frBottom, text='Cancelar', command=self.fechar_tela, font= ctk.CTkFont('Inter',weight='bold', size=20),
                                        height=40, fg_color='transparent', hover_color='#dc3545', text_color='black')
        self.btFinalizar = ctk.CTkButton(self.frBottom, text='Finalizar', command=self.atender_chamado, **config_button)
        
    def carregar_widgets(self):
        
        self.frTitulo.pack(fill=ctk.X, padx=5, pady=5)
        self.lbTitulo.pack(side=ctk.LEFT,anchor=ctk.W, padx=20, pady=10, expand=True)
        self.btFechar.pack(side=ctk.LEFT, anchor=ctk.E, padx=10)
        self.btFechar.pack_propagate(0)
        self.frConteudo.pack(fill= ctk.BOTH, expand=True, padx=5, pady=(0,5))
        self.lbTituloChamado.pack(anchor=ctk.W, padx=20, pady=(0,10))
        self.entryTituloChamado.pack(fill=ctk.X, padx=20, pady=(0,10))
        self.lbDetalhesChamado.pack(anchor=ctk.W, padx=20, pady=(0,10), )
        self.tbDetalhesChamado.pack(padx=20, pady=(0,10), fill=ctk.BOTH, expand=True)
        self.lbCategoriaChamado.pack(anchor=ctk.W, padx=20, pady=(0,10))
        self.cbCategoriaChamado.pack(fill=ctk.X, padx=20, pady=(0,10))
        self.lbPrioridadeChamado.pack(anchor=ctk.W, padx=20, pady=(0,10))
        self.cbPrioridadeChamado.pack(fill=ctk.X, padx=20, pady=(0,10))
        self.lbDetalhesAtendimento.pack(anchor=ctk.W, padx=20, pady=(0,10))
        self.tbDetalhesAtendimento.pack(fill=ctk.BOTH, expand=True, padx=20, pady=(0,10))
        self.frBottom.pack(fill=ctk.X, padx=5, pady=(0,5))

        self.btFinalizar.pack(side=ctk.RIGHT, padx=20, pady=5)
        self.btCancelar.pack(side=ctk.RIGHT, padx=10, pady=5)
    
    def atender_chamado(self):
        id_chamado = self.chamado.id
        suporte = self.root.usuario_logado.id
        detalhes = self.tbDetalhesAtendimento.get('0.0', ctk.END)
        
        retorno = atendimentoCRUD.atender_chamado_id(id_chamado, suporte, detalhes)
        thead = threading.Thread(target=lambda : WidgetAlerta(self.master, retorno.get('mensagem'),retorno.get('tipo')))
        thead.start()
        if retorno.get('tipo') == 'sucesso':
            self.master.telaGerenciarChamados.limpar_frChamados()
            self.master.telaGerenciarChamados.consultar_chamados()
            self.master.telaGerenciarChamados.carregar_chamados()
            self.fechar_tela()
            
    def fechar_tela(self):
        self.destroy()

        
        
        
        