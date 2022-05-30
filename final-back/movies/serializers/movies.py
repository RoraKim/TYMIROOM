from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Genre, Movie, Review, Actor

user = get_user_model()

class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('movie_id', 'title', 'poster_path', 'release_date', 'popularity', 'genres', 'wish_users')

class MovieDetailSerializer(serializers.ModelSerializer):

    class ActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('actor_id', 'name', 'profile_path')

    class ReviewSerializer(serializers.ModelSerializer):
        
        class UserSerializer(serializers.ModelSerializer):
            class Meta:
                model = get_user_model()
                fields = ('username',)
        user = UserSerializer(read_only=True)
        class Meta:
            model = Review
            fields = '__all__'

    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('name',)

    review_set = ReviewSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = user
            fields = ('id',)
    
    movie = MovieSerializer(read_only=True)
    like_users = UserSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
