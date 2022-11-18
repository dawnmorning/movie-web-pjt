from .models import Review, Comment
from rest_framework import serializers
from accounts.serializers import ProfileSerializer
from movies.serializers import MovieSerializer

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('like_users', 'review', 'author',)

class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    profile = ProfileSerializer(read_only=True)
    comments = CommentSerializer(source='comment_set.all', read_only=True ,many=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie', 'author', 'like_users', 'profile')