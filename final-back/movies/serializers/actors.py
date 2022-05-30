from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Actor, Movie

class ActorSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title', 'poster_path', 'release_date', 'popularity',)

    actor_movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = '__all__'