from django.urls import path
from .views import HomePageView, SignupView, FormProfileView, signin, UserHomepageView


urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('signin/', signin, name='signin'),
    path('create_profile/', FormProfileView.as_view(), name='create_profile'),
    path('user_page/', UserHomepageView.as_view(), name='user_homepage'),
]
