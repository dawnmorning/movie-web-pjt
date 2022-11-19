from .models import Profile

from rest_framework import serializers
# from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'id',)

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ('user',)