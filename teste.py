import tkinter as tk
from tkinter import ttk

class SmoothHideFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        
        self.widgets_to_hide = []
        self.create_widgets()
        self.pack()
        
    def create_widgets(self):
        # Exemplo de widgets
        self.label = tk.Label(self, text="Este é um label", font=("Arial", 18))
        self.label.pack(padx=20, pady=10)
        
        self.button = ttk.Button(self, text="Alternar Detalhes", command=self.toggle_details)
        self.button.pack(pady=10)
        
        # Widgets para mostrar e ocultar suavemente
        self.detail_label = tk.Label(self, text="Detalhes:", font=("Arial", 16))
        self.detail_label.pack(padx=20, pady=10)
        
        self.detail_text = tk.Text(self, height=5, width=30)
        self.detail_text.insert(tk.END, "Alguns detalhes aqui...\n" * 5)
        self.detail_text.pack(padx=20, pady=10)
        
        # Adicionar widgets que serão ocultados
        self.widgets_to_hide.extend([self.detail_label, self.detail_text])
        
        # Configurações iniciais
        self.hidden = True
        
    def toggle_details(self):
        if self.hidden:
            self.show_widgets()
        else:
            self.hide_widgets()
            
    def hide_widgets(self):
        # Animação de desvanecimento
        for widget in self.widgets_to_hide:
            self.fade_out(widget)
        self.hidden = True
        
    def show_widgets(self):
        # Mostrar widgets
        for widget in self.widgets_to_hide:
            widget.pack()
        # Animação de aparecimento
        for widget in self.widgets_to_hide:
            self.fade_in(widget)
        self.hidden = False
        
    def fade_out(self, widget, alpha=1.0):
        if alpha > 0:
            alpha -= 0.1
            widget.configure(fg=self.fade_color(alpha))
            self.after(50, lambda: self.fade_out(widget, alpha))
        else:
            widget.pack_forget()
            
    def fade_in(self, widget, alpha=0.0):
        if alpha < 1:
            alpha += 0.1
            widget.configure(fg=self.fade_color(alpha))
            self.after(50, lambda: self.fade_in(widget, alpha))
        else:
            pass  # Não faz nada ao finalizar o fade in
            
    def fade_color(self, alpha):
        # Converter alpha para um valor hexadecimal (exemplo)
        alpha = int(alpha * 255)
        return f'#{alpha:02x}{alpha:02x}{alpha:02x}'
        

root = tk.Tk()
app = SmoothHideFrame(root)
root.mainloop()
