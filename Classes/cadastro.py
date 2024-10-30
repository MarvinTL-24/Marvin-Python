from datetime import datetime

class Aluno:
    def __init__(self, nome, matricula, curso, data_nascimento):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.data_nascimento = data_nascimento
        self.notas = Notas()

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

    def idade(self):
        nascimento = datetime.strptime(self.data_nascimento, "%d/%m/%Y")
        hoje = datetime.now()
        return hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))

    def __str__(self):
        return (f"Nome: {self.nome}\n"
                f"Matrícula: {self.matricula}\n"
                f"Curso: {self.curso}\n"
                f"Data de Nascimento: {self.data_nascimento}\n"
                f"Notas:\n{self.notas}")

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
    cursos = {
        "Engenharia": ["Matemática", "Física", "Química"],
        "Administração": ["Economia", "Gestão", "Marketing"]
    }

    while True:
        print('-----------------------------------------------------------------------------------------------------')
        print("\nMenu Principal:")
        print("1. Cadastrar Aluno")
        print("2. Consultar Aluno")
        print("3. Excluir Aluno")
        print("4. Notas do Aluno")
        print("5. Adicionar Notas ao Aluno")
        print("6. Calcular Média do Aluno")
        print("7. Sair")
        print('-----------------------------------------------------------------------------------------------------')
        opcao = input("Digite sua opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            matricula = input("Matrícula: ")
            curso_nome = input("Curso (Engenharia/Administração): ")
            if curso_nome not in cursos:
                print("Curso inválido. Tente novamente.")
                continue
            data_nascimento = input("Data de Nascimento (DD/MM/YYYY): ")
            aluno = Aluno(nome, matricula, curso_nome, data_nascimento)
            if aluno.idade() < 0:
                print("Data de nascimento inválida. O aluno não pode ser cadastrado.")
                continue
            sistema.adicionar_aluno(aluno)
            print("Aluno cadastrado com sucesso!")
            print('-----------------------------------------------------------------------------------------------------')

        elif opcao == "2":
            nome = input("Nome do aluno a ser consultado: ")
            aluno = sistema.buscar_aluno_por_nome(nome)
            if aluno:
                print(aluno)
            else:
                print("Aluno não encontrado.")
            print('-----------------------------------------------------------------------------------------------------')

        elif opcao == "3":
            matricula = input("Matrícula do aluno a ser excluído: ")
            sistema.excluir_aluno(matricula)
            print('-----------------------------------------------------------------------------------------------------')

        elif opcao == "4":
            matricula = input("Matrícula do aluno para consultar notas: ")
            aluno = sistema.buscar_aluno_por_matricula(matricula)
            if aluno:
                print(aluno.notas)
            else:
                print("Aluno não encontrado.")
            print('-----------------------------------------------------------------------------------------------------')

        elif opcao == "5":
            matricula = input("Matrícula do aluno para adicionar notas: ")
            aluno = sistema.buscar_aluno_por_matricula(matricula)
            if aluno:
                for i in range(3):
                    disciplina = input(f"Disciplina {i + 1} ({', '.join(cursos[aluno.curso])}): ")
                    if disciplina in cursos[aluno.curso]:
                        try:
                            nota = float(input(f"Nota para {disciplina} (0 a 10): "))
                            aluno.notas.adicionar_nota(disciplina, nota)
                            print("Nota adicionada com sucesso!")
                        except ValueError:
                            print("Erro: Entrada inválida. Por favor, insira um número.")
                    else:
                        print("Disciplina inválida. Tente novamente.")
            else:
                print("Aluno não encontrado.")
            print('-----------------------------------------------------------------------------------------------------')

        elif opcao == "6":
            matricula = input("Matrícula do aluno para calcular média: ")
            aluno = sistema.buscar_aluno_por_matricula(matricula)
            if aluno:
                media = aluno.notas.calcular_media()
                print(f"Média das notas do aluno {aluno.nome}: {media:.2f}")
            else:
                print("Aluno não encontrado.")
            print('-----------------------------------------------------------------------------------------------------')

        elif opcao == "7":
            break

        else:
            print("Opção inválida!")
            print('-----------------------------------------------------------------------------------------------------')

if __name__ == "__main__":
    main()
