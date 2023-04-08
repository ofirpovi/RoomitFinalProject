from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.views import APIView
# from rest_framework import viewsets
from rest_framework.response import Response
# from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
# from django.contrib.auth.forms import UserCreationForm
from django.views import View

from . import serializers
from . import models
from . import permissions


class HomePageView(TemplateView):
    template_name = "home.html"


class RegistrationView(APIView):
    """Create a new `User` object in the system."""

    def get(self, request):
        return render(request, "signup.html")

    def post(self, request):
        print("post: {}".format(request.POST))
        serializer = serializers.UserSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginUser():
    pass


class LogoutUser():
    pass
