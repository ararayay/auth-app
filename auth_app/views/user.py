from drf_spectacular.utils import extend_schema

from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from auth_app.serializers.user import UserSerializer


class UserAPIView(APIView):
    """Просмотр, обновление и мягкое удаление профиля текущего пользователя"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    @extend_schema(tags=['User'])
    def get(self, request, *args, **kwargs) -> Response:
        """Получить профиль"""
        serializer = UserSerializer(request.user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @extend_schema(tags=['User'])
    def patch(self, request, *args, **kwargs) -> Response:
        """Обновить профиль"""
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(data={'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @extend_schema(tags=['User'])
    def delete(self, request, *args, **kwargs) -> Response:
        """Удалить аккаунт (мягкое удаление)"""
        refresh_token = request.data.get('refresh')
        if refresh_token:
            try:
                RefreshToken(refresh_token).blacklist()
            except TokenError:
                return Response(data={'error': 'Invalid or expired refresh token'}, status=status.HTTP_400_BAD_REQUEST)

        user = request.user
        user.is_active = False
        user.save(update_fields=['is_active'])

        return Response(status=status.HTTP_204_NO_CONTENT)
