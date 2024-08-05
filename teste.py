import customtkinter
from PIL import Image
import pywinstyles

HEIGHT = 500
WIDTH = 500

app = customtkinter.CTk()
app.title("example")
app.geometry((f"{WIDTH}x{HEIGHT}"))
app.resizable(False, False)

Label1 = customtkinter.CTkLabel(master=app, text="", fg_color='red',
                                width=500, height=500)
Label1.place(x=0, y=0)

Button1 = customtkinter.CTkButton(master=app, width=255, height=172, corner_radius=48,
                                  text='BUTTON', bg_color="#000001") 
Button1.place(x=120, y=57)

pywinstyles.set_opacity(Button1, color="#000001") # just add this line

app.mainloop()