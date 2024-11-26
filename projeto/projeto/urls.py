urlpatterns = [
    # rota, view referente, nome de referência
    path('', views.home, name='home'),
    path('usuarios/', views.usuarios, name='listagem_usuarios')  # Adicionado aqui
]