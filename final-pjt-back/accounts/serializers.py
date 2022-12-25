from rest_framework import serializers, exceptions
from django.contrib.auth import get_user_model, authenticate
from rest_framework.validators import UniqueValidator
from django.core.validators import MinValueValidator, MaxValueValidator
from dj_rest_auth.registration.serializers import RegisterSerializer

User = get_user_model()

class UpdateUserSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(
        max_length=None, use_url=True,
    )
    class Meta:
        model = User
        fields = ('profile_image',)

class CustomRegisterSerializer(RegisterSerializer):
    # 기본 설정 필드: username, password, email
    # 추가 설정 필드: profile_image, nickname
    profile_image = serializers.ImageField(use_url=True, required=False)
    username = serializers.CharField(
        max_length=100,
        validators=[UniqueValidator(queryset=User.objects.all())]
        )
    nickname = serializers.CharField(
        max_length=100,
        validators=[UniqueValidator(queryset=User.objects.all())]
        )

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['profile_image'] = self.validated_data.get('profile_image', '')
        data['nickname'] = self.validated_data.get('nickname', '')
        return data

class NestedUserSerializer(serializers.ModelSerializer):
    grade = serializers.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        read_only=True)
 
    class Meta:
        model = User
        fields = ('id', 'username', 'nickname', 'profile_image', 'grade', 'followings')

class UserSerializer(serializers.ModelSerializer):
    grade = serializers.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        read_only=True)
    followings = NestedUserSerializer(source='followings.all', many=True, read_only=True)
    followers = NestedUserSerializer(source='followers.all', many=True, read_only=True)
    cnt_followings = serializers.IntegerField(source='followings.count', read_only=True)
    cnt_followers = serializers.IntegerField(source='followers.count',  read_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'nickname', 'profile_image',
            'grade', 'followings', 'followers','cnt_followings', 'cnt_followers',
            )
        read_only_fields = ('id', 'username', 'grade',)
