from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import GuestBook

user = get_user_model()

class GuestbookSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = user
            fields = ('id',)

    user = UserSerializer(read_only=True)
    me = UserSerializer(read_only=True)
    friend = UserSerializer(read_only=True)

    class Meta:
        model = GuestBook
        fields = '__all__'