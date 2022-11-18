from .models import Review, Comment
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('like_users', 'review', 'user',)

class ReviewSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True,many=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie', 'user', 'like_users',)