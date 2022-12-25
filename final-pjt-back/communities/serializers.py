from .models import Review, Comment
from rest_framework import serializers
from accounts.serializers import UserSerializer
from movies.serializers import MovieSerializer
from django.contrib.auth import get_user_model

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    like_users = UserSerializer(read_only=True, many=True)
    cnt_like_users = serializers.IntegerField(source='like_users.count', read_only=True)


    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('like_users', 'review', 'author', 'created_at')

class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    author = UserSerializer(read_only=True)
    like_users = UserSerializer(read_only=True, many=True)
    cnt_like_users = serializers.IntegerField(source='like_users.count', read_only=True)
    comments = CommentSerializer(source='comment_set.all', read_only=True, many=True)
    cnt_comments = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie', 'author', 'like_users',)