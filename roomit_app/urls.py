from . import views as app_views
from django.contrib.auth import views as auth_views
from django.urls import path



urlpatterns = [
    path('', app_views.post_list, name='post_list_page'),
    path('requirementsR/<str:username>/', app_views.requirementsR, name='requirementsR'),
    path('requirementsP/<str:username>/', app_views.requirementsP, name='requirementsP'),
    path('more/', app_views.more, name='more'),
]

