from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from auth_app.models import Role
from auth_app.services.access import AdminManagePermission
from auth_app.serializers.role import RoleSerializer


class RoleAPIView(APIView):
    permission_classes = [AdminManagePermission]

    def get(self, request):
        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = RoleSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )