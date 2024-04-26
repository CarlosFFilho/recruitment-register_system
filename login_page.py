# IMPORTING LIBRARIES

from tkinter import *


# IMPORTING FRONTS PAGES

import register_page as rpage
import front_connector as fconn


# USER LOGIN SCREEN

def login():

    def btn_clicked_1():
        
        log_user = entry0.get()
        pass_user = entry1.get()
        
        window3.destroy()
        
        fconn.load_login(log_user, pass_user)
    
    
    def btn_clicked_2():
        
        window3.destroy()

        rpage.registry()

        login()
        
    window3 = Tk()
    
    window3.geometry("434x266")
    window3.configure(bg = "#ffffff")
    canvas = Canvas(
        window3,
        bg = "#ffffff",
        height = 266,
        width = 434,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)
    
    background3_img = PhotoImage(file = f"imagens/background3.png")
    background3 = canvas.create_image(
        217.0, 133.0,
        image=background3_img)
    
    entry0_img = PhotoImage(file = f"imagens/img_textBox01.png")
    entry0_bg = canvas.create_image(
        232.5, 102.5,
        image = entry0_img)
    
    entry0 = Entry(
        bd = 0,
        bg = "#d9d9d9",
        highlightthickness = 0)
    
    entry0.place(
        x = 173, y = 96,
        width = 119,
        height = 11)
    
    entry1_img = PhotoImage(file = f"imagens/img_textBox111.png")
    entry1_bg = canvas.create_image(
        243.0, 139.5,
        image = entry1_img)
    
    entry1 = Entry(
        bd = 0,
        bg = "#d9d9d9",
        highlightthickness = 0)
    
    entry1.place(
        x = 194, y = 133,
        width = 98,
        height = 11)
    
    img0 = PhotoImage(file = f"imagens/img01.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked_1,
        relief = "flat")
    
    b0.place(
        x = 194, y = 164,
        width = 46,
        height = 29)
    
    img1 = PhotoImage(file = f"imagens/img11.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked_2,
        relief = "flat")
    
    b1.place(
        x = 134, y = 200,
        width = 165,
        height = 29)
    
    window3.resizable(False, False)
    window3.mainloop()

login()