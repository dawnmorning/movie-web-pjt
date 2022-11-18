from django.shortcuts import get_object_or_404
from .models import User, Profile
from .serializers import ProfileSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
# Create your views here.


@api_view(["GET", "PUT"])
@permission_classes([IsAuthenticated])
def profile_ru(request, username):
    person = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=person)

    if request.method == "PUT":
        if request.user != person:
            return Response({'message': '해당 작업의 권한이 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)
            
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
