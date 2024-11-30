from rest_framework import serializers
from django.utils.timezone import now
from .models import Student
from courses.models import Course  # Certifique-se de importar o modelo de Course para buscar os nomes diretamente

class StudentSerializer(serializers.ModelSerializer):
    # Permite atualizar os cursos com seus IDs
    courses = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), many=True)

    class Meta:
        model = Student
        fields = ['id', 'name', 'registration_number', 'email', 'date_of_birth', 'profile_picture', 'courses']

    def validate_date_of_birth(self, value):
        if value > now().date():
            raise serializers.ValidationError("A data de nascimento não pode ser no futuro.")
        return value

    def validate_name(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError("O nome deve ter pelo menos 3 caracteres.")
        return value

    def validate_registration_number(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("O número de matrícula deve conter apenas números.")
        return value

    def to_representation(self, instance):
        # Personalizando a representação para mostrar os nomes dos cursos
        representation = super().to_representation(instance)
        
        # Modificando o campo 'courses' para mostrar os nomes dos cursos em vez dos IDs
        if 'courses' in representation:
            course_names = [course.name for course in instance.courses.all()]
            representation['courses'] = course_names  # Agora vamos retornar os nomes
        
        return representation
