import customtkinter as ctk
from telas.telaAtualizarChamado import TelaAtualizarChamado
from telas.telaAtenderChamado import TelaAtenderChamado

class WidgetChamado(ctk.CTkFrame):
    def __init__(self, master,root, chamado):
        super().__init__(master, cursor='hand2')
        self.chamado = chamado
        self.root=root
        self.configurar_tela()
        self.criar_widgets()
        self.carregar_widgets()
        self.bind('<Motion>', self.aplicar_hover_color)
        self.bind("<Leave>", self.aplicar_hover_color)
        self.bind('<Button-1>', self.verificar_click_chamado)
        

        
    def configurar_tela(self):
        self.configure(fg_color='#f2f2f2')
        self.configure(corner_radius=20)
        
    def criar_widgets(self):
        
        config_label_titles = {'text_color':'gray', 'font':ctk.CTkFont('Inter', weight='normal', size=15), 'bg_color':'transparent'}
        config_label_dados = {'text_color':'black', 'font':ctk.CTkFont('Inter', weight='normal', size=18)}
        config_textbox_chamado = {'fg_color':'#f2f2f2','font':ctk.CTkFont('Inter', weight='normal', size=18),
                                  'text_color':'black', 'border_color':'#f2f2f2'}
        config_frame = {'fg_color':'transparent', 'bg_color':'transparent'}
        self.frTop = ctk.CTkFrame(self, **config_frame)
        self.frTitulo = ctk.CTkFrame(self.frTop, **config_frame)
        self.lbTituloChamado = ctk.CTkLabel(self.frTitulo, text=self.chamado.titulo,
                                            font=ctk.CTkFont('Inter', weight='bold', size=18), text_color='black')
        self.lbStatus = ctk.CTkLabel(self.frTitulo, text=self.chamado.get_status(), font=ctk.CTkFont("Inter", weight='bold', size=12),
                                     text_color='#333333')
        
        self.lbDetalheChamado = ctk.CTkLabel(self.frTop, text=self.chamado.detalhes,
                                            **config_label_dados)
        
        self.frSeparator = ctk.CTkFrame(self, height=2, fg_color='gray')
        
        self.frMiddle = ctk.CTkFrame(self, **config_frame)
        
        self.frMiddleCol1 = ctk.CTkFrame(self.frMiddle, **config_frame)
        self.frMiddleCol2 = ctk.CTkFrame(self.frMiddle, **config_frame)
        self.frMiddleCol3 = ctk.CTkFrame(self.frMiddle, **config_frame)
        self.frMiddleCol4 = ctk.CTkFrame(self.frMiddle, **config_frame)
        self.frBottom = ctk.CTkFrame(self, **config_frame)
        self.frBottomCol1 = ctk.CTkFrame(self.frBottom, **config_frame)
        self.frBottomCol2 = ctk.CTkFrame(self.frBottom, **config_frame)
        
        self.lbCategoria = ctk.CTkLabel(self.frMiddleCol1, text='Categoria', **config_label_titles)
        self.lbSetor = ctk.CTkLabel(self.frMiddleCol2, text='Setor', **config_label_titles)
        self.lbSolicitante = ctk.CTkLabel(self.frMiddleCol3, text='Soliciado Por', **config_label_titles)
        
        
        self.lbCategoriaChamado  =ctk.CTkLabel(self.frMiddleCol1, text=self.chamado.get_categoria(), **config_label_dados)
        self.lbSetorChamado  =ctk.CTkLabel(self.frMiddleCol2, text=self.chamado.setor.nome, **config_label_dados)
        self.lbSolicitanteChamado = ctk.CTkLabel(self.frMiddleCol3, text=self.chamado.solicitante.nome, **config_label_dados)
        
        self.btAtualizar = ctk.CTkButton(self.frMiddleCol4, text='Atualizar', fg_color='#0d6efd', font=ctk.CTkFont('Inter', weight='bold', size=18),
                                         command=self.carregar_tela_atualizarChamado)
        if self.chamado.get_status() == 'Concluido':
            atendimento = self.chamado.atendimento.first()
            self.lbAtendimento = ctk.CTkLabel(self.frBottomCol1, text='Atendido Por', **config_label_titles)
            self.lbAtendimentoChamado = ctk.CTkLabel(self.frBottomCol1, text=atendimento.suporte.nome, **config_label_dados)
            self.lbDescricaoAtendimento = ctk.CTkLabel(self.frBottomCol2, text='Descrição do Atendimento', **config_label_titles)
            self.tbDescricaoAtendimento = ctk.CTkTextbox(self. frBottomCol2, **config_textbox_chamado)
            self.tbDescricaoAtendimento.insert('0.0', atendimento.detalhes)
            self.tbDescricaoAtendimento.configure(state=ctk.DISABLED)
            self.lbTituloDataAtendimento = ctk.CTkLabel(self.frBottomCol1, text='Data do Atendimento', **config_label_titles)
            self.lbDataAtendimento = ctk.CTkLabel(self.frBottomCol1, text=atendimento.data_atendimento.strftime('%d-%m-%Y %H:%M'), **config_label_dados)
        if self.root.usuario_logado.get_privilegio() in ('Administrador', 'Suporte'):
            self.btAtualizar.configure(text='Atender')
            self.btAtualizar.configure(command=self.exibir_telaAtenderChamado)
            
        
    def carregar_widgets(self):
     
        self.frTop.pack(fill=ctk.X, padx=10, pady=(10,5))
        self.frTitulo.pack(fill=ctk.X)
        self.lbTituloChamado.pack(padx=5, anchor=ctk.W, side=ctk.LEFT, expand=True)
        self.lbStatus.pack(padx=5, side=ctk.LEFT, anchor=ctk.E)
        self.lbDetalheChamado.pack(padx=10, pady=(5,20), anchor=ctk.W)
        
        self.frMiddleCol1.pack(side=ctk.LEFT, fill=ctk.X, pady=5, expand=True)
        self.frMiddleCol2.pack(side=ctk.LEFT, fill=ctk.X, expand=True)
        self.frMiddleCol3.pack(side=ctk.LEFT, fill=ctk.X, expand=True)
        self.frMiddleCol4.pack(side=ctk.LEFT, fill=ctk.X, expand=True)
        self.lbCategoria.pack(padx=5, anchor=ctk.W)
        self.lbSetor.pack(padx=5, anchor=ctk.W)
        self.lbSolicitante.pack(padx=5, anchor=ctk.W)
        
        self.lbCategoriaChamado.pack(padx=5, anchor=ctk.W, pady=(0,5))
        self.lbSetorChamado.pack(padx=5, anchor=ctk.W, pady=(0,5))
        self.lbSolicitanteChamado.pack(padx=5, anchor=ctk.W, pady=(0,5))
        
        self.btAtualizar.pack(padx=5, anchor=ctk.E, pady=(0,5))
        if (self.chamado.get_status() == 'Concluido'):
            self.btAtualizar.configure(state=ctk.DISABLED)
            self.lbAtendimento.pack(padx=5, anchor=ctk.W)
            self.lbAtendimentoChamado.pack(padx=5, anchor=ctk.W, pady=(0,5))
            self.lbDescricaoAtendimento.pack(anchor=ctk.W, padx=5)
            self.tbDescricaoAtendimento.pack(fill=ctk.BOTH, expand=True, padx=5, pady=5, anchor=ctk.W)
            self.lbTituloDataAtendimento.pack(anchor=ctk.W, padx=5, pady=5)
            self.lbDataAtendimento.pack(anchor=ctk.W, padx=5, pady=5)
            
        self.frTop.bind('<Button-1>', self.verificar_click_chamado)
        self.frTitulo.bind('<Button-1>', self.verificar_click_chamado)
        self.frMiddle.bind('<Button-1>', self.verificar_click_chamado)
        self.frMiddleCol1.bind('<Button-1>', self.verificar_click_chamado)
        self.frMiddleCol2.bind('<Button-1>', self.verificar_click_chamado)
        self.frMiddleCol3.bind('<Button-1>', self.verificar_click_chamado)
        self.frMiddleCol4.bind('<Button-1>', self.verificar_click_chamado)
        self.lbTituloChamado.bind('<Button-1>', self.verificar_click_chamado)
        self.lbDetalheChamado.bind('<Button-1>', self.verificar_click_chamado)
        self.lbStatus.bind('<Button-1>', self.verificar_click_chamado)
        self.lbCategoria.bind('<Button-1>', self.verificar_click_chamado)
        self.lbCategoriaChamado.bind('<Button-1>', self.verificar_click_chamado)
        self.lbSetor.bind('<Button-1>', self.verificar_click_chamado)
        self.lbSetorChamado.bind('<Button-1>', self.verificar_click_chamado)
        self.lbSolicitante.bind('<Button-1>', self.verificar_click_chamado)
        self.lbSolicitanteChamado.bind('<Button-1>', self.verificar_click_chamado)
        if self.chamado.get_status() == 'Concluido':
            self.lbAtendimento.bind('<Button-1>', self.verificar_click_chamado)
            self.lbAtendimentoChamado.bind('<Button-1>', self.verificar_click_chamado)
            self.frBottom.bind('<Button-1>', self.verificar_click_chamado)
            self.lbDescricaoAtendimento.bind('<Button-1>', self.verificar_click_chamado)
            self.tbDescricaoAtendimento.bind('<Button-1>', self.verificar_click_chamado)
            self.frBottomCol1.bind('<Button-1>', self.verificar_click_chamado)
            self.frBottomCol2.bind('<Button-1>', self.verificar_click_chamado)
            self.lbTituloDataAtendimento.bind('<Button-1>', self.verificar_click_chamado)
            self.lbDataAtendimento.bind('<Button-1>', self.verificar_click_chamado)
        
    def expandir_informacoes(self):
        self.frSeparator.pack(fill=ctk.X, padx=10)
        self.frMiddle.pack(fill=ctk.X, padx=10, pady=10)
        if (self.chamado.get_status() == 'Concluido'):
            self.frBottom.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)
            self.frBottomCol1.pack(side=ctk.LEFT, fill=ctk.BOTH)
            self.frBottomCol2.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True)

    
    def carregar_tela_atualizarChamado(self):
        TelaAtualizarChamado(self.root,self.chamado, self.root.PRIVILEGIO)
   
    def exibir_telaAtenderChamado(self):
        TelaAtenderChamado(self.root,self.chamado)
   
    def ocultar_informacoes(self):
        if (self.chamado.get_status() == 'Concluido'):
            self.frBottom.pack_forget()
        self.frMiddle.pack_forget()
        self.frSeparator.pack_forget()
        
        
    def verificar_click_chamado(self,event):
        mouse_x, mouse_y = self.winfo_pointerxy()

        frame_x = self.winfo_rootx()
        frame_y = self.winfo_rooty()
    
        frame_width = self.winfo_width()
        frame_height = self.winfo_height()

        if frame_x <= mouse_x < frame_x + frame_width and \
        frame_y <= mouse_y < frame_y + frame_height:
            if not self.lbCategoria.winfo_viewable():
                self.expandir_informacoes()
            else:
                self.ocultar_informacoes()
                
    def aplicar_hover_color(self, event):

        mouse_x, mouse_y = self.winfo_pointerxy()
    
        frame_x = self.winfo_rootx()
        frame_y = self.winfo_rooty()
        
        frame_width = self.winfo_width()
        frame_height = self.winfo_height()
        
        if frame_x <= mouse_x < frame_x + frame_width and \
        frame_y <= mouse_y < frame_y + frame_height:
            self.configure(fg_color='#f3f6f4')
        else:
            self.configure(fg_color="#f2f2f2")
            
    def carregar_tela(self):
        self.pack(fill=ctk.X, padx=5, pady=(5))
        