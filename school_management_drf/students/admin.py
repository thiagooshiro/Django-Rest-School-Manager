from django.contrib import admin
from django.utils.html import mark_safe
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'registration_number', 'email', 'profile_picture_display')  # Atualize o nome da coluna
    search_fields = ('name', 'registration_number', 'email')

    # Personalize a exibição da imagem
    def profile_picture_display(self, obj):
        if obj.profile_picture:
            return mark_safe(f'<img src="{obj.profile_picture.url}" width="50" height="50" />')
        return 'No Image'

    profile_picture_display.short_description = 'Profile Picture'  # Nome da coluna no admin
