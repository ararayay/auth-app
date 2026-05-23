from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from auth_app.models import User


class UserSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password', 'password2')

    def validate(self, attrs):
        if User.objects.filter(first_name=attrs['first_name'], last_name=attrs['last_name'], email=attrs['email']).exists():
            raise serializers.ValidationError({'message': 'User already exists'})
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'message': 'Passwords do not match'})
        return attrs

    def create(self, validated_data):
        return User.create_user(validated_data)
