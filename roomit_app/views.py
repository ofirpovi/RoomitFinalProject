from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.views import APIView
# from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import auth
from django.views import View
from django.contrib import messages
# from formtools.wizard.views import SessionWizardView
from django.urls import reverse
from .forms import CreateRequirementsPForm, UpdateRequirementsPForm
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from . import serializers
from . import models
from . import permissions
from .models import RequirementsP


#from .forms import InfoForm


def home(request):
    return render(request, 'roomit_app/home.html')


@api_view(['POST', 'GET'])
def signup(request):
    if request.method == 'POST':
        try:
            serializer = serializers.UserSerializer(data=request.POST)
            serializer.is_valid(raise_exception=True)

        except (serializers.ValidationError) as e:
            return Response(data={'request': request, 'error_message': e}, status=status.HTTP_400_BAD_REQUEST)

        user = serializer.save()
        data = {'user': user}
        return Response(data, status=status.HTTP_201_CREATED)

    elif request.method == 'GET':
        return render(request, 'signup.html')

@api_view(['GET', 'POST'])
def signin(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("Enter if")
            login(request, user)
            context = {'user': user}
            return Response(context= context, status= status.HTTP_200_OK)
        else:
            return Response(status= status.HTTP_406_NOT_ACCEPTABLE)
           
    elif request.method == 'GET':
        return render(request, 'signin.html')


def signout(request):
    logout(request)
    return Response(status= status.HTTP_200_OK)



@api_view(['GET', 'POST'])
#@login_required
def profile_info(request):
    try:
        profile = models.Info.objects.get(User_ID=request.user)
    except models.Info.DoesNotExist:
        profile = None

    if request.method == 'GET':
        serializer = serializers.InfoSerializer(profile)
        #return Response(serializer.data)
        return render(request, 'info_form.html') 

    elif request.method == 'POST':
        serializer =serializers.InfoSerializer(data=request.POST)
        print('Before')
        if serializer.is_valid():
            print('After')
            #print(serializer)
            serializer.save(user=request.user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def profile(request):
    return render(request, 'profile.html')


def requirements(request, username):
    user = User.objects.get(username=username)
    requirements = RequirementsP.objects.get(user=user)

    if request.method == 'POST':
        form = UpdateRequirementsPForm(request.POST, instance=requirements)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your Requirements have been updated!')
            return redirect('profile', request.user)

    else:
        form = UpdateRequirementsPForm(instance=requirements)

    context = {
        'form': form,
    }
    return render(request, 'requirements.html', context)


class UserHomepageView(APIView):
    def get(self, request):
        return render(request, 'user_homepage.html')
