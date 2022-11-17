from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.core.validators import MinValueValidator
# Create your models here.

class User(AbstractUser):

    def __str__(self):
        return self.username

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # primary_key를 User의 pk로 설정하여 통합적으로 관리
    nickname = models.CharField(max_length=128)
    interested = models.CharField(max_length=128)
    # 업로드할 경로, 이미지를 선택하지 않았을 때 대신 올라갈 기본값 설정
    profile_image = ProcessedImageField(
        blank=True,
        upload_to='profile/%Y/%m',
        processors=[ResizeToFill(300, 300)],
        format='JPEG',
        options={'quality': 70},
        default='default.jpg',
    )
    grade = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)],
    )

# User모델이 post_save 이벤트를 발생시켰을 때 해당 이벤트가 일어났다는 사실을 받음
@receiver(post_save, sender=User)                               # 프로필을 생성해주는 코드를 직접 작성하지 않아도 알아서 유저 생성 이벤트를 감지하여 프로필 자동 생성
def create_user_profile(sender, instance, created, **kwargs):   # 해당 유저 인스턴스와 연결되는 프로필 데이터를  생성
    if created:                                                  
        Profile.objects.create(user=instance) 