from django.urls import path
from . import views
# .views import HomePageView, SignupView, FormProfileView, signin, UserHomepageView


urlpatterns = [
    path('home/', views.HomePageView.as_view(), name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('info_form/', views.profile_info, name='info_form'),
    path('user_homepage/', views.UserHomepageView.as_view(), name='user_homepage'),
]
