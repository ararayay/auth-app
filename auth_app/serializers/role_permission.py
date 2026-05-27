from rest_framework import serializers

from auth_app.models import RolePermission


class RolePermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = RolePermission
        fields = '__all__'
