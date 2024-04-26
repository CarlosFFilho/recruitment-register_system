# IMPORTING LIBRARIES

from tkinter import *
import datetime
import pytz


# IMPORTING FRONTS PAGES

import front_connector as fc


# APPLICATION SCREEN

def initial(expiration):
    
    id_confirm = 0

    def btn_clicked():
        
        Name = entry20.get()
        Identity = entry19.get()
        Type_identity = opcao_selecionada4.get()
        Phone_number = entry17.get()
        Email_address = entry16.get()
        Driving_licence = opcao_selecionada3.get()
        Driving_licence_class = opcao_selecionada5.get()
        
        Street = entry13.get()
        City = entry12.get()
        State = entry11.get()
        Postal_code = entry10.get()
        Country = entry9.get()
        Avaliable_for_change = opcao_selecionada2.get()
        
        Educational_level = opcao_selecionada6.get()
        Course = entry6.get()
        Institution = entry5.get()
        Year_of_course_completion = entry4.get()
        English_language = opcao_selecionada.get()
        
        Chemical_industry_years = entry2.get()
        Last_position = entry1.get()
        Performed_activities = entry0.get()
        
        window.destroy()
        
        confirmations_infos = fc.load_initial(Name, Identity, Type_identity, Phone_number, Email_address, Driving_licence, Driving_licence_class, 
Educational_level, Course, Institution, Year_of_course_completion, English_language, Street, City, State, Postal_code, 
Country, Avaliable_for_change, Chemical_industry_years, Last_position, Performed_activities)

        identity_confirm = confirmations_infos[0]
        
        id_confirm = confirmations_infos[1]

        fc.load_confirmation(expiration, identity_confirm, id_confirm)


    window = Tk()
    
    window.geometry("339x557")
    window.configure(bg = "#ffffff")
    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 557,
        width = 339,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)
    
    background_img = PhotoImage(file = f"images/background.png")
    background = canvas.create_image(
        170.0, 279.0,
        image=background_img)
    
    canvas.create_text(
        171.5, 46.5,
        text = "RECRUITMENT PAGE",
        fill = "#ffffff",
        font = ("Inter-ExtraBold", int(12.0)))
    
    canvas.create_text(
        72.5, 83.0,
        text = "Name:",
        fill = "#ffffff",
        font = ("None", int(10.0)))
    
    canvas.create_text(
        77.5, 103.0,
        text = "Identity:",
        fill = "#ffffff",
        font = ("None", int(10.0)))
    
    canvas.create_text(
        198.5, 103.0,
        text = "Type:",
        fill = "#ffffff",
        font = ("None", int(10.0)))
    
    canvas.create_text(
        73.5, 123.0,
        text = "Phone:",
        fill = "#ffffff",
        font = ("None", int(10.0)))
    
    canvas.create_text(
        72.5, 143.0,
        text = "Email:",
        fill = "#ffffff",
        font = ("None", int(10.0)))
    
    canvas.create_text(
        120.5, 163.0,
        text = "Have a driver's license?",
        fill = "#ffffff",
        font = ("None", int(10.0)))
    
    canvas.create_text(
        100.5, 330.0,
        text = "Education level:",
        fill = "#ffffff",
        font = ("None", int(10.0)))
    
    canvas.create_text(
        118.0, 286.0,
        text = "Avaliable for change?",
        fill = "#ffffff",
        font = ("None", int(10.0)))
    
    canvas.create_text(
        74.0, 226.0,
        text = "Street:",
        fill = "#ffffff",
        font = ("None", int(10.0)))
    
    canvas.create_text(
        69.0, 246.0,
        text = "City:",
        fill = "#ffffff",
        font = ("None", int(10.0)))
    
    canvas.create_text(
        191.0, 246.0,
        text = "State:",
        fill = "#ffffff",
        font = ("None", int(10.0)))
    
    canvas.create_text(
        92.5, 266.0,
        text = "Postal code:",
        fill = "#ffffff",
        font = ("None", int(10.0)))
    
    canvas.create_text(
        198.5, 266.0,
        text = "Country:",
        fill = "#ffffff",
        font = ("None", int(10.0)))
    
    canvas.create_text(
        77.5, 350.0,
        text = "Course:",
        fill = "#ffffff",
        font = ("None", int(10.0)))
    
    canvas.create_text(
        200.0, 350.0,
        text = "Institution:",
        fill = "#ffffff",
        font = ("None", int(10.0)))
    
    canvas.create_text(
        111.5, 370.0,
        text = "Year of completion:",
        fill = "#ffffff",
        font = ("None", int(10.0)))
    
    canvas.create_text(
        105.0, 390.0,
        text = "English domain?",
        fill = "#ffffff",
        font = ("None", int(10.0)))
    
    canvas.create_text(
        97.5, 433.0,
        text = "Industry years:",
        fill = "#ffffff",
        font = ("None", int(10.0)))
    
    canvas.create_text(
        92.5, 453.0,
        text = "Last position:",
        fill = "#ffffff",
        font = ("None", int(10.0)))
    
    canvas.create_text(
        81.5, 473.0,
        text = "Activities:",
        fill = "#ffffff",
        font = ("None", int(10.0)))
    
    canvas.create_text(
        117.0, 183.0,
        text = "Driver’s license class:",
        fill = "#ffffff",
        font = ("None", int(10.0)))
    
    img0 = PhotoImage(file = f"images/img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")
    
    b0.place(
        x = 143, y = 508,
        width = 63,
        height = 21)
    
    
    entry0_img = PhotoImage(file = f"images/img_textBox0.png")
    entry0_bg = canvas.create_image(
        205.0, 474.0,
        image = entry0_img)
    
    entry0 = Entry(
        bd = 0,
        bg = "#d9d9d9",
        highlightthickness = 0)
    
    entry0.place(
        x = 129, y = 469,
        width = 152,
        height = 11)
    
    entry1_img = PhotoImage(file = f"images/img_textBox1.png")
    entry1_bg = canvas.create_image(
        212.0, 454.0,
        image = entry1_img)
    
    entry1 = Entry(
        bd = 0,
        bg = "#d9d9d9",
        highlightthickness = 0)
    
    entry1.place(
        x = 143, y = 449,
        width = 138,
        height = 11)
    
    entry2_img = PhotoImage(file = f"images/img_textBox2.png")
    entry2_bg = canvas.create_image(
        198.5, 434.0,
        image = entry2_img)
    
    entry2 = Entry(
        bd = 0,
        bg = "#d9d9d9",
        highlightthickness = 0)
    
    entry2.place(
        x = 150, y = 429,
        width = 131,
        height = 11)
    
    entry3_img = PhotoImage(file = f"images/img_textBox3.png")
    entry3_bg = canvas.create_image(
        250.0, 391.0,
        image = entry3_img)
    
    opcoes = ["YES", "NO"]
    opcao_selecionada = StringVar(window)
    opcao_selecionada.set(opcoes[1])
    
    menu_opcoes = OptionMenu(window, opcao_selecionada, *opcoes)
    menu_opcoes.pack()
    
    menu_opcoes.place(
        x = 160, y = 386,
        width = 120,
        height = 18)
    
    entry4_img = PhotoImage(file = f"images/img_textBox4.png")
    entry4_bg = canvas.create_image(
        243.5, 371.0,
        image = entry4_img)
    
    entry4 = Entry(
        bd = 0,
        bg = "#d9d9d9",
        highlightthickness = 0)
    
    entry4.place(
        x = 170, y = 366,
        width = 110,
        height = 11)
    
    entry5_img = PhotoImage(file = f"images/img_textBox5.png")
    entry5_bg = canvas.create_image(
        261.0, 351.0,
        image = entry5_img)
    
    entry5 = Entry(
        bd = 0,
        bg = "#d9d9d9",
        highlightthickness = 0)
    
    entry5.place(
        x = 235, y = 346,
        width = 46,
        height = 11)
    
    entry6_img = PhotoImage(file = f"images/img_textBox6.png")
    entry6_bg = canvas.create_image(
        134.5, 351.0,
        image = entry6_img)
    
    entry6 = Entry(
        bd = 0,
        bg = "#d9d9d9",
        highlightthickness = 0)
    
    entry6.place(
        x = 102, y = 346,
        width = 63,
        height = 11)
    
    entry7_img = PhotoImage(file = f"images/img_textBox7.png")
    entry7_bg = canvas.create_image(
        217.0, 331.0,
        image = entry7_img)
    
    opcoes6 = ["None", "Associates", "Bachelor degree", "Master degree", "Doctorate"]
    opcao_selecionada6 = StringVar(window)
    opcao_selecionada6.set(opcoes6[0])
    
    menu_opcoes6 = OptionMenu(window, opcao_selecionada6, *opcoes6)
    menu_opcoes6.pack()
    
    menu_opcoes6.place(
        x = 153, y = 326,
        width = 128,
        height = 18)
    
    entry8_img = PhotoImage(file = f"images/img_textBox8.png")
    entry8_bg = canvas.create_image(
        190.5, 287.0,
        image = entry8_img)
    
    opcoes2 = ["YES", "NO"]
    opcao_selecionada2 = StringVar(window)
    opcao_selecionada2.set(opcoes2[1])
    
    menu_opcoes2 = OptionMenu(window, opcao_selecionada2, *opcoes2)
    menu_opcoes2.pack()
    
    menu_opcoes2.place(
        x = 183, y = 282,
        width = 99,
        height = 18)
    
    entry9_img = PhotoImage(file = f"images/img_textBox9.png")
    entry9_bg = canvas.create_image(
        260.5, 267.0,
        image = entry9_img)
    
    entry9 = Entry(
        bd = 0,
        bg = "#d9d9d9",
        highlightthickness = 0)
    
    entry9.place(
        x = 230, y = 262,
        width = 51,
        height = 11)
    
    entry10_img = PhotoImage(file = f"images/img_textBox10.png")
    entry10_bg = canvas.create_image(
        145.0, 267.0,
        image = entry10_img)
    
    entry10 = Entry(
        bd = 0,
        bg = "#d9d9d9",
        highlightthickness = 0)
    
    entry10.place(
        x = 134, y = 262,
        width = 32,
        height = 11)
    
    entry11_img = PhotoImage(file = f"images/img_textBox11.png")
    entry11_bg = canvas.create_image(
        250.0, 247.0,
        image = entry11_img)
    
    entry11 = Entry(
        bd = 0,
        bg = "#d9d9d9",
        highlightthickness = 0)
    
    entry11.place(
        x = 214, y = 242,
        width = 67,
        height = 11)
    
    entry12_img = PhotoImage(file = f"images/img_textBox12.png")
    entry12_bg = canvas.create_image(
        130.5, 247.0,
        image = entry12_img)
    
    entry12 = Entry(
        bd = 0,
        bg = "#d9d9d9",
        highlightthickness = 0)
    
    entry12.place(
        x = 88, y = 242,
        width = 71,
        height = 11)
    
    entry13_img = PhotoImage(file = f"images/img_textBox13.png")
    entry13_bg = canvas.create_image(
        195.5, 227.0,
        image = entry13_img)
    
    entry13 = Entry(
        bd = 0,
        bg = "#d9d9d9",
        highlightthickness = 0)
    
    entry13.place(
        x = 98, y = 222,
        width = 183,
        height = 11)
    
    entry14_img = PhotoImage(file = f"images/img_textBox14.png")
    entry14_bg = canvas.create_image(
        229.5, 184.0,
        image = entry14_img)
    
    opcoes5 = ["None", "A", "B", "C", "D"]
    opcao_selecionada5 = StringVar(window)
    opcao_selecionada5.set(opcoes5[0])
    
    menu_opcoes5 = OptionMenu(window, opcao_selecionada5, *opcoes5)
    menu_opcoes5.pack()
    
    menu_opcoes5.place(
        x = 182, y = 179,
        width = 99,
        height = 18)
    
    entry15_img = PhotoImage(file = f"images/img_textBox15.png")
    entry15_bg = canvas.create_image(
        253.0, 164.0,
        image = entry15_img)
    
    opcoes3 = ["YES", "NO"]
    opcao_selecionada3 = StringVar(window)
    opcao_selecionada3.set(opcoes3[1])
    
    menu_opcoes3 = OptionMenu(window, opcao_selecionada3, *opcoes3)
    menu_opcoes3.pack()
    
    menu_opcoes3.place(
        x = 195, y = 159,
        width = 86,
        height = 18)
    
    entry16_img = PhotoImage(file = f"images/img_textBox16.png")
    entry16_bg = canvas.create_image(
        193.0, 144.0,
        image = entry16_img)
    
    entry16 = Entry(
        bd = 0,
        bg = "#d9d9d9",
        highlightthickness = 0)
    
    entry16.place(
        x = 95, y = 139,
        width = 186,
        height = 11)
    
    entry17_img = PhotoImage(file = f"images/img_textBox17.png")
    entry17_bg = canvas.create_image(
        216.0, 124.0,
        image = entry17_img)
    
    entry17 = Entry(
        bd = 0,
        bg = "#d9d9d9",
        highlightthickness = 0)
    
    entry17.place(
        x = 101, y = 119,
        width = 180,
        height = 11)
    
    entry18_img = PhotoImage(file = f"images/img_textBox18.png")
    entry18_bg = canvas.create_image(
        268.0, 104.0,
        image = entry18_img)
       
    opcoes4 = ["RG", "CPF"]
    opcao_selecionada4 = StringVar(window)
    opcao_selecionada4.set(opcoes4[0])
    
    menu_opcoes4 = OptionMenu(window, opcao_selecionada4, *opcoes4)
    menu_opcoes4.pack()
    
    menu_opcoes4.place(
        x = 220, y = 96,
        width = 60,
        height = 18)
    
    entry19_img = PhotoImage(file = f"images/img_textBox19.png")
    entry19_bg = canvas.create_image(
        137.5, 104.0,
        image = entry19_img)
    
    entry19 = Entry(
        bd = 0,
        bg = "#d9d9d9",
        highlightthickness = 0)
    
    entry19.place(
        x = 101, y = 99,
        width = 67,
        height = 11)
    
    entry20_img = PhotoImage(file = f"images/img_textBox20.png")
    entry20_bg = canvas.create_image(
        197.5, 84.0,
        image = entry20_img)
    
    entry20 = Entry(
        bd = 0,
        bg = "#d9d9d9",
        highlightthickness = 0)
    
    entry20.place(
        x = 95, y = 79,
        width = 186,
        height = 11)
    
    window.resizable(False, False)
    window.mainloop()
