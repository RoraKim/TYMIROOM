from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import GuestBook, Profile, User
from .serializers.user import UserSerializer
from .serializers.profile import ProfileSerializer, ProfileUpdateSerializer
from .serializers.guestbook import GuestbookSerializer
from .serializers.follow import FollowSerializer

@api_view(['GET'])
def user_list(request, username):
    users = User.objects.filter(username__contains=username).all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def follow(request, username):
    person = get_object_or_404(User, username=username)
    user = request.user
    if person != user:
        if person.followings.filter(id=user.pk).exists():
            person.followings.remove(user)
        else:
            person.followings.add(user)
    serializer = ProfileSerializer(person)
    return Response(serializer.data)

@api_view(['GET'])
def followers(request, username):
    user = get_object_or_404(User, username=username)
    serializer = FollowSerializer(user)
    return Response(serializer.data)


@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    if not Profile.objects.filter(user_id = user.pk).exists():
        Profile.objects.create(user_id = user.pk)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)

@api_view(['POST'])
def profile_update(request):
    profile = get_object_or_404(Profile, user_id = request.user.id)
    serializer = ProfileUpdateSerializer(instance=profile, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)

@api_view(['POST'])
def guestbook_create(request, username):
    user = get_object_or_404(User, username=username)
    serializer = GuestbookSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save(friend = request.user, me = user)
        serializer = ProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT', 'DELETE'])
def guestbook_update_delete(request, username, guestbook_id):
    user = get_object_or_404(User, username=username)
    guestbook = get_object_or_404(GuestBook, id=guestbook_id)

    def update_guestbook():
        if request.user == guestbook.friend:
            serializer = GuestbookSerializer(instance=guestbook, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                serializer = ProfileSerializer(user)
                return Response(serializer.data)

    def delete_guestbook():
        if request.user == guestbook.friend:
            guestbook.delete()
            serializer = ProfileSerializer(user)
            return Response(serializer.data)
    
    if request.method == 'PUT':
        return update_guestbook()
    elif request.method == 'DELETE':
        return delete_guestbook()
