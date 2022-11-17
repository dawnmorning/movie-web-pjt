from .models import Profile
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ('user',)