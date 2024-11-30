from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import Student
from django.utils.timezone import now

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'registration_number', 'email', 'date_of_birth', 'profile_picture' ]

    def validate_date_of_birth(self, value):
        """
        Validação personalizada para garantir que a data de nascimento não seja no futuro.
        """
        if value > now().date():
            raise serializers.ValidationError("A data de nascimento não pode ser no futuro.")
        return value

    def validate_name(self, value):
        """
        Validação personalizada para o campo 'name' (nome do estudante).
        """
        if len(value.strip()) < 3:
            raise serializers.ValidationError("O nome deve ter pelo menos 3 caracteres.")
        return value

    def validate_registration_number(self, value):
        """
        Validação personalizada para o campo 'registration_number'.
        """
        if not value.isdigit():
            raise serializers.ValidationError("O número de matrícula deve conter apenas números.")
        return value
