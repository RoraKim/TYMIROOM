from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('users/<username>/', views.user_list),
    path('<username>/follow/', views.follow),
    path('<username>/followers/', views.followers),
    path('profile/<username>/', views.profile),
    path('update/profile/', views.profile_update),
    path('profile/<username>/guestbook/', views.guestbook_create),
    path('profile/<username>/guestbook/<int:guestbook_id>/', views.guestbook_update_delete),
]
