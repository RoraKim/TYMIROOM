from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Genre, Movie

class GenreSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('movie_id','title', 'poster_path', 'release_date', 'popularity',)
    
    genre_movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = '__all__'
