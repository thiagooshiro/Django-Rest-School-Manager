# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    role = models.CharField(max_length=50, choices=[
        ('admin', 'Admin'),
        ('teacher', 'Professor'),
        ('coordinator', 'Coordenador'),
        ('assistant', 'Assistente Administrativo'),
        ('student', 'Aluno'),
    ]) 


