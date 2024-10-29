alunos = {}

def cadastrar_aluno():
    nome = input("Nome do aluno: ")
    matricula = input("Matrícula do aluno: ")
    curso = input("Curso do aluno: ")
    nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    alunos[matricula] = {
        'nome': nome,
        'curso': curso,
        'nascimento': nascimento
    }
    print("Aluno cadastrado com sucesso!")

def consultar_aluno():
    pesquisa = input("Pesquisar por nome ou matrícula: ")
    encontrado = False
    for matricula, dados in alunos.items():
        if pesquisa.lower() in dados['nome'].lower() or pesquisa == matricula:
            print(f"Matrícula: {matricula}, Nome: {dados['nome']}, Curso: {dados['curso']}, Data de Nascimento: {dados['nascimento']}")
            encontrado = True
    if not encontrado:
        print("Aluno não encontrado.")

def excluir_aluno():
    matricula = input("Matrícula do aluno a ser excluído: ")
    if matricula in alunos:
        del alunos[matricula]
        print("Aluno excluído com sucesso!")
    else:
        print("Aluno não encontrado.")

def pesquisar_por_curso():
    curso = input("Digite o nome do curso: ")
    encontrados = [dados for dados in alunos.values() if dados['curso'].lower() == curso.lower()]
    if encontrados:
        for dados in encontrados:
            print(f"Nome: {dados['nome']}, Curso: {dados['curso']}")
    else:
        print("Nenhum aluno encontrado nesse curso.")

def gerar_relatorio():
    criterio = input("Ordenar por (nome, curso ou nascimento): ")
    if criterio in ['nome', 'curso', 'nascimento']:
        alunos_ordenados = sorted(alunos.items(), key=lambda x: x[1][criterio])
        for matricula, dados in alunos_ordenados:
            print(f"Matrícula: {matricula}, Nome: {dados['nome']}, Curso: {dados['curso']}, Data de Nascimento: {dados['nascimento']}")
    else:
        print("Critério de ordenação inválido.")

def salvar_dados():
    # TODO: Implementar a funcionalidade de salvar dados
    print("Salvar dados - ainda não implementado")

while True:
    print("\nMenu Principal:")
    print("1. Cadastrar aluno")
    print("2. Consultar aluno")
    print("3. Excluir aluno")
    print("4. Pesquisar por curso")
    print("5. Gerar relatório")
    print("6. Salvar dados")
    print("7. Sair")
        
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        cadastrar_aluno()
    elif opcao == '2':
        consultar_aluno()
    elif opcao == '3':
        excluir_aluno()
    elif opcao == '4':
        pesquisar_por_curso()
    elif opcao == '5':
        gerar_relatorio()
    elif opcao == '6':
        salvar_dados()
    elif opcao == '7':
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
