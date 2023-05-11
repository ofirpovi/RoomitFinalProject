from django.urls import path
from . import views as app_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', app_views.post_list, name='post_list_page'),
    path('requirementsR/<str:username>/',
         app_views.requirementsR, name='requirementsR'),
    path('requirementsP/<str:username>/',
         app_views.requirementsP, name='requirementsP'),
    path('more/', app_views.more, name='more'),
    path('filter-results/property', app_views.PropertyFilterListView.as_view(),
         name='filter-results-property'),
    path('filter-results/roommate', app_views.RoommateFilterListView.as_view(),
         name='filter-results-roommate'),
    path('like-picture/', app_views.like_picture, name='like_picture'),
    path('like-picture/<str:username>/', app_views.like_picture, name='like_picture'),
    path('unlike-picture/<str:username>/', app_views.unlike_picture, name='unlike_picture'),
    path('likes-me/', app_views.likes_me, name='likes_me'),
    path('i-like/', app_views.i_like, name='i_like'),
]

