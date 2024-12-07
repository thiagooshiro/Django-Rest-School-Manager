from django.db import models
from django.core.exceptions import ValidationError
from django.utils.timezone import now
from courses.models import Course  # Importando o modelo Course para usar o relacionamento

class Student(models.Model):
    name = models.CharField(max_length=100, validators=[])
    registration_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    profile_picture = models.ImageField(upload_to=f'profile_pics/{registration_number}/', blank=True, null=True)  # Adiciona o campo de imagem
    courses = models.ManyToManyField(Course, related_name='students', blank=True)  # Relaciona com o modelo Course

    def clean(self):
        # Verificar se a data de nascimento é no futuro
        if self.date_of_birth > now().date():
            raise ValidationError("A data de nascimento não pode ser no futuro.")
    
    def __str__(self):
        return self.name
