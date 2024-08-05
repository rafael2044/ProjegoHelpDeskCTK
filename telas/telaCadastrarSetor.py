import customtkinter as ctk
from widgets.widgetAlerta import WidgetAlerta
import threading
from crud import setorCRUD
import pywinstyles

class TelaCadastrarSetor(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.root = master
        self.wm_overrideredirect(True)
        self.configurar_tela()
        self.criar_widgets()
        self.carregar_widgets()
        self.grab_set()
       
    def configurar_tela(self):
        self.update()
        WIDTH = 600
        HEIGHT = 300
        POS_X = int((self.root.winfo_screenwidth() - WIDTH) / 2)
        POS_Y = int((self.root.winfo_screenheight() - HEIGHT) /2)
        self.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")
        
        
    def criar_widgets(self):
        config_label = {'text_color':'black', 'font':ctk.CTkFont('Inter', size=20)}
        config_entry = {'text_color':'black', 'font':ctk.CTkFont('Inter', weight='normal', size=20), 'fg_color':'white', 'height':40}
        config_button = {'fg_color':'#0d6efd', 'font':ctk.CTkFont('Inter',weight='bold', size=20), 'height':40}
        
                
        self.frMain  = ctk.CTkFrame(self, fg_color="#ced4da", bg_color='#000001', corner_radius=20)
        self.frMain.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)
        pywinstyles.apply_style(self, 'transparent')
        pywinstyles.set_opacity(self.frMain, color='#000001')
        self.frTitulo = ctk.CTkFrame(self.frMain, fg_color='transparent', bg_color='transparent', height=20)
        
        self.btFechar = ctk.CTkButton(self.frTitulo, text='X',width=30, height=30, fg_color='transparent', bg_color='transparent',
                                      hover_color='#dc3545', command=self.fechar_tela, border_color='black', border_width=2,
                                      text_color='black', font=ctk.CTkFont('Inter',weight='bold', size=20))
        
        self.lbTitulo = ctk.CTkLabel(self.frTitulo, text='Cadastrar Setor', font=ctk.CTkFont('Inter', weight='bold', size=25),
                                     text_color='black')
        self.lbNomeSetor = ctk.CTkLabel(self.frMain, text='Nome do Setor', **config_label)
        self.entryNomeSetor  =ctk.CTkEntry(self.frMain,**config_entry)
        
        self.btCancelar = ctk.CTkButton(self.frMain, text='Cancelar', command=self.fechar_tela, font= ctk.CTkFont('Inter',weight='bold', size=20),
                                        fg_color='transparent', hover_color='#dc3545', text_color='black', height=40)
        self.btCriar = ctk.CTkButton(self.frMain, text='Criar', command=self.criar_setor, **config_button)
        
        
        
    def carregar_widgets(self):
        self.frTitulo.pack(fill=ctk.X, padx=5, pady=5)
        self.lbTitulo.pack(side=ctk.LEFT,anchor=ctk.W, padx=15, pady=(20,0), expand=True)
        self.btFechar.pack(side=ctk.LEFT, anchor=ctk.E, padx=15, pady=(20,0))
        self.btFechar.pack_propagate(0)
        ctk.CTkFrame(self.frMain, height=2, bg_color='black').pack(fill=ctk.X, padx=20, pady=10)
        self.lbNomeSetor.pack(anchor=ctk.W, padx=20, pady=(0,10))
        self.entryNomeSetor.pack(fill=ctk.X, padx=20, pady=(0,10))
        self.btCriar.pack(side=ctk.RIGHT, padx=20, pady=10)
        self.btCancelar.pack(side=ctk.RIGHT, padx=10, pady=10)
    
    def criar_setor(self):
        nome_setor = self.entryNomeSetor.get()        
        try:
            retorno = setorCRUD.adicionar_setor(nome_setor)
            thead = threading.Thread(target=lambda : WidgetAlerta(self.master,retorno['mensagem'], retorno['tipo']))
            thead.start()
            if retorno['tipo'] == 'sucesso':
                self.entryNomeSetor.delete('0', ctk.END)
        except Exception as e:
                thead = threading.Thread(target=lambda : WidgetAlerta(self.master,'Ocorreu um erro ao cadastrar o setor!', 'erro'))
                thead.start()
            
    def limpar_campos(self):
        self.entryNomeSetor.delete('0', ctk.END)
    
    def fechar_tela(self):
        self.destroy()

        
        
        
        