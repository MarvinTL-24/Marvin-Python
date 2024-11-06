import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class Aluno:
    def __init__(self, nome, matricula, curso, data_nascimento):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.data_nascimento = data_nascimento
        self.notas = {}  # Dicionário para armazenar listas de notas por disciplina

    def idade(self):
        nascimento = datetime.strptime(self.data_nascimento, "%d/%m/%Y")
        hoje = datetime.now()
        return hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))

    def adicionar_notas(self, disciplina, notas):
        self.notas[disciplina] = notas

    def calcular_media_curso(self):
        total_notas = sum(sum(notas) for notas in self.notas.values())
        quantidade_notas = sum(len(notas) for notas in self.notas.values())
        return total_notas / quantidade_notas if quantidade_notas > 0 else 0.0

    def __str__(self):
        notas_str = '\n'.join([f"{disciplina}: {', '.join(map(str, notas))}" for disciplina, notas in self.notas.items()])
        return (f"Nome: {self.nome}\nMatrícula: {self.matricula}\nCurso: {self.curso}\n"
                f"Data de Nascimento: {self.data_nascimento}\nNotas:\n{notas_str}")

class SistemaCadastroAlunos:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def buscar_aluno_por_matricula(self, matricula):
        return next((aluno for aluno in self.alunos if aluno.matricula == matricula), None)

    def excluir_aluno(self, matricula):
        aluno = self.buscar_aluno_por_matricula(matricula)
        if aluno:
            self.alunos.remove(aluno)
            return True
        return False

class Aplicacao:
    def __init__(self, root):
        self.sistema = SistemaCadastroAlunos()
        self.root = root
        self.root.title("Sistema de Cadastro de Alunos")

        # Dicionário de cursos disponíveis
        self.cursos = {"Programação", "Designer"}
        self.create_widgets()

    def create_widgets(self):
        # Widgets de cadastro de aluno

        tk.Label(self.root, text="Data de Nascimento (DD/MM/YYYY):").grid(row=3, column=0, sticky="ew")
        self.nascimento_entry = tk.Entry(self.root, bd=2, relief="solid")
        self.nascimento_entry.grid(row=3, column=1, pady=2, sticky="ew")

        tk.Label(self.root, text="Nome:").grid(row=0, column=0, sticky="ew")
        self.nome_entry = tk.Entry(self.root, bd=2, relief="solid")
        self.nome_entry.grid(row=0, column=1, pady=2, sticky="ew")

        tk.Label(self.root, text="Matrícula:").grid(row=1, column=0, sticky="ew")
        self.matricula_entry = tk.Entry(self.root, bd=2, relief="solid")
        self.matricula_entry.grid(row=1, column=1, pady=2, sticky="ew")

        tk.Label(self.root, text="Curso:").grid(row=2, column=0, sticky="ew")
        self.curso_entry = tk.Entry(self.root, bd=2, relief="solid")
        self.curso_entry.grid(row=2, column=1, pady=2, sticky="ew")

        tk.Label(self.root, text="Disciplina:").grid(row=4, column=0, sticky="ew")
        self.disciplina_entry = tk.Entry(self.root, bd=2, relief="solid")
        self.disciplina_entry.grid(row=4, column=1, pady=2, sticky="ew")

        tk.Label(self.root, text="Notas (separadas por vírgula):").grid(row=5, column=0, sticky="ew")
        self.notas_entry = tk.Entry(self.root, bd=2, relief="solid")
        self.notas_entry.grid(row=5, column=1, pady=2, sticky="ew")

        self.cadastrar_button = tk.Button(self.root, text="Cadastrar Aluno", command=self.cadastrar_aluno)
        self.cadastrar_button.grid(row=6, column=0, columnspan=2, pady=5, sticky="ew")

        self.adicionar_notas_button = tk.Button(self.root, text="Adicionar Notas", command=self.adicionar_notas)
        self.adicionar_notas_button.grid(row=7, column=0, columnspan=2, pady=5, sticky="ew")

        # Botão para salvar alunos
        self.salvar_button = tk.Button(self.root, text="Salvar Alunos", command=self.salvar)
        self.salvar_button.grid(row=8, column=0, columnspan=2, pady=5, sticky="ew")

    def cadastrar_aluno(self):
        nome = self.nome_entry.get()
        matricula = self.matricula_entry.get()
        curso = self.curso_entry.get()
        data_nascimento = self.nascimento_entry.get()

        if curso not in self.cursos:
            messagebox.showerror("Erro", "Curso inválido.")
            return

        try:
            aluno = Aluno(nome, matricula, curso, data_nascimento)
            if aluno.idade() < 0:
                raise ValueError("Data de nascimento inválida.")
            self.sistema.adicionar_aluno(aluno)
            messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def adicionar_notas(self):
        matricula = self.matricula_entry.get()
        disciplina = self.disciplina_entry.get()
        notas_texto = self.notas_entry.get()
        aluno = self.sistema.buscar_aluno_por_matricula(matricula)

        if not aluno:
            messagebox.showerror("Erro", "Aluno não encontrado.")
            return

        try:
            notas = list(map(float, notas_texto.split(',')))
            aluno.adicionar_notas(disciplina, notas)
            messagebox.showinfo("Sucesso", "Notas adicionadas com sucesso!")
        except ValueError:
            messagebox.showerror("Erro", "Formato de notas inválido.")

    def salvar(self):
        with open("Cadastro.txt", "w") as file:
            file.write("Cadastro de alunos:\n\n")
            for aluno in self.sistema.alunos:
                file.write(str(aluno) + "\n\n")
            messagebox.showinfo("Sucesso", "Dados salvos em 'Cadastro.txt'.")

# Criando a janela principal
if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacao(root)
    root.title("Cadastros de Alunos")
    root.geometry("400x500")  # Ajuste no tamanho da janela
    root.mainloop()
