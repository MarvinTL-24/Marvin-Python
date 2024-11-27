from django.shortcuts import render

def home(request):
    return render(request, 'usuario/home.html')

# Adicionado aqui
def usuarios(request):
    if request.method == 'POST':
        # Criar um novo usuário com os dados do formulário
        novo_usuario = Usuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.idade = request.POST.get('idade')
        novo_usuario.data_nascimento = request.POST.get('data_nascimento')
        novo_usuario.escolaridade = request.POST.get('escolaridade')
        novo_usuario.email = request.POST.get('email')
        novo_usuario.experiencia_ti = request.POST.get('experiencia_ti')

        # Salvar o novo usuário
        novo_usuario.save()

        # Associar a disponibilidade (campo ManyToMany)
        disponibilidades = request.POST.getlist('disponibilidade')  # recebe uma lista de valores
        for valor in disponibilidades:
            # Verifica se a disponibilidade já existe, se não, cria um novo objeto
            disponibilidade_obj, created = Disponibilidade.objects.get_or_create(valor=valor)
            novo_usuario.disponibilidade.add(disponibilidade_obj)
        
        # Salvar as alterações no banco de dados
        novo_usuario.save()

        # Redireciona para a página de usuários
        return redirect('usuarios')

    # Quando o método não for POST, exibe a lista de usuários já cadastrados
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/usuarios.html', {'usuarios': usuarios})
