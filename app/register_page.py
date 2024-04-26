# IMPORTING LIBRARIES

from tkinter import *


# IMPORTING FRONTS PAGES

from front_connector import load_register


# NEW USER REGISTRATION SCREEN

def registry():
    
    def btn_clicked():
        
        name = entry2.get()
        email = entry1.get()
        password = entry0.get()
        
        window4.destroy()

        load_register(name, email, password)


    window4 = Tk()
    
    window4.geometry("434x266")
    window4.configure(bg = "#ffffff")
    canvas = Canvas(
        window4,
        bg = "#ffffff",
        height = 266,
        width = 434,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)
    
    background4_img = PhotoImage(file = f"imagens/background4.png")
    background4 = canvas.create_image(
        217.0, 133.0,
        image=background4_img)
    
    entry0_img = PhotoImage(file = f"imagens/img_textBox02.png")
    entry0_bg = canvas.create_image(
        245.5, 145.5,
        image = entry0_img)
    
    entry0 = Entry(
        bd = 0,
        bg = "#d9d9d9",
        highlightthickness = 0)
    
    entry0.place(
        x = 193, y = 140,
        width = 105,
        height = 9)
    
    entry1_img = PhotoImage(file = f"imagens/img_textBox122.png")
    entry1_bg = canvas.create_image(
        235.0, 118.5,
        image = entry1_img)
    
    entry1 = Entry(
        bd = 0,
        bg = "#d9d9d9",
        highlightthickness = 0)
    
    entry1.place(
        x = 172, y = 113,
        width = 126,
        height = 9)
    
    entry2_img = PhotoImage(file = f"imagens/img_textBox22.png")
    entry2_bg = canvas.create_image(
        235.0, 89.5,
        image = entry2_img)
    
    entry2 = Entry(
        bd = 0,
        bg = "#d9d9d9",
        highlightthickness = 0)
    
    entry2.place(
        x = 172, y = 84,
        width = 126,
        height = 9)
    
    img02 = PhotoImage(file = f"imagens/img02.png")
    b02 = Button(
        image = img02,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")
    
    b02.place(
        x = 188, y = 166,
        width = 58,
        height = 29)
    
    
    window4.resizable(False, False)
    window4.mainloop()