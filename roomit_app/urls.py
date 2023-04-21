from django.urls import path
from . import views as app_views
from django.contrib.auth import views as auth_views
from django.urls import path, re_path
from . import views
# .views import HomePageView, SignupView, FormProfileView, signin, UserHomepageView


urlpatterns = [
    # path('home/', app_views.home, name='home'),
    path('signup/', app_views.signup, name='signup'),
    path('signin/', auth_views.LoginView.as_view(template_name='signin.html'), name='signin'),
    path('signout/', auth_views.LogoutView.as_view(template_name='signup.html'), name='signout'),
    path('info_form/', app_views.profile_info, name='info_form'),
    path('user_homepage/', app_views.UserHomepageView.as_view(), name='user_homepage'),
    path('', app_views.post_list, name='post_list_page'),
    path('requirementsR/<str:username>/', app_views.requirementsR, name='requirementsR'),
    path('requirementsP/<str:username>/', app_views.requirementsP, name='requirementsP'),
    # path('post_list/', app_views.post_list, name='post_list_page'),
    path('more/', app_views.more, name='more'),
]

