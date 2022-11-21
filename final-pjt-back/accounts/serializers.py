from rest_framework import serializers, exceptions
from django.contrib.auth import get_user_model, authenticate
from rest_framework.validators import UniqueValidator
from django.core.validators import MinValueValidator, MaxValueValidator
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
User = get_user_model()

# class CustomLoginSerializer(LoginSerializer):
    
#     username = serializers.CharField(required=False, allow_blank=True)
#     email = serializers.EmailField(required=False, allow_blank=True)
#     password = serializers.CharField(style={'input_type': 'password'})
#     profile_image = serializers.ImageField(use_url=True, required=False)
#     nickname = serializers.CharField(
#         max_length=100,
#         validators=[UniqueValidator(queryset=User.objects.all())]
#         read_only=True
#         )

#     def authenticate(self, **kwargs):
#         return authenticate(self.context['request'], **kwargs)

#     def _validate_email(self, email, password):
#         if email and password:
#             user = self.authenticate(email=email, password=password)
#         else:
#             msg = _('Must include "email" and "password".')
#             raise exceptions.ValidationError(msg)

#         return user

#     def _validate_username(self, username, password):
#         if username and password:
#             user = self.authenticate(username=username, password=password)
#         else:
#             msg = ('Must include "username" and "password".')
#             raise exceptions.ValidationError(msg)
#         print(user)
#         return user



class CustomRegisterSerializer(RegisterSerializer):
    # 기본 설정 필드: username, password, email
    # 추가 설정 필드: profile_image    class Meta:
    profile_image = serializers.ImageField(use_url=True, required=False)
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
        model = get_user_model()
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
        model = get_user_model()
        fields = (
            'id', 'username', 'email', 'nickname', 'profile_image',
            'grade', 'followings', 'followers','cnt_followings', 'cnt_followers',
            )
        read_only_fields = ('id', 'username', 'grade',)
