from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from auth_app.services.access import HasAccessPermission


class ReportReadPermission(HasAccessPermission):
    resource = 'reports'
    action = 'read'


class ReportCreatePermission(HasAccessPermission):
    resource = 'reports'
    action = 'create'


class ReportsAPIView(APIView):

    def get_permissions(self):
        if self.request.method == 'GET':
            return [ReportReadPermission()]

        if self.request.method == 'POST':
            return [ReportCreatePermission()]

        return super().get_permissions()

    def get(self, request):
        return Response([
            {'id': 1, 'title': 'Annual Report'},
        ])

    def post(self, request):
        return Response(
            {
                'message': 'Report created',
                'data': request.data,
            },
            status=status.HTTP_201_CREATED
        )
