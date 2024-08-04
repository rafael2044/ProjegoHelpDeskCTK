import customtkinter as ctk
from peewee import DoesNotExist
from models.model import Usuario
from widgets.widgetAlerta import WidgetAlerta
import threading

class TelaLogin(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master=master
        self.configurar_tela()
        self.criar_widgets()
        self.carregar_widgets()
        self.carregar_tela()
        
        
    def configurar_tela(self):
        self.configure(fg_color='#0d6efd')
        self.configure(bg_color='#0d6efd')
        
        
    def criar_widgets(self):
        self.frCentral = ctk.CTkFrame(self, fg_color='white', bg_color='transparent', corner_radius=20,
                                      width=500, height=500)

        self.lbNomeSistema = ctk.CTkLabel(self.frCentral, text='helpdesk', font=ctk.CTkFont('Inter', weight='bold', size=35),
                                          text_color='black')
        self.lbEntrar = ctk.CTkLabel(self.frCentral, text='Entrar no Sistema', font=ctk.CTkFont('Inter', weight='bold', size=18),
                                     text_color='black')
        
        self.frSeparator = ctk.CTkFrame(self.frCentral, fg_color='#f2f2f2', height=2)
        
        config_label_login = {'text_color':'black', 'font':ctk.CTkFont('Inter', weight='bold', size=15)}
        config_entry_login = {'text_color':'black', 'font':ctk.CTkFont('Inter', weight='normal', size=15), 'fg_color':'#f2f2f2',
                              'border_color':'#f2f2f2', 'height':40}
        self.lbUsuario = ctk.CTkLabel(self.frCentral, text='Usuario', **config_label_login)
        self.entryUsuario = ctk.CTkEntry(self.frCentral, placeholder_text='Seu Usuário', **config_entry_login)
        self.lbSenha = ctk.CTkLabel(self.frCentral, text='Senha', **config_label_login)
        self.entrySenha = ctk.CTkEntry(self.frCentral, placeholder_text='Senha', **config_entry_login,
                                       show='*') 
        
        self.btEntrar = ctk.CTkButton(self.frCentral, text='Entrar', font=ctk.CTkFont('Inter', weight='bold', size=18),
                                      fg_color='#0d6efd', height=40, command=self.logar)
        
        self.entryUsuario.bind('<Return>', lambda event: self.entrySenha.focus_force())
        self.entrySenha.bind("<Return>", lambda event : self.logar())
    def carregar_widgets(self):

        self.frCentral.place(rely=0.5, relx=0.5, anchor=ctk.CENTER,
                             relwidth=0.40, relheight=0.6)
        
        self.lbNomeSistema.pack(pady=(50,20))
        self.lbEntrar.pack()
        self.frSeparator.pack(fill=ctk.X, pady=30, padx=30)
        self.lbUsuario.pack(anchor=ctk.W, padx=30, pady=(10,5))
        self.entryUsuario.pack(fill=ctk.X, padx=30)
        self.lbSenha.pack(anchor=ctk.W, padx=30, pady=(10,5))
        self.entrySenha.pack(fill=ctk.X, padx=30)
        self.btEntrar.pack(fill=ctk.X, padx=30, pady=20)
    
        
    def logar(self):
        usuario = self.entryUsuario.get()
        senha = self.entrySenha.get()
        try:
            retorno_usuario = Usuario.get(Usuario.usuario == usuario)
            if retorno_usuario.senha == senha:
                    self.master.PRIVILEGIO = retorno_usuario.get_privilegio()
                    self.master.criar_widgets()
                    self.master.carregar_widgets()
                    self.master.usuario_logado = retorno_usuario
                    self.destroy()
            else:
                try:
                    process_thread = threading.Thread(target=lambda : WidgetAlerta(self, 'Senha Incorreta!', 'alerta'))
                    process_thread.start()
                except Exception as e:
                    pass
        except DoesNotExist as e:
            try:
                process_thread = threading.Thread(target=lambda : WidgetAlerta(self, 'O usuario não existe!', 'alerta'))
                process_thread.start()
            except Exception as e:
                print(f"{e}")
    
    
    def carregar_tela(self):
        self.pack(fill=ctk.BOTH, expand=True)
        self.focus_force()
        