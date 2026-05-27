from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from auth_app.models import Permission
from auth_app.services.access import AdminManagePermission
from auth_app.serializers.permission import PermissionSerializer


class PermissionAPIView(APIView):
    permission_classes = [AdminManagePermission]

    def get(self, request):
        permissions = Permission.objects.all()
        serializer = PermissionSerializer(permissions, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = PermissionSerializer(data=request.data)

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
