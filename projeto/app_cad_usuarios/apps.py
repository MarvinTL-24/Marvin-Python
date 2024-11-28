from django.apps import AppConfig


class AppCadUsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_cad_usuarios'

class PollsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'