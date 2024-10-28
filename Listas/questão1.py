alunos = {}

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
    
    elif opcao == '2':
        pesquisa = input("Pesquisar por nome ou matrícula: ")
        encontrado = False
        for matricula, dados in alunos.items():
            if pesquisa.lower() in dados['nome'].lower() or pesquisa == matricula:
                print(f"Matrícula: {matricula}, Nome: {dados['nome']}, Curso: {dados['curso']}, Data de Nascimento: {dados['nascimento']}")
                encontrado = True
        if not encontrado:
            print("Aluno não encontrado.")
    
    elif opcao == '3':
        matricula = input("Matrícula do aluno a ser excluído: ")
        if matricula in alunos:
            del alunos[matricula]
            print("Aluno excluído com sucesso!")
        else:
            print("Aluno não encontrado.")
    
    elif opcao == '4':
        curso = input("Digite o nome do curso: ")
        encontrados = [dados for dados in alunos.values() if dados['curso'].lower() == curso.lower()]
        if encontrados:
            for dados in encontrados:
                print(f"Nome: {dados['nome']}, Matrícula: {matricula}")
        else:
            print("Nenhum aluno encontrado nesse curso.")
    
    elif opcao == '5':
        criterio = input("Ordenar por (nome, curso ou nascimento): ")
        if criterio in ['nome', 'curso', 'nascimento']:
            alunos_ordenados = sorted(alunos.items(), key=lambda x: x[1][criterio])
            for matricula, dados in alunos_ordenados:
                print(f"Matrícula: {matricula}, Nome: {dados['nome']}, Curso: {dados['curso']}, Data de Nascimento: {dados['nascimento']}")
        else:
            print("Critério de ordenação inválido.")
    
    elif opcao == '6':
        # TODO : SALVAR
        print("Salvar dados - ainda não sei")
    
    elif opcao == '7':
        print("Saindo do programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")
