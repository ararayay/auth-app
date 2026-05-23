from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from auth_app.serializers.user import UserSerializer


class RegisterAPIView(APIView):
    """Регистрация пользователя"""
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs) -> Response:
        try:
            serializer = UserSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(data={'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            refresh.payload.update({'user_id': user.id, 'first_name': user.first_name, 'last_name': user.last_name})
            return Response(data={'refresh': str(refresh), 'access': str(refresh.access_token)},
                            status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response(data={'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
