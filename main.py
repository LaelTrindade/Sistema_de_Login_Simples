import os
import customtkinter as ctk
from tkinter import *
from PIL import Image
from main_cadastro import cadastro_screen
import database

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('dark-blue')

app = ctk.CTk()
app.geometry('700x400')
app.title('Login')
icon_app = PhotoImage(file = os.path.join(BASE_DIR, 'assets', 'images', 'icon.png'))

app.iconphoto(True, icon_app)
app.resizable(False, False)

image_login = ctk.CTkImage(
    dark_image = Image.open(os.path.join(BASE_DIR, 'assets', 'images', 'image_login.png')),
    light_image = Image.open(os.path.join(BASE_DIR, 'assets', 'images', 'image_login.png')),
    size = (400, 390))

label_image = ctk.CTkLabel(app,
    text = '',
    image = image_login)

label_image.place(x = 5, y = 5)

frame_1 = ctk.CTkFrame(app,
    width = 285,
    height = 390,
    corner_radius = 10)

frame_1.place(x = 410, y = 5)

label_1 = ctk.CTkLabel(frame_1,
    text = 'Login',
    font = ('arial', 20, 'bold'))

label_1.place(relx = 0.5, y = 50, anchor = 'center')

label_2 = ctk.CTkLabel(frame_1,
    text = 'Para utilizar nossos serviços, \ninsira suas informações de login!',
    font = ('arial', 10, 'italic'))

label_2.place(relx = 0.5, y = 80, anchor = 'center')

frame_2 = ctk.CTkFrame(frame_1,
    width = 225,
    height = 160,
    fg_color = '#1a1a1a',
    corner_radius = 20)

frame_2.place(relx = 0.5, rely = 0.46, anchor = 'center')

entry_1 = ctk.CTkEntry(frame_2,
    width = 175,
    placeholder_text = 'Usuário...')

entry_1.place(relx = 0.5, rely = 0.3, anchor = 'center')

entry_2 = ctk.CTkEntry(frame_2,
    width = 175,
    placeholder_text = 'Senha...',
    show = '*')

entry_2.place(relx = 0.5, rely = 0.6, anchor = 'center')

checkbox_1 = ctk.CTkCheckBox(frame_2,
    text = 'Lembre de mim',
    checkbox_width = 12,
    checkbox_height = 12)

checkbox_1.place(relx = 0.36, rely = 0.8, anchor = 'center')

def login_button():
    login = entry_1.get()
    senha = entry_2.get()

    sucesso, mensagem = database.login_usuario(login, senha)
    database.mostrar_popup("Bem-vindo" if sucesso else "Erro", mensagem, master = app)

button_1 = ctk.CTkButton(frame_1,
    width = 215,
    text = 'Login',
    corner_radius = 10,
    fg_color = '#1E3A8A',
    command = login_button)

button_1.place(relx = 0.5, y = 290, anchor = 'center')

button_2 = ctk.CTkButton(frame_1,
    width = 215,
    text = 'Registrar-se',
    corner_radius = 10,
    fg_color = '#1E3A8A',
    command = cadastro_screen)

button_2.place(relx = 0.5, y = 325, anchor = 'center')

app.mainloop()