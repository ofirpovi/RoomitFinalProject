from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.views import APIView
# from rest_framework import viewsets
from rest_framework.response import Response
# from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import auth
from django.views import View
from django.contrib import messages

from . import serializers
from . import models
from . import permissions


class HomePageView(TemplateView):
    template_name = "home.html"


class SignupView(APIView):
    """Create a new `User` object in the system."""

    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        try:
            serializer = serializers.UserSerializer(data=request.POST)
            serializer.is_valid(raise_exception=True)

        except (serializers.ValidationError, AttributeError) as e:
            return render(request, 'signup.html', {'error_message': "This is an Error"}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return redirect('create_profile', status=status.HTTP_201_CREATED)


def signin(request):
    if request.method == 'POST':
        username = request.POST['Email']
        password = request.POST['Password']
        user = auth.authenticate(Email=username, Password=password)
        if user is not None:
            auth.login(request, user)
            # TODO change to get the matches of the user
            user_matches = models.Roommates.objects.all
            context = {'my_matches': user_matches}
            return render(request, 'user_homepage.html', context)
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('signin')
    else:
        return render(request, 'signin.html')


def signout(request):
    auth.logout(request)
    return redirect('home')


class FormProfileView(APIView):
    def post(self, request):
        return render(request, 'profile_form.html')


class UserHomepageView(APIView):
    def get(self, request):
        return render(request, 'user_homepage.html')
