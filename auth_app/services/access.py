from auth_app.models import RolePermission

from rest_framework.permissions import BasePermission


class HasAccessPermission(BasePermission):
    resource = None
    action = None

    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False

        return RolePermission.objects.filter(
            role__userrole__user=user,
            permission__resource=self.resource,
            permission__action=self.action
        ).exists()


class AdminManagePermission(HasAccessPermission):
    resource = 'admin'
    action = 'manage'
