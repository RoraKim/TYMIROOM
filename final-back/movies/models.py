from django.db import models
from django.conf import settings
from datetime import datetime, timedelta, timezone

# Create your models here.
class Genre(models.Model):
    id = models.IntegerField()
    genre_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

class Actor(models.Model):
    id = models.IntegerField()
    actor_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    profile_path = models.CharField(max_length=200)
    popularity = models.FloatField()
    
class Movie(models.Model):
    id = models.IntegerField()
    movie_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    release_date = models.DateField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    popularity = models.FloatField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    genres = models.ManyToManyField(Genre, related_name='genre_movies')
    actors = models.ManyToManyField(Actor, related_name='actor_movies')
    seen_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='seen_movies')
    wish_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='wish_movies')

class Review(models.Model):
    content = models.TextField()
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='review')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')

    @property
    def created_string(self):
        time = datetime.now(tz=timezone.utc) - self.created_at
        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.registered_date.date()
            return str(time.days) + '일 전'
        else:
            return self.created_at.date