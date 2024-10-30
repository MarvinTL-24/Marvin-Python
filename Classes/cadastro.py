class Aluno:
    def __init__(self, nome, matricula, curso, data_nascimento):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.data_nascimento = data_nascimento

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, nova_matricula):
        self._matricula = nova_matricula

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, novo_curso):
        self._curso = novo_curso

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, nova_data_nascimento):
        self._data_nascimento = nova_data_nascimento

    def __str__(self):
        return (f"Nome: {self.nome}\n"
                f"Matrícula: {self.matricula}\n"
                f"Curso: {self.curso}\n"
                f"Data de Nascimento: {self.data_nascimento}")

class SistemaCadastroAlunos:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def buscar_aluno_por_nome(self, nome):
        return next((aluno for aluno in self.alunos if aluno.nome.lower() == nome.lower()), None)

    def buscar_aluno_por_matricula(self, matricula):
        return next((aluno for aluno in self.alunos if aluno.matricula == matricula), None)

    def excluir_aluno(self, matricula):
        aluno = self.buscar_aluno_por_matricula(matricula)
        if aluno:
            self.alunos.remove(aluno)
            print("Aluno excluído com sucesso!")
        else:
            print("Aluno não encontrado.")

class Notas:
    def __init__(self):
        self.notas = []

    def adicionar_nota(self, disciplina, nota):
        if 0 <= nota <= 10:
            self.notas.append({"disciplina": disciplina, "nota": nota})
        else:
            print(f"Erro: Nota inválida ({nota}). Deve estar entre 0 e 10.")

    def get_notas(self):
        return self.notas

    def calcular_media(self):
        if not self.notas:
            return 0.0
        return sum(nota["nota"] for nota in self.notas) / len(self.notas)

    def __str__(self):
        return '\n'.join([f"{nota['disciplina']}: {nota['nota']}" for nota in self.notas])

class Curso:
    def __init__(self, nome, disciplinas):
        self.nome = nome
        self.disciplinas = disciplinas

    def __str__(self):
        return f"Curso: {self.nome}, Disciplinas: {', '.join(self.disciplinas)}"

def main():
    sistema = SistemaCadastroAlunos()

    while True:
        print("\nMenu Principal:")
        print("1. Cadastrar Aluno")
        print("2. Consultar Aluno")
        print("3. Excluir Aluno")
        print("4. Notas do Aluno")
        print("5. Sair")

        opcao = input("Digite sua opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            matricula = input("Matrícula: ")
            curso = input("Curso: ")
            data_nascimento = input("Data de Nascimento: ")
            aluno = Aluno(nome, matricula, curso, data_nascimento)
            sistema.adicionar_aluno(aluno)
            print("Aluno cadastrado com sucesso!")

        elif opcao == "2":
            nome = input("Nome do aluno a ser consultado: ")
            aluno = sistema.buscar_aluno_por_nome(nome)
            if aluno:
                print(aluno)
            else:
                print("Aluno não encontrado.")

        elif opcao == "3":
            matricula = input("Matrícula do aluno a ser excluído: ")
            sistema.excluir_aluno(matricula)

        elif opcao == "4":
            matricula = input("Matrícula do aluno para consultar notas: ")
            aluno = sistema.buscar_aluno_por_matricula(matricula)
            if aluno:
                notas = Notas()  # Aqui você pode adicionar notas ao aluno
                print(notas)
            else:
                print("Aluno não encontrado.")

        elif opcao == "5":
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
