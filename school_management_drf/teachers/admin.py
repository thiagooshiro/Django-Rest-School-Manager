from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'registration_number', 'email', 'course', 'hire_date')  # Exibe o curso
    search_fields = ('name', 'registration_number', 'email', 'course__name')  # Permite busca pelo curso
