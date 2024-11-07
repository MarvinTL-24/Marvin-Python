import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Função para capturar os dados do formulário
def enviar_dados():
    nome = nome_entry.get()
    email = email_entry.get()
    senha = senha_entry.get()

    # Exibir os dados capturados em uma caixa de diálogo
    messagebox.showinfo("Dados Capturados", f"Nome: {nome}\nEmail: {email}\nSenha: {senha}")

# Criar a janela principal
window = tk.Tk()
window.title("Cadastro de Usuário")
window.geometry("400x300")  # Definir tamanho fixo da janela
window.config(bg="#f4f4f9")  # Cor de fundo da janela

# Criar um frame para conter os widgets do formulário
form_frame = ttk.Frame(window, padding="20", relief="solid", style="TFrame")
form_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

# Definir estilo para os widgets
style = ttk.Style()
style.configure("TFrame", background="#ffffff")
style.configure("TLabel", background="#ffffff", font=("Arial", 12))
style.configure("TButton", font=("Arial", 12), background="#4CAF50", foreground="white")
style.configure("TEntry", font=("Arial", 12), padding=5)

# Criar os widgets do formulário
nome_label = ttk.Label(form_frame, text="Nome:")
nome_entry = ttk.Entry(form_frame, width=30)

email_label = ttk.Label(form_frame, text="Email:")
email_entry = ttk.Entry(form_frame, width=30)

senha_label = ttk.Label(form_frame, text="Senha:")
senha_entry = ttk.Entry(form_frame, show="*", width=30)

# Organizar os widgets usando o gerenciador de layout grid
nome_label.grid(row=0, column=0, sticky="w", pady=5)
nome_entry.grid(row=0, column=1, sticky="ew", pady=5)

email_label.grid(row=1, column=0, sticky="w", pady=5)
email_entry.grid(row=1, column=1, sticky="ew", pady=5)

senha_label.grid(row=2, column=0, sticky="w", pady=5)
senha_entry.grid(row=2, column=1, sticky="ew", pady=5)

# Ajustar a largura das colunas
form_frame.grid_columnconfigure(1, weight=1)

# Criar um botão para enviar o formulário
enviar_button = ttk.Button(form_frame, text="Enviar", command=enviar_dados)
enviar_button.grid(row=3, column=0, columnspan=2, pady=10)

# Iniciar o loop de eventos
window.mainloop()
