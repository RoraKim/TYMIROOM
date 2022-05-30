from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Movie, Review, Genre, Actor
from .serializers.movies import (
    MovieSerializer, 
    MovieDetailSerializer, 
    ReviewSerializer,
    )
from .serializers.genres import GenreSerializer
from .serializers.actors import ActorSerializer
from django.core.paginator import Paginator
# Create your views here.

@api_view(['GET'])
def movie_list(request):
    if request.GET.get('page'):
        page_number = int(request.GET.get('page')) # 현재 페이지 넘버
    else:
        page_number = 1
    movies = Movie.objects.order_by('title')[(page_number-1) * 18: page_number * 18]
    if request.GET.get('search'):
        search = request.GET.get('search')
        movies = Movie.objects.filter(title__contains=search).order_by('title')
    if request.GET.get('random'):
        movies = Movie.objects.order_by('?')[0:21]

    if request.GET.get('date'):
        movies = Movie.objects.order_by('-release_date')[(page_number-1) * 18: page_number * 18]

    serialize = MovieSerializer(movies, many=True)
    return Response(serialize.data)

@api_view(['GET'])
def moviegame_list(request):
    movies = Movie.objects.filter(popularity__gt=40).order_by('?')[0:16]
    # movies = Movie.objects.order_by('-popularity')[0:16]
    serialize = MovieSerializer(movies, many=True)
    return Response(serialize.data)

@api_view(['GET'])
def actorgame_list(request):
    actors = Actor.objects.filter(popularity__gt=30).order_by('?')[0:16]
    # movies = Movie.objects.order_by('-popularity')[0:16]
    serialize = ActorSerializer(actors, many=True)
    return Response(serialize.data)


@api_view(['GET'])
def seen_movie_list(request, username):
    if request.GET.get('page'):
        page_number = request.GET.get('page') # 현재 페이지 넘버
    else:
        page_number = 1

    user = get_object_or_404(get_user_model(), username=username)
    movies = Movie.objects.filter(seen_users=user)[(page_number-1) * 20: page_number * 20]
    serialize = MovieSerializer(movies, many=True)
    return Response(serialize.data) 

@api_view(['GET', 'POST'])
def movie_detail(request, movie_id):
    
    movie = get_object_or_404(Movie, movie_id = movie_id)
    def movie_list():
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)
    def review_create():
        if not Review.objects.filter(user_id = request.user.pk, movie_id = movie_id).exists():
            serializer = ReviewSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(movie=movie, user=request.user)
                serializer = MovieDetailSerializer(movie)
                # 리턴을 무비 리스트로 보내야하나?
                return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        return movie_list()
    elif request.method == 'POST':
        return review_create()

@api_view(['PUT', 'DELETE'])
def review_update_delete(request, movie_id, review_id):
    movie = get_object_or_404(Movie, movie_id = movie_id)
    review = get_object_or_404(Review, id = review_id)
    
    def update_review():
        if request.user == review.user:
            serializer = ReviewSerializer(instance=review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                serializer = MovieDetailSerializer(movie)
                return Response(serializer.data)
    
    def delete_review():
        if request.user == review.user:
            review.delete()
            serializer = MovieDetailSerializer(movie)
            return Response(serializer.data)

    if request.method == 'PUT':
        return update_review()
    elif request.method == 'DELETE':
        return delete_review()

@api_view(['POST'])
def review_like(request, movie_id, review_id):
    movie = get_object_or_404(Movie, movie_id = movie_id)
    review = get_object_or_404(Review, id = review_id)
    user = request.user
    if review.like_users.filter(id=user.id).exists():
        review.like_users.remove(user)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)
    else:
        review.like_users.add(user)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)

@api_view(['GET'])
def genre_detail(request, genre_id):
    genre = get_object_or_404(Genre, genre_id = genre_id)
    serializer = GenreSerializer(genre)
    return Response(serializer.data)

@api_view(['GET'])
def actor_detail(request, actor_id):
    actor = get_object_or_404(Actor, actor_id = actor_id)
    serializer = ActorSerializer(actor)
    return Response(serializer.data)

@api_view(['POST'])
def seen_movies(request, movie_id):
    movie = get_object_or_404(Movie, movie_id = movie_id)
    user = request.user
    if movie.seen_users.filter(id=user.id).exists():
        movie.seen_users.remove(user)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)
    else:
        movie.seen_users.add(user)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)

@api_view(['POST'])
def wish_movies(request, movie_id):
    movie = get_object_or_404(Movie, movie_id = movie_id)
    user = request.user
    if movie.wish_users.filter(id=user.id).exists():
        movie.wish_users.remove(user)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)
    else:
        movie.wish_users.add(user)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)

