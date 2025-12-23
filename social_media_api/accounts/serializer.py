from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password','bio', 'profile_picture']

    def create(self, validate_data):
        password = validate_data.pop('password')
        user = User.objects.create_user(
            password=password,
            **validate_data
        )
        return user