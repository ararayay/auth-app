from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from auth_app.models import RolePermission
from auth_app.services.access import AdminManagePermission
from auth_app.serializers.role_permission import RolePermissionSerializer


class RolePermissionAPIView(APIView):
    permission_classes = [AdminManagePermission]

    def get(self, request):
        role_permissions = RolePermission.objects.all()
        serializer = RolePermissionSerializer(role_permissions, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = RolePermissionSerializer(data=request.data)

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
