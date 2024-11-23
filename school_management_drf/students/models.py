from django.db import models
from django.core.exceptions import ValidationError
from django.utils.timezone import now

class Student(models.Model):
    name = models.CharField(max_length=100, validators=[])
    registration_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    # school = models.ForeignKey('School', on_delete=models.CASCADE, related_name='students')

    def clean(self):
        # Verificar se a data de nascimento é no futuro
        if self.date_of_birth > now().date():
            raise ValidationError("A data de nascimento não pode ser no futuro.")
    
    def __str__(self):
        return self.name
