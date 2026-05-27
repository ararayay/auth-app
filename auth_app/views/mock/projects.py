from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from auth_app.services.access import HasAccessPermission


class ProjectReadPermission(HasAccessPermission):
    resource = 'projects'
    action = 'read'


class ProjectCreatePermission(HasAccessPermission):
    resource = 'projects'
    action = 'create'


class ProjectsAPIView(APIView):

    def get_permissions(self):
        if self.request.method == 'GET':
            return [ProjectReadPermission()]

        if self.request.method == 'POST':
            return [ProjectCreatePermission()]

        return super().get_permissions()

    def get(self, request):
        return Response([
            {'id': 1, 'name': 'Project Alpha'},
            {'id': 2, 'name': 'Project Beta'},
        ])

    def post(self, request):
        return Response(
            {
                'message': 'Project created',
                'data': request.data,
            },
            status=status.HTTP_201_CREATED
        )
