from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from auth_app.models import User


class UserSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password', 'password2')

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('User with this email already exists')
        return value

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'message': 'Passwords do not match'})
        return attrs

    def create(self, validated_data):
        return User.create_user(validated_data)
