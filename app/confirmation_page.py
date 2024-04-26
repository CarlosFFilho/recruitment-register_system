# APPLICATION CONFIRMATION SCREEN

from tkinter import *

def confirm_page (identity_confirm, id_confirm):

    window2 = Tk()
    
    window2.geometry("434x266")
    window2.configure(bg = "#ffffff")
    canvas = Canvas(
        window2,
        bg = "#ffffff",
        height = 266,
        width = 434,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)
    
    background2_img = PhotoImage(file = f"imagens/background2.png")
    background = canvas.create_image(
        217.0, 133.0,
        image=background2_img)
    
    canvas.create_text(
        241.5, 181.0,
        text = identity_confirm,
        fill = "#fffdfd",
        font = ("Moulpali-Regular", int(9.0)))
    
    canvas.create_text(
        217.5, 150.0,
        text = id_confirm,
        fill = "#fffefe",
        font = ("Moul-Regular", int(16.0)))
    
    window2.resizable(False, False)
    window2.mainloop()