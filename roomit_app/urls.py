from django.urls import path
from . import views as app_views

urlpatterns = [
    path('', app_views.post_list, name='post_list_page'),
    path('requirementsR/<str:username>/', app_views.requirementsR, name='requirementsR'),
    path('requirementsP/<str:username>/', app_views.requirementsP, name='requirementsP'),
    path('more/', app_views.more, name='more'),
    # path('search-results', app_views.search, name='search-results'),dd
    path('like-picture/<str:username>/', app_views.like_picture, name='like_picture'),
    path('likes-me/', app_views.likes_me, name='likes_me'),
    path('i-like/', app_views.i_like, name='i_like'),
]

