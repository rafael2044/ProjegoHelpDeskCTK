import customtkinter as ctk
from PIL import Image
from tkinter import PhotoImage

class TelaLoading(ctk.CTkFrame):
    def __init__(self, master,root):
        super().__init__(master, bg_color='white', fg_color='white')
        self.master=master
        self.root = root
        self.configurar_tela()
        self.carregar_git()
        self.animation()
    def configurar_tela(self):
        self.pack(expand=True, fill=ctk.BOTH)
        self.lbGif = ctk.CTkLabel(self, text='')
        self.lbGif.pack(fill=ctk.BOTH, expand=True, padx=400, pady=200)
        
    def carregar_git(self):
        imgLoading = 'assets/gifs/loading.gif'
        info = Image.open(imgLoading)
        self.frames = info.n_frames
        self.photoimage_objects = []
        for i in range(self.frames):
           obj = PhotoImage(file=imgLoading, format=f'gif -index {i}')
           self.photoimage_objects.append(obj)

    def animation(self, current_frame=0):
        image = self.photoimage_objects[current_frame]
        self.lbGif.configure(image=image)
        current_frame = current_frame + 1

        if current_frame == self.frames:
            current_frame = 0

        self.loop = self.root.after(50, lambda: self.animation(current_frame))
    
    def stop_animation(self):
        self.root.after_cancel(self.loop)
