from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from django.core.validators import MinValueValidator, MaxValueValidator
from dj_rest_auth.registration.serializers import RegisterSerializer

User = get_user_model()

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

class UserSerializer(serializers.ModelSerializer):
    grade = serializers.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        read_only=True)
 
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'is_active', 'nickname', 'profile_image','grade',)
        read_only_fields = ('id', 'username', 'is_active','grade',)


# class ProfileSerializer(serializers.ModelSerializer):
#     user = UserSerializer(read_only=True)

#     class Meta:
#         model = Profile
#         fields = '__all__'
#         read_only_fields = ('user',)