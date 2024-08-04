import customtkinter as ctk
from PIL import Image
from assets.imagens.image import imgInternet,imgEquipamento, imgSistema, imgSoftware
from crud import setorCRUD, chamadoCRUD
from models.model import Categoria, Prioridade
from widgets.widgetAlerta import WidgetAlerta
import threading

class TelaNovoChamado(ctk.CTkScrollableFrame):
    def __init__(self, master, root):
        super().__init__(master)
        self.master= self._parent_canvas #Corrige o bug do scroll
        self.root = root
        self.configurar_tela()
        self.criar_widgets()
        self.carregar_widgets()
        self.carregar_tela()
    

    def configurar_tela(self):
        self.configure(bg_color='white')
        self.configure(fg_color='white')
        self.configure(corner_radius=0)
        
        
    def criar_widgets(self):
        config_label = {'text_color':'black'}
        self.frMain = ctk.CTkFrame(self, bg_color='white', fg_color='white')
        self.lbTitulo = ctk.CTkLabel(self.frMain, text="T.I Help Desk", font=ctk.CTkFont("Inter", weight='bold', size=30),
                                     **config_label)
        self.lbInstrucoes = ctk.CTkLabel(self.frMain, text="Olá, aqui estão as coisas em que podemos ajudá-lo",
                                        font=ctk.CTkFont("Inter", weight='normal', size=15),**config_label)
        
        
        config_frame_ajuda = {'height':200, 'bg_color':'transparent', 'fg_color':'transparent'}
        config_label_ajuda = {'font':ctk.CTkFont("Inter", weight='bold', size=15), **config_label}
        config_label_detalhes = {'font':ctk.CTkFont("Inter", weight='normal', size=15), **config_label}
        img_sistema= ctk.CTkImage(Image.open(imgSistema), size=(64,64))
        img_equipamento= ctk.CTkImage(Image.open(imgEquipamento), size=(64,64))
        img_software= ctk.CTkImage(Image.open(imgSoftware), size=(64,64))
        img_internet = ctk.CTkImage(Image.open(imgInternet), size=(64,64))
        
        
        self.frAjuda = ctk.CTkFrame(self.frMain, bg_color='transparent', fg_color='transparent')
        self.frAjudaSistema = ctk.CTkFrame(self.frAjuda, **config_frame_ajuda)
        
        self.lbSistema = ctk.CTkLabel(self.frAjudaSistema, text='Sistema PR',
                                      **config_label_ajuda, image=img_sistema, compound='top')
        self.lbSistemaDetalhe = ctk.CTkLabel(self.frAjudaSistema, 
                                             text='Informe o modulo e detalhe o problema que está acontecendo com o sistema',
                                             **config_label_detalhes, wraplength=200, anchor=ctk.W)
        
        
        self.frAjudaEquipamento = ctk.CTkFrame(self.frAjuda, **config_frame_ajuda)
        
        self.lbEquipamento = ctk.CTkLabel(self.frAjudaEquipamento, text='Equipamento',
                                      **config_label_ajuda, image=img_equipamento, compound='top')
        self.lbEquipamentoDetalhe = ctk.CTkLabel(self.frAjudaEquipamento, text='Informe o equipamento e o problema que está acontecendo com o computador',
                                             **config_label_detalhes, wraplength=200)
        
        
        self.frAjudaSoftware = ctk.CTkFrame(self.frAjuda, **config_frame_ajuda)
        
        self.lbSoftware = ctk.CTkLabel(self.frAjudaSoftware, text='Programas',
                                      **config_label_ajuda, image=img_software, compound='top')
        self.lbSoftwareDetalhe = ctk.CTkLabel(self.frAjudaSoftware, 
                                              text='Informe o programa e detalhe o problema que está acontecendo',
                                             **config_label_detalhes, wraplength=200)
        
        
        self.frAjudaRede = ctk.CTkFrame(self.frAjuda, **config_frame_ajuda)
        
        self.lbRede = ctk.CTkLabel(self.frAjudaRede, text='Internet',
                                      **config_label_ajuda, image=img_internet, compound='top')
        self.lbRedeDetalhe = ctk.CTkLabel(self.frAjudaRede, text='Informe o problema e detalhe o que está acontecendo com a internet',
                                             **config_label_detalhes, wraplength=200)
        
        
        self.frChamado =ctk.CTkFrame(self.frMain, **config_frame_ajuda, width=600)
        
        self.lbEviarChamado = ctk.CTkLabel(self.frChamado, text='Enviar um novo chamado de TI',
                                           font=ctk.CTkFont('Inter', weight='bold', size=25),
                                           text_color='black')
        
        config_label_chamado = {'font':ctk.CTkFont('Inter', weight='bold', size=15), 'text_color':'black'}
        config_entry_chamado = {'height':40, 'fg_color':'#f2f2f2','font':ctk.CTkFont('Inter', weight='normal', size=15),
                                'text_color':'black', 'border_color':'#f2f2f2' }
        config_combobox_chamado = {'height':40, 'fg_color':'#f2f2f2','font':ctk.CTkFont('Inter', weight='normal', size=15),
                                'text_color':'black', 'border_color':'#f2f2f2', 'state':'readonly',
                                'width':250,'button_color':'#0d6efd', 'dropdown_font':ctk.CTkFont('Inter', weight='normal', size=15)}
        
        config_textbox_chamado = {'fg_color':'#f2f2f2','font':ctk.CTkFont('Inter', weight='normal', size=15),
                                  'text_color':'black', 'border_color':'#f2f2f2'}
        self.carregar_dados()
        self.varSetor = ctk.StringVar()
        self.varCategoria = ctk.StringVar()
        self.varPrioridade = ctk.StringVar()
        
        if self.setores and self.categorias and self.prioridades:
            self.varSetor.set(self.setores[0])
            self.varCategoria.set(self.categorias[0])
            self.varPrioridade.set(self.prioridades[0])
        
        
        self.lbTituloChamado = ctk.CTkLabel(self.frChamado, text='Título do Chamado', **config_label_chamado)
        self.entryTituloChamado = ctk.CTkEntry(self.frChamado, placeholder_text='Você precisa de ajuda com o quê?',
                                               **config_entry_chamado)
        
        self.lbSetor = ctk.CTkLabel(self.frChamado, text='Setor', **config_label_chamado)
        self.cbSetor = ctk.CTkComboBox(self.frChamado, **config_combobox_chamado, values=self.setores, variable=self.varSetor)
        
        self.lbCategoria = ctk.CTkLabel(self.frChamado, text='Categoria', **config_label_chamado)
        self.cbCategoria = ctk.CTkComboBox(self.frChamado, **config_combobox_chamado,values=self.categorias, variable=self.varCategoria)
        
        self.lbPrioridade = ctk.CTkLabel(self.frChamado, text='Prioridade', **config_label_chamado)
        self.cbPrioridade = ctk.CTkComboBox(self.frChamado, **config_combobox_chamado, values=self.prioridades, variable=self.varPrioridade)
        
        self.lbDetalhe = ctk.CTkLabel(self.frChamado, text='Detalhes do Problema', **config_label_chamado)
        self.txDetalhe = ctk.CTkTextbox(self.frChamado,**config_textbox_chamado)
        
        self.btEnviar = ctk.CTkButton(self.frChamado, text='Enviar Chamado',
                                      font=ctk.CTkFont('Inter', weight='bold', size=15), height=40,
                                      fg_color='#0d6efd', command=self.enviar_chamado)
        
    def carregar_dados(self):
        self.setores = None
        self.categorias = Categoria.get_categorias_name()
        self.prioridades = Prioridade.get_prioridades_name()
        try:
            self.setores = setorCRUD.seleciona_nome_setores()
        except Exception as e:
            print(f"Erro ao carregar dados do database: {e}")
            
    def carregar_widgets(self):
        self.frMain.pack()
        
    
        self.lbTitulo.pack(pady=20)
        self.lbInstrucoes.pack()
        
        self.frAjuda.pack()
        
        self.frAjudaSistema.pack(side=ctk.LEFT, padx=10)
        self.frAjudaEquipamento.pack(side=ctk.LEFT, padx=10)
        self.frAjudaSoftware.pack(side=ctk.LEFT, padx=10)
        self.frAjudaRede.pack(side=ctk.LEFT, padx=10)
        
        self.frAjudaSistema.pack_propagate(0)
        self.frAjudaEquipamento.pack_propagate(0)
        self.frAjudaSoftware.pack_propagate(0)
        self.frAjudaRede.pack_propagate(0)
        
        
        self.lbSistema.pack(padx=5)
        self.lbSistemaDetalhe.pack()
        self.lbEquipamento.pack(padx=5)
        self.lbEquipamentoDetalhe.pack(fill=ctk.X)
        self.lbSoftware.pack(padx=5)
        self.lbSoftwareDetalhe.pack(fill=ctk.X)
        self.lbRede.pack(padx=5)
        self.lbRedeDetalhe.pack(fill=ctk.X)
        
        self.frChamado.pack(padx=80, fill=ctk.X)
        
        self.lbEviarChamado.pack()
        
        self.lbTituloChamado.pack(anchor='w', padx=10, pady=10)
        self.entryTituloChamado.pack(anchor='w', padx=10, fill=ctk.X)
        self.lbSetor.pack(anchor='w', padx=10, pady=10)
        self.cbSetor.pack(anchor='w', padx=10)
        self.lbCategoria.pack(anchor='w', padx=10, pady=10)
        self.cbCategoria.pack(anchor='w', padx=10)
        self.lbPrioridade.pack(anchor='w', padx=10, pady=10)
        self.cbPrioridade.pack(anchor='w', padx=10)
        self.lbDetalhe.pack(anchor='w', padx=10, pady=10)
        self.txDetalhe.pack(anchor='w', padx=10, fill=ctk.BOTH, expand=True)
        self.btEnviar.pack(padx=10, pady=10, fill=ctk.X)
        
    def enviar_chamado(self):
        id_usuario = self.root.usuario_logado.id
        titulo = self.entryTituloChamado.get()
        setor = setorCRUD.selecionar_id_setor_por_nome(self.varSetor.get())
        categoria = Categoria.get_categoria_id(self.varCategoria.get())
        prioridade = Prioridade.get_prioridade_id(self.varPrioridade.get())
        detalhes = self.txDetalhe.get('0.0', ctk.END)
        
        retorno = chamadoCRUD.adicionar_chamado(id_usuario, titulo, setor, categoria,
                                                prioridade, detalhes)
        
        if retorno['tipo'] == 'sucesso':
            self.entryTituloChamado.delete('0', ctk.END)
            self.txDetalhe.delete('0.0', ctk.END)
        
        thead = threading.Thread(target=lambda : WidgetAlerta(self,retorno['mensagem'], retorno['tipo']))
        thead.start()
        
        
    def carregar_tela(self):
        self.pack(fill=ctk.BOTH, expand=True)