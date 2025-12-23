from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password','bio', 'profile_picture']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = get_user_model().objects.create_user(
            password=password,
            **validated_data
        )
        #create a token immediately after registration
        Token.objects.create(user=user)
        return user
    """
    serializers.CharField()
    """
     
