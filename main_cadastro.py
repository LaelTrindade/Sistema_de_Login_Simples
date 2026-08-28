import os
import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk
import database

cadastro_app = None

def cadastro_screen():

    global cadastro_app

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    if(cadastro_app is None or not cadastro_app.winfo_exists()):
        cadastro_app = ctk.CTkToplevel()
        cadastro_app.title('Cadastro')
        cadastro_app.geometry('350x500')
        cadastro_app.resizable(False, False)
        cadastro_app.attributes('-topmost', True)

        frame_1 = ctk.CTkFrame(cadastro_app,
            width = 340,
            height = 340,
            corner_radius = 10)
        
        frame_1.place(relx = 0.5, rely = 0.65, anchor = 'center')

        canvas_1 = Canvas(cadastro_app,
            width = 340,
            height = 140,
            highlightthickness = 0,
            bg = "#1F1F1F")
        
        canvas_1.place(x = 5, y = 5)

        img = Image.open(os.path.join(BASE_DIR, 'assets', 'images', 'image_cadastro_1.png'))
        img = img.resize((340, 140))
        bg = ImageTk.PhotoImage(img)

        canvas_1.create_image(0, 0, anchor = 'nw', image = bg)
        canvas_1.bg = bg

        x_center = 170
        y_center = 40

        offsets = [
            (-2,0), (2,0), (0,-2), (0,2),
            (-1,-1), (-1,1), (1,-1), (1,1)
        ]

        for dx, dy in offsets:
            canvas_1.create_text(
                x_center + dx,
                y_center + dy,
                text="Registrar-se",
                fill="#172F70",
                font=("Montserrat", 24, "bold")
            )

        # Essa parte de fazer o contorno foi bem complexa, peguei do ChatGPT.

        canvas_1.create_text(
            170,
            40,
            text = 'Registrar-se',
            fill = 'white',
            font = ("Montserrat", 24, "bold")
        )

        offsets = [
            (-1,0), (1,0), (0,-1), (0,1),
            (-1,-1), (-1,1), (1,-1), (1,1)
        ]

        for dx, dy in offsets:
            canvas_1.create_text(
                170 + dx,
                85 + dy,
                text='Crie sua conta agora e aproveite todos\nos nossos serviços com facilidade e segurança.!',
                fill='#172F70',
                font=('Montserrat', 10, 'italic'),
                justify='center'
            )

        # Essa parte de fazer o contorno foi bem complexa, peguei do ChatGPT.

        canvas_1.create_text(
            170,
            85,
            text = 'Crie sua conta agora e aproveite todos\nos nossos serviços com facilidade e segurança.!',
            fill = 'white',
            font = ('Montserrat', 10, 'italic'),
            justify = 'center'
        )

        label_2 = ctk.CTkLabel(frame_1,
            text = 'Nome Completo:',
            font = ('verdana', 12, 'italic'))
        
        label_2.place(x = 5, y = 2)

        entry_1 = ctk.CTkEntry(frame_1,
            width = 250,
            height = 15,
            placeholder_text = 'Ex: Eduardo da Silva')
        
        entry_1.place(x = 5, y = 25)

        label_3 = ctk.CTkLabel(frame_1,
            text = 'Telefone/Celular:',
            font = ('verdana', 12, 'italic'))
        
        label_3.place(x = 5, y = 55)

        entry_2 = ctk.CTkEntry(frame_1,
            width = 250,
            height = 15,
            placeholder_text = '(DDD) x xxxx-xxxx')
        
        entry_2.place(x = 5, y = 78)

        label_4 = ctk.CTkLabel(frame_1,
            text = 'Email:',
            font = ('verdana', 12, 'italic'))
        
        label_4.place(x = 5, y = 108)

        entry_3 = ctk.CTkEntry(frame_1,
            width = 250,
            height = 15,
            placeholder_text = 'exemplo@gmail.com')
        
        entry_3.place(x = 5, y = 131)

        label_5 = ctk.CTkLabel(frame_1,
            text = 'Senha:',
            font = ('verdana', 12, 'italic'))
        
        label_5.place(x = 5, y = 163)

        entry_4 = ctk.CTkEntry(frame_1,
            width = 250,
            height = 15,
            show = '*')
        
        entry_4.place(x = 5, y = 186)

        label_6 = ctk.CTkLabel(frame_1,
            text = 'Confirmar senha:',
            font = ('verdana', 12, 'italic'))
        
        label_6.place(x = 5, y = 218)

        entry_5 = ctk.CTkEntry(frame_1,
            width = 250,
            height = 15,
            show = '*')
        
        entry_5.place(x = 5, y = 241)

        checkbox_var = ctk.BooleanVar(value = False)
        checkbox_1 = ctk.CTkCheckBox(frame_1,
            text = 'Concordo com os Termos e Condições de Uso',
            checkbox_width = 10,
            checkbox_height = 10,
            variable = checkbox_var)

        checkbox_1.place(x = 5, y = 267)

        def finalizar_cadastro(): 
            if not checkbox_var.get():

                database.mostrar_popup('Erro',
                'Você deve aceitar os Termos e Condições de uso.', master = cadastro_app)

                return

            data_users = {
            "nome": entry_1.get(),
            "telefone": entry_2.get(),
            "email": entry_3.get(),
            "senha": entry_4.get()
            }

            confirmar = entry_5.get()

            if(data_users["senha"] != confirmar):
                
                database.mostrar_popup('Erro', "Senha não confere.", master = cadastro_app)
                return
            
            data_users["login"] = database.gerar_login(data_users["nome"])
            
            sucesso, mensagem = database.cadastrar_usuario(data_users)
            database.mostrar_popup("Sucesso" if sucesso else "Erro", mensagem, master = cadastro_app)

        button_1 = ctk.CTkButton(frame_1,
            width = 150,
            height = 25,
            text = 'Finalizar',
            fg_color = '#1E3A8A',
            corner_radius = 10,
            command = finalizar_cadastro)
        
        button_1.place(relx = 0.5, y = 312, anchor = 'center')