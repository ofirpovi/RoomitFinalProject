from django.urls import path
from . import views
# .views import HomePageView, SignupView, FormProfileView, signin, UserHomepageView


urlpatterns = [
    path('home/', views.HomePageView.as_view(), name='home'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('create_profile/', views.FormProfileView.as_view(), name='create_profile'),
    path('user_homepage/', views.UserHomepageView.as_view(), name='user_homepage'),
]
