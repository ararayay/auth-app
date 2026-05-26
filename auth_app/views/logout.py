from drf_spectacular.utils import extend_schema

from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken


class LogoutAPIView(APIView):
    """Выход из системы - инвалидация refresh-токена"""
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(tags=['Auth'])
    def post(self, request, *args, **kwargs) -> Response:
        """Выход из системы"""
        refresh_token = request.data.get('refresh')
        if not refresh_token:
            return Response(data={'error': 'Refresh token is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except TokenError:
            return Response(data={'error': 'Invalid or expired refresh token'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_204_NO_CONTENT)
