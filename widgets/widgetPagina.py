import customtkinter as ctk
import math

class WidgetPagina(ctk.CTkFrame):
    def __init__(self, master, dados: list):
        super().__init__(master=master)
        self.dados = dados
        self.configurar_tela()
        self.criar_widgets()
        self.carregar_widgets()

    def configurar_tela(self):
        self.configure(bg_color='transparent')
        self.configure(fg_color='transparent')
        
        
    def configurar_paginacao(self):
        self.num_item_page = 5
        self.num_page = math.ceil(len(self.dados)/self.num_item_page)
        self.current_page = 1
        
    def carregar_pagina(self, num_pagina):
        if num_pagina != self.current_page:
            self.current_page = num_pagina
            self.carregar_itens()
            
    def proxima_pagina(self):
        if self.current_page < self.num_page:
            self.current_page+=1
            self.carregar_itens()
    def pagina_anterior(self):
        if self.current_page>1:
            self.current_page -= 1
            self.carregar_itens()
            
    def carregar_itens(self):
        if self.frConteudo.winfo_children():
            for item in self.frConteudo.winfo_children():
                item.pack_forget()
                
        for item in self.wig_dados[(self.current_page*5-5):self.current_page*5]:
            item.pack()
                    
        
    def gerar_dados(self):
        self.wig_dados = []
        for d in self.dados:
            self.wig_dados.append(ctk.CTkLabel(self.frConteudo, text=d))
        print(self.wig_dados)
        
    def criar_widgets(self):
        self.frConteudo = ctk.CTkFrame(self)
        self.frPaginacao = ctk.CTkFrame(self)
        self.configurar_paginacao()
        self.gerar_dados()

        
        
        
    def carregar_widgets(self):
        self.frConteudo.pack(fill=ctk.BOTH, expand=True)
        self.frPaginacao.pack(fill=ctk.X)
        
        
        self.carregar_itens()
        ctk.CTkButton(self.frPaginacao, text='<', command=self.pagina_anterior, width=30).pack(side=ctk.LEFT)
        for x in range(self.num_page):
            print(x)
            ctk.CTkButton(self.frPaginacao, text=f'{x+1}', command=lambda x=x: self.carregar_pagina(x+1), width=30).pack(side=ctk.LEFT)
        ctk.CTkButton(self.frPaginacao, text='>', command=self.proxima_pagina, width=30).pack(side=ctk.LEFT)
        
        
        
        
        
        
if __name__ == '__main__':
    app = ctk.CTk()
    dados = ['123', 'dasdaw', 'sdasds ', 'adawdasdasd',
             'asdsdsdas', 'sddscxcz', 'sdasdasdsad',
             '123', 'dasdaw', 'sdasds ', 'adawdasdasd',
             'asdsdsdas', 'sddscxcz', 'sdasdasdsad']
    
    paginador = WidgetPagina(app, dados)
    
    paginador.pack(fill=ctk.BOTH, expand=True)
    
    app.mainloop()