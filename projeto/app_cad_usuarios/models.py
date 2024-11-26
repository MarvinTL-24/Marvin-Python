from django.db import models

class Usuario(models.Model):
    # Dados Pessoais
    nome = models.CharField(max_length=200)
    idade = models.IntegerField()
    data_nascimento = models.DateField()

    # Dados Profissionais
    ESCOLARIDADE_CHOICES = [
        ('Ensino fundamental','Ensino fundamental'),
        ('Ensino Médio','Ensino Médio'),
        ('Universitário','Universitário'),
        ('Formado','Formado'),
    ]
    escolaridade = models.CharField(max_length=20, choices=ESCOLARIDADE_CHOICES)
    email = models.EmailField(max_length=255)
    
    EXPERIENCIA_CHOICES = [
        ('Sim','Sim'),
        ('Não','Não'),
    ]
    experiencia_ti = models.CharField(max_length=3, choices=EXPERIENCIA_CHOICES)

    # Disponibilidade
    DISPONIBILIDADE_CHOICES = [
        ('M','M'),
        ('T','T'),
        ('N','N'),
    ]
    disponibilidade = models.ManyToManyField('Disponibilidade', blank=True)

    def __str__(self):
        return self.nome


class Disponibilidade(models.Model):
    valor = models.CharField(max_length=1, choices=Usuario.DISPONIBILIDADE_CHOICES)

    def __str__(self):
        return self.get_valor_display()
