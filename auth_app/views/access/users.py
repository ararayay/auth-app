from rest_framework.response import Response
from rest_framework.views import APIView

from auth_app.models import User
from auth_app.services.access import AdminManagePermission
from auth_app.serializers.user import UserSerializer


class UserListAPIView(APIView):
    permission_classes = [AdminManagePermission]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
