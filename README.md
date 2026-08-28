# Sistema de Login [Moderno]

Sistema desktop de login e cadastro de usuários, desenvolvido em Python com CustomTkinter. Interface moderna com tela de login e tela de registro, validação de dados e persistência em JSON.

## ✨ Funcionalidades

- **Login de usuário** com validação de login e senha
- **Cadastro de novo usuário** (nome completo, telefone, email e senha)
- **Geração automática de login** a partir do nome completo (ex: `Lael Trindade` → `lael.trindade`)
- **Validação de confirmação de senha** no cadastro
- **Aceite obrigatório dos Termos e Condições** via checkbox
- **Popups de feedback** (sucesso/erro) para o usuário
- **Persistência de dados em JSON**, sem necessidade de banco de dados externo
- **Tema escuro** por padrão, com interface construída em CustomTkinter

## ⚠️ Limitações conhecidas

- O checkbox **"Lembrar de mim"** na tela de login está presente na interface, mas não possui funcionalidade implementada
- O cadastro **não valida campos em branco** (nome, telefone, email e senha) — apenas o aceite dos Termos e Condições e a confirmação de senha são validados

## 🛠️ Tecnologias

- **Python 3.12**
- **[CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)** — widgets modernos sobre o Tkinter
- **Pillow (PIL)** — manipulação de imagens
- **JSON** — armazenamento local dos usuários cadastrados

## 📂 Estrutura do projeto

```
Sistema de Login [Moderno]/
├── main.py                 # Tela de login (ponto de entrada)
├── main_cadastro.py         # Tela de cadastro de usuário
├── database.py               # Funções de leitura/escrita no JSON e popups
├── assets/
│   ├── images/                # Ícone e imagens da interface
│   └── database/
│       └── data.json           # Armazenamento dos usuários (versionado, vazio)
└── README.md
```

## ▶️ Como executar

1. Clone o repositório:
```bash
git clone git@github.com:LaelTrindade/Sistema-de-Login-Simples---Custom-Tkinter.git
cd Sistema-de-Login-Simples---Custom-Tkinter
```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
```

3. Instale as dependências:
```bash
pip install customtkinter pillow
```

4. Execute o sistema:
```bash
python main.py
```

> O arquivo `assets/database/data.json` já vem versionado no repositório, vazio (`{"users": []}`), pronto para uso na primeira execução.

## 📌 Sobre o projeto

Este projeto foi desenvolvido como exercício prático de **interfaces gráficas em Python**, explorando posicionamento de widgets com `place()`, customização visual com Canvas (contorno de texto), manipulação de imagens com Pillow e persistência simples de dados sem depender de um banco de dados relacional.
