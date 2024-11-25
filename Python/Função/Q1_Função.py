alunos = {}

def cadastrar_aluno():
    nome = input("Nome do aluno: ")
    sexo = input("Sexo do aluno: ")
    curso = input("Curso do aluno: ")
    nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    RG = input("RG do aluno: ")
    cidade = input("Cidade do aluno: ")
    local = input("Endereço do aluno: ")
    grau_escolaridade = input("Grau de Escolaridade atual: ")
    
    # Coletando os nomes dos pais
    pais = []
    pai = input("Digite o nome do pai: ")
    pais.append(pai)
    mae = input("Digite o nome da mãe: ")
    pais.append(mae)

    telefone = input("Digite o telefone do aluno: ")
    estado = input("Digite o estado do aluno: ")

    alunos[RG] = {
        'nome': nome,
        'sexo': sexo,
        'curso': curso,
        'nascimento': nascimento,
        'cidade': cidade,
        'endereco': local,
        'grau_escolaridade': grau_escolaridade,
        'pais': pais,
        'telefone': telefone,
        'estado': estado
    }
    print("Aluno cadastrado com sucesso!")

def consultar_aluno():
    pesquisa = input("Pesquisar por nome ou RG: ")
    encontrado = False
    for rg, dados in alunos.items():
        if pesquisa.lower() in dados['nome'].lower() or pesquisa == rg:
            print(f"RG: {rg}, Nome: {dados['nome']}, Sexo: {dados['sexo']}, Curso: {dados['curso']}, Data de Nascimento: {dados['nascimento']}")
            encontrado = True
    if not encontrado:
        print("Aluno não encontrado.")

def excluir_aluno():
    rg = input("RG do aluno a ser excluído: ")
    if rg in alunos:
        del alunos[rg]
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
    criterio = input("Pode-se criar um relatorio com um dos seguintes dados.\nDigite o dado que souber dentre (nome, curso, nascimento, RG, cidade, endereco, grau_escolaridade, pais, telefone, estado): ")
    if criterio in ['nome', 'curso', 'nascimento', 'RG', 'cidade', 'endereco', 'grau_escolaridade', 'pais', 'telefone', 'estado']:
        alunos_ordenados = sorted(alunos.items(), key=lambda x: x[1][criterio])
        for rg, dados in alunos_ordenados:
            print(f"RG: {rg}, Nome: {dados['nome']}, Curso: {dados['curso']}, Data de Nascimento: {dados['nascimento']}, "
                  f"Cidade: {dados['cidade']}, Endereço: {dados['endereco']}, Nome dos pais: {', '.join(dados['pais'])}, "
                  f"Telefone: {dados['telefone']}, Grau de escolaridade: {dados['grau_escolaridade']}, Estado: {dados['estado']}")
    else:
        print("Critério de ordenação inválido.")

def salvar_dados():
    # TODO: Implementar a funcionalidade de salvar dados
    print("Salvar dados - ainda não implementado")

print('-----------------------------------------------------------------------------------------------------')
while True:
    print("\nMenu Principal:")
    print("1. Cadastrar aluno")
    print("2. Consultar aluno")
    print("3. Excluir aluno")
    print("4. Pesquisar por curso")
    print("5. Gerar relatório")
    print("6. Salvar dados")
    print("7. Sair")
    print('-----------------------------------------------------------------------------------------------------')

    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        print('-----------------------------------------------------------------------------------------------------')
        cadastrar_aluno()
        print('-----------------------------------------------------------------------------------------------------')
    elif opcao == '2':
        print('-----------------------------------------------------------------------------------------------------')
        consultar_aluno()
        print('-----------------------------------------------------------------------------------------------------')
    elif opcao == '3':
        print('-----------------------------------------------------------------------------------------------------')
        excluir_aluno()
        print('-----------------------------------------------------------------------------------------------------')
    elif opcao == '4':
        print('-----------------------------------------------------------------------------------------------------')
        pesquisar_por_curso()
        print('-----------------------------------------------------------------------------------------------------')
    elif opcao == '5':
        print('-----------------------------------------------------------------------------------------------------')
        gerar_relatorio()
        print('-----------------------------------------------------------------------------------------------------')
    elif opcao == '6':
        print('-----------------------------------------------------------------------------------------------------')
        salvar_dados()
        print('-----------------------------------------------------------------------------------------------------')
    elif opcao == '7':
        print('-----------------------------------------------------------------------------------------------------')
        print("Saindo do programa.")
        print('-----------------------------------------------------------------------------------------------------')
        break
    else:
        print('-----------------------------------------------------------------------------------------------------')
        print("Opção inválida. Tente novamente.")
        print('-----------------------------------------------------------------------------------------------------')
