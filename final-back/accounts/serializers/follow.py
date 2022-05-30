from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Profile, GuestBook

class FollowSerializer(serializers.ModelSerializer):

    class FollowersSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'username',)
    followings = FollowersSerializer(many=True, read_only=True)
    followers = FollowersSerializer(many=True, read_only=True)
    class Meta:
        model = get_user_model()
        fields = ('username', 'followings', 'followers')