from django.urls import path
from .views import HomePageView, RegistrationView


urlpatterns = [
    path('signup/', RegistrationView.as_view(), name='signup'),
    path('', HomePageView.as_view(), name='home'),
]
