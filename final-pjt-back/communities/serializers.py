from .models import Review, Comment
from rest_framework import serializers
from accounts.serializers import UserSerializer
from movies.serializers import MovieSerializer
from django.contrib.auth import get_user_model

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    like_users = UserSerializer(read_only=True ,many=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('like_users', 'review', 'author',)

class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    author = UserSerializer(read_only=True)
    like_users = UserSerializer(read_only=True, many=True)
    comments = CommentSerializer(source='comment_set.all', read_only=True ,many=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie', 'author', 'like_users',)