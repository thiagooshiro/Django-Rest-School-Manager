from rest_framework import viewsets
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
import logging

# Configuração do logger
logger = logging.getLogger(__name__)

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]  # Apenas usuários autenticados podem acessar as views


class CustomLoginView(APIView):
    permission_classes = [AllowAny]  # Permite que qualquer um tente logar

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        
        if not username or not password:
            # Loga a tentativa de login sem os parâmetros necessários
            logger.warning("Login falhou: parâmetros de login ausentes.")
            raise AuthenticationFailed("Usuário e senha são obrigatórios.")

        try:
            # Busca o usuário diretamente pelo nome de usuário
            user = CustomUser.objects.get(username=username)

            # Verifica se a senha fornecida corresponde à senha armazenada
            if not user.check_password(password):
                logger.warning(f"Tentativa de login falhou para o usuário {username}. Senha incorreta.")
                raise AuthenticationFailed("Credenciais inválidas.")
            
            # Se a senha estiver correta, gera o token
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)
            
            # Loga o sucesso do login
            logger.info(f"Usuário {username} autenticado com sucesso.")
            
            return Response(
                {"access": access_token, "refresh": refresh_token},
                status=status.HTTP_200_OK
            )
        except CustomUser.DoesNotExist:
            # Loga a falha na busca pelo usuário
            logger.warning(f"Tentativa de login falhou para o usuário {username}. Usuário não encontrado.")
            raise AuthenticationFailed("Credenciais inválidas.")

# View para renovar o token de acesso com o refresh token
class CustomTokenRefreshView(TokenRefreshView):
    pass
