import os
import json
import customtkinter as ctk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FILE = os.path.join(BASE_DIR, 'assets', 'database', 'data.json')

popup = None

def mostrar_popup(title, message, master):

    global popup

    if(master is None):
        master = ctk._get_default_root()

    if(popup is None or not popup.winfo_exists()):
        popup = ctk.CTkToplevel()
        popup.title(title)
        popup.geometry('300x150')
        popup.resizable(False, False)

        label = ctk.CTkLabel(popup,
            text = message,
            wraplength = 250,
            font = ('arial', 16, 'bold'))
        
        label.pack(pady = 20)
        
        popup.attributes("-topmost", True)
        popup.transient(master)
        popup.update_idletasks()
        popup.grab_set()
        popup.focus()


def carregar_dados():
    try:
        with open(FILE, 'r') as f:
            return json.load(f)
    
    except:
        return {"users": []}
    
def salvar_dados(dados):
    with open(FILE, 'w') as f:
        json.dump(dados, f, indent = 4)
    
def cadastrar_usuario(dados_usuario):
    dados = carregar_dados()

    for user in dados["users"]:
        if(user["email"]) == dados_usuario["email"]:
            return False, "Email já cadastrado."
        
    dados_usuario["id"] = len(dados["users"]) + 1

    dados["users"].append(dados_usuario)
    salvar_dados(dados)

    return True, "Usuário cadastrado com sucesso!"

def login_usuario(login_digitado, senha_digitada):
    dados = carregar_dados()

    for user in dados["users"]:
        if user["login"] == login_digitado:
            if user["senha"] == senha_digitada:
                return True, f"Bem-vindo, {user['nome']}!"
            else:
                return False, "Senha incorreta."

    return False, "Login não encontrado."

def gerar_login(nome_completo):
    nomes = nome_completo.strip().split()
    if len(nomes) < 2:
        return nomes[0].lower()
    primeiro = nomes[0].lower()
    ultimo = nomes[-1].lower()
    return f"{primeiro}.{ultimo}"