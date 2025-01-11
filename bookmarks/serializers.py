from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Bookmark

class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ['id', 'user', 'title', 'url', 'category', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']  

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
