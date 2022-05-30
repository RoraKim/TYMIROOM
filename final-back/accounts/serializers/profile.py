from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Profile, GuestBook
from movies.models import Movie



class ProfileSerializer(serializers.ModelSerializer):

    class UserProfileSerializer(serializers.ModelSerializer):
        class Meta:
            model = Profile
            fields = ('tymi_image', 'room_image', 'level', 'exp', 'life_movie')

    class GuestbookSerializer(serializers.ModelSerializer):
        class UserSerializer(serializers.ModelSerializer):
            class Meta:
                model = get_user_model()
                fields = ('id', 'username')
        friend = UserSerializer(read_only=True)
        class Meta:
            model = GuestBook
            fields = ('id', 'content', 'friend', 'created_string')
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'username')

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('movie_id', 'title', 'poster_path', 'release_date', 'popularity', 'genres', 'wish_users')
    wish_movies = MovieSerializer(many=True, read_only=True)
    guestbook_me = GuestbookSerializer(many=True, read_only=True)
    profile_set = UserProfileSerializer(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('profile_set', 'guestbook_me', 'wish_movies', 'username',)

class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'