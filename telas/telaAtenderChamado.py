import customtkinter as ctk
from widgets.widgetAlerta import WidgetAlerta
import threading
from models.categoria import Categoria
from models.prioridade import Prioridade
import datetime

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
        config_entry = {'text_color':'black', 'font':ctk.CTkFont('Inter', weight='normal', size=20), 'fg_color':'#f2f2f2',
                              'border_color':'#f2f2f2', 'height':40}
        config_button = {'fg_color':'#0d6efd', 'font':ctk.CTkFont('Inter',weight='bold', size=20), 'height':40}
        
        config_combobox_chamado = {'height':40, 'fg_color':'#f2f2f2','font':ctk.CTkFont('Inter', weight='normal', size=15),
                                'text_color':'black', 'border_color':'#f2f2f2', 'state':'readonly',
                                'width':250,'button_color':'#0d6efd', 'dropdown_font':ctk.CTkFont('Inter', weight='normal', size=15)}
        
        config_textbox_chamado = {'fg_color':'#f2f2f2','font':ctk.CTkFont('Inter', weight='normal', size=15),
                                  'text_color':'black', 'border_color':'#f2f2f2'}
        
        self.carregar_dados()
        self.varCategoria = ctk.StringVar()
        self.varCategoria.set(self.chamado.categoria.nome_categoria)
        self.varPrioridade = ctk.StringVar()
        self.varPrioridade.set(self.chamado.prioridade.nome_prioridade)
        
        self.frMain  = ctk.CTkScrollableFrame(self, fg_color='white', bg_color='transparent', border_width=1, border_color='black', corner_radius=0)
        self.frMain.master = self.frMain._parent_canvas
        self.frTitulo = ctk.CTkFrame(self.frMain, fg_color='transparent', bg_color='transparent', height=20)
        
        self.btFechar = ctk.CTkButton(self.frTitulo, text='X',width=30, height=30, fg_color='transparent', bg_color='transparent',
                                      hover_color='gray', command=self.fechar_tela, border_color='black', border_width=2,
                                      text_color='black', font=ctk.CTkFont('Inter',weight='bold', size=20))
        
        self.lbTitulo = ctk.CTkLabel(self.frTitulo, text='Atualizar Chamado', **config_label)
        self.lbTituloChamado = ctk.CTkLabel(self.frMain, text='Titulo do Chamado', **config_label)
        self.entryTituloChamado  =ctk.CTkEntry(self.frMain,**config_entry)
        self.entryTituloChamado.insert('0', self.chamado.titulo)
        self.entryTituloChamado.configure(state=ctk.DISABLED)
        self.lbDetalhesChamado = ctk.CTkLabel(self.frMain, text='Detalhes do Chamado', **config_label)
        self.tbDetalhesChamado = ctk.CTkTextbox(self.frMain, **config_textbox_chamado)
        self.tbDetalhesChamado.insert('0.0', self.chamado.detalhes)
        self.tbDetalhesChamado.configure(state=ctk.DISABLED)
        self.lbCategoriaChamado = ctk.CTkLabel(self.frMain, text='Categoria do Chamado', **config_label)
        self.cbCategoriaChamado = ctk.CTkComboBox(self.frMain, **config_combobox_chamado,values=self.categorias, variable=self.varCategoria)
        self.cbCategoriaChamado.configure(state=ctk.DISABLED)
        self.lbPrioridadeChamado = ctk.CTkLabel(self.frMain, text='Prioridade do Chamado', **config_label)
        self.cbPrioridadeChamado = ctk.CTkComboBox(self.frMain, **config_combobox_chamado,values=self.prioridades, variable=self.varPrioridade)
        self.cbPrioridadeChamado.configure(state=ctk.DISABLED)
        self.lbDescricaoAtendimento = ctk.CTkLabel(self.frMain, text='Descrição do Atendimento', **config_label)
        self.tbDescricaoAtendimento = ctk.CTkTextbox(self.frMain, **config_textbox_chamado)
        
        self.btCancelar = ctk.CTkButton(self.frMain, text='Cancelar', command=self.fechar_tela, font= ctk.CTkFont('Inter',weight='bold', size=20),
                                        height=40, fg_color='white', hover_color='gray', text_color='black')
        self.btFinalizar = ctk.CTkButton(self.frMain, text='Finalizar', command=self.atender_chamado, **config_button)
        
    def carregar_widgets(self):
        self.frMain.pack(fill=ctk.BOTH, expand=True, padx=5, pady=5)
        self.frTitulo.pack(fill=ctk.X)
        self.lbTitulo.pack(side=ctk.LEFT,anchor=ctk.W, padx=20, pady=30, expand=True)
        self.btFechar.pack(side=ctk.LEFT, anchor=ctk.E, padx=10)
        self.btFechar.pack_propagate(0)
        self.lbTituloChamado.pack(anchor=ctk.W, padx=20, pady=(0,10))
        self.entryTituloChamado.pack(fill=ctk.X, padx=20, pady=(0,10))
        self.lbDetalhesChamado.pack(anchor=ctk.W, padx=20, pady=(0,10), )
        self.tbDetalhesChamado.pack(padx=20, pady=(0,10), fill=ctk.BOTH, expand=True)
        self.lbCategoriaChamado.pack(anchor=ctk.W, padx=20, pady=(0,10))
        self.cbCategoriaChamado.pack(fill=ctk.X, padx=20, pady=(0,10))
        self.lbPrioridadeChamado.pack(anchor=ctk.W, padx=20, pady=(0,10))
        self.cbPrioridadeChamado.pack(fill=ctk.X, padx=20, pady=(0,10))
        self.lbDescricaoAtendimento.pack(anchor=ctk.W, padx=20, pady=(0,10))
        self.tbDescricaoAtendimento.pack(fill=ctk.BOTH, expand=True, padx=20, pady=(0,10))
        self.btFinalizar.pack(side=ctk.RIGHT, padx=20, pady=30)
        self.btCancelar.pack(side=ctk.RIGHT, padx=10, pady=30)
    
    def carregar_dados(self):
        self.categorias = None
        self.prioridades = None
        try:
            self.categorias = [x.nome_categoria for x in Categoria.select()]
            self.prioridades = [x.nome_prioridade for x in Prioridade.select()]
        except Exception as e:
            print(f"Erro ao carregar dados do database: {e}")
    
    def atender_chamado(self):
        suporte_atendimento = self.root.usuario_logado
        descricao_atendimento = self.tbDescricaoAtendimento.get('0.0', ctk.END)
        try:
            if descricao_atendimento:
                data_fechamento = datetime.datetime.now()
                self.chamado.situacao = 2
                self.chamado.descricao_atendimento = descricao_atendimento
                self.chamado.data_fechamento = data_fechamento
                self.chamado.suporte_atendimento = suporte_atendimento
                self.chamado.save()
                self.master.telaChamados.carregar_dados_chamados()
                self.master.telaChamados.carregar_chamados()
                try:
                    thead = threading.Thread(target=lambda : WidgetAlerta(self.root.frConteudo, 'Chamado finalizado com sucesso!', 'sucesso'))
                    thead.start()
                except Exception as e:
                    pass
                self.destroy()
            else:
                try:
                    thead = threading.Thread(target=lambda : WidgetAlerta(self,'O campo de descrição precisa ser preenchido!', 'aviso'))
                    thead.start()
                except Exception as e:
                    pass
        except Exception as e:
                thead = threading.Thread(target=lambda : WidgetAlerta(self,'Ocorreu um erro finalizar atendimento do chamado!', 'erro'))
                thead.start()
            
    def fechar_tela(self):
        self.destroy()

        
        
        
        