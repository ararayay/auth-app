from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from auth_app.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'second_name', 'email')
        read_only_fields = ('id', 'username')

    def validate_email(self, value):
        queryset = User.objects.filter(email=value)
        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)
        if queryset.exists():
            raise serializers.ValidationError('User with this email already exists')
        return value


