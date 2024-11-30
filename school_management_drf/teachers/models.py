from django.db import models
from django.core.exceptions import ValidationError
from django.utils.timezone import localdate
from courses.models import Course

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='teachers')  # Relaciona com o modelo Course
    date_of_birth = models.DateField()
    hire_date = models.DateField(default=localdate)  # Usando localdate para pegar apenas a data
    profile_picture = models.ImageField(upload_to='teacher_pics/', blank=True, null=True)

    def clean(self):
        # Validação para evitar datas de nascimento no futuro
        if self.date_of_birth > localdate():
            raise ValidationError("A data de nascimento não pode ser no futuro.")
    
    def __str__(self):
        return self.name
