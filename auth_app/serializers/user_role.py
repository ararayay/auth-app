from rest_framework import serializers

from auth_app.models import UserRole


class UserRoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserRole
        fields = '__all__'
        