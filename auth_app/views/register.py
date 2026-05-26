from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from auth_app.serializers.user import UserSerializer
from auth_app.utils.tokens import get_tokens_for_user


class RegisterAPIView(APIView):
    """Регистрация пользователя"""
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs) -> Response:
        try:
            serializer = UserSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(data={'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

            user = serializer.save()
            return Response(data=get_tokens_for_user(user), status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response(data={'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
