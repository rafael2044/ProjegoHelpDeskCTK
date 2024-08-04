import customtkinter as ctk
from telas.telaAlerta import TelaAlerta
from widgets.widgetAlerta import WidgetAlerta
import threading

class TelaUsuario(ctk.CTkFrame):
    def __init__(self, master,root, usuario):
        super().__init__(master)
        self.master=master
        self.root = root
        self.usuario_logado = usuario
        self.configurar_tela()
        self.criar_widgets()
        self.carregar_tela()
        self.carregar_widgets()
        
    def configurar_tela(self):
        self.configure(bg_color='transparent')
        self.configure(fg_color='#f7f7f7')
        self.configure(corner_radius=20)
        
    def criar_widgets(self):
        config_label = {'text_color':'black', 'font':ctk.CTkFont('Inter', size=20)}
        config_entry = {'text_color':'black', 'font':ctk.CTkFont('Inter', weight='normal', size=20), 'fg_color':'#f2f2f2',
                              'border_color':'#f2f2f2', 'height':40}
        config_button = {'fg_color':'#0d6efd', 'font':ctk.CTkFont('Inter',weight='bold', size=20), 'height':40}
        self.lbTitulo = ctk.CTkLabel(self, text='Minhas Informações', **config_label)
        self.entryNome  =ctk.CTkEntry(self,**config_entry)
        self.entryNome.insert('0', self.usuario_logado.nome)
        self.entryUsuario = ctk.CTkEntry(self, **config_entry)
        self.entryUsuario.insert('0', self.usuario_logado.usuario)
        self.entryUsuario.configure(state=ctk.DISABLED)
        self.btAtualizar = ctk.CTkButton(self, text='Atualizar Perfil', command=self.atualizar_nome, **config_button)
        self.lbAlterarSenha = ctk.CTkLabel(self, text='Alterar Senha', **config_label)
        self.entrySenhaAtual = ctk.CTkEntry(self, placeholder_text='Senha Atual', show='*', **config_entry, state=ctk.DISABLED)
        self.entrySenhaNova = ctk.CTkEntry(self, placeholder_text='Nova Senha', show='*', **config_entry)
        self.btAlterarSenha = ctk.CTkButton(self, text='Alterar Senha', command=self.alterar_senha, **config_button)
        
    def carregar_widgets(self):
        self.lbTitulo.pack(anchor=ctk.W, padx=20, pady=30)
        self.entryNome.pack(fill=ctk.X, padx=20, pady=(0,20))
        self.entryUsuario.pack(fill=ctk.X, padx=20)
        self.btAtualizar.pack(anchor=ctk.W, padx=20, pady=(20,0))
        ctk.CTkFrame(self, height=2, fg_color="#f2f2f2").pack(fill=ctk.X, padx=20, pady=30)
        self.lbAlterarSenha.pack(anchor=ctk.W, padx=20, pady=(0,30))
        self.entrySenhaAtual.pack(fill=ctk.X, padx=20, pady=(0,20))
        self.entrySenhaNova.pack(fill=ctk.X, padx=20)
        self.btAlterarSenha.pack(anchor=ctk.W, padx=20, pady=20)
    
    def atualizar_nome(self):
        novo_nome = self.entryNome.get()
        if novo_nome != self.usuario_logado.nome_usuario:
            self.usuario_logado.nome_usuario = novo_nome
            self.usuario_logado.save()
            try:
                thead = threading.Thread(target=lambda : WidgetAlerta(self, 'Nome alterado com Sucesso!', 'sucesso'))
                thead.start()
            except Exception as e:
                pass
        else:
            try:
                thead = threading.Thread(target=lambda : WidgetAlerta(self,'O novo nome não pode ser igual ao atual!', 'alerta'))
                thead.start()
            except Exception as e:
                pass
            
    def alterar_senha(self):
        nova_senha = self.entrySenhaNova.get()
        
        if len(nova_senha) >= 4:
            if self.usuario_logado.senha_usuario != nova_senha:
                self.usuario_logado.senha_usuario = nova_senha
                self.usuario_logado.save()
                self.entrySenhaAtual.delete('0', ctk.END)
                self.entrySenhaNova.delete('0', ctk.END)
                try:
                    thead = threading.Thread(target=lambda : WidgetAlerta(self, 'Senha alterada com Sucesso!', 'sucesso'))
                    thead.start()
                except Exception as e:
                    pass
            else:
                try:
                    thead = threading.Thread(target=lambda : WidgetAlerta(self, 'A senha precisa ser diferente da atual!', 'alerta'))
                    thead.start()
                except Exception as e:
                    pass
                
        else:
            try:
                thead = threading.Thread(target=lambda : WidgetAlerta(self, 'A senha precisa conter 4 ou mais caracteres!', 'info'))
                thead.start()
            except Exception as e:
                pass
            

    def carregar_tela(self):
        self.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.7, anchor=ctk.CENTER)
        
        
        
        