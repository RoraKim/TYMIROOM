from . import views
from django.urls import path

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list),
    path('<username>/seen/list/', views.seen_movie_list),
    path('<int:movie_id>/', views.movie_detail),
    path('<int:movie_id>/<int:review_id>/', views.review_update_delete),
    path('<int:movie_id>/<int:review_id>/like/', views.review_like),
    path('genres/<int:genre_id>/', views.genre_detail),
    path('actors/<int:actor_id>/', views.actor_detail),
    path('<int:movie_id>/seen/', views.seen_movies),
    path('<int:movie_id>/wish/', views.wish_movies),
    # 영화 월드컵 path
    path('moviegame/', views.moviegame_list),
    path('actorgame/', views.actorgame_list),
]
