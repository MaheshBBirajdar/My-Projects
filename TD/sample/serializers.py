from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        


class PostSerializer(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = '__all__'

    def get_like_count(self, post):
        return post.like_set.count()


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['lid', 'post', 'user']