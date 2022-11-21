from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
# Create your views here.

User = get_user_model()

@api_view(["GET", "PUT"])
@permission_classes([IsAuthenticated])
def user_ru(request, username):
    person = get_object_or_404(User, username=username)

    if request.method == "PUT":
        if request.user != person:
            return Response({'message': '해당 작업의 권한이 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)
            
        serializer = UserSerializer(person, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'GET':
        serializer = UserSerializer(person)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def follow(request, username):
    User = get_user_model()
    me = request.user
    you = User.objects.get(username=username)

    if me != you:
        if you.followers.filter(pk=me.pk).exists():
            you.followers.remove(me)
            is_following = False
        else:
            you.followers.add(me)
            is_following = True
    
    followers = list(you.followers.all().values('id', 'nickname', 'profile_image', 'grade'))

    context = {
        'is_following': is_following,
        'followers': followers,
        'cnt_followers': you.followers.count(),
        'cnt_followings': you.followings.count(),
    }
    print(context)
    
    return Response(context)