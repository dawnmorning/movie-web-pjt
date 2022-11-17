from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  # 기존에 사용하는 User 관리 interface 설정
from .models import User  # 새롭게 등록한 User 모델

# Register your models here.
admin.site.register(User, UserAdmin)