# accounts/serializers.py
from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed


# accounts/serializers.py
from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Adiciona o campo de senha

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role', 'is_active', 'is_staff', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')  # Pega a senha antes
        user = CustomUser(**validated_data)
        user.set_password(password)  # Aplica o hash na senha
        user.save()  # Salva o usuário com a senha hashada
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)  # Pega a senha, mas é opcional
        if password:
            instance.set_password(password)  # Se a senha foi fornecida, aplica o hash
        for attr, value in validated_data.items():
            setattr(instance, attr, value)  # Atualiza os outros atributos
        instance.save()  # Salva o usuário atualizado
        return instance


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)