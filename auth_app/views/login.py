from drf_spectacular.utils import extend_schema

from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from auth_app.serializers.login import LoginSerializer
from auth_app.utils.tokens import get_tokens_for_user


class LoginAPIView(APIView):
    """Вход пользователя по email и паролю"""
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    @extend_schema(tags=['Auth'])
    def post(self, request, *args, **kwargs) -> Response:
        """Вход в систему"""
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'error': serializer.errors}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data['user']
        return Response(data=get_tokens_for_user(user), status=status.HTTP_200_OK)
