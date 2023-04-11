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

from django.contrib.auth.models import User
from rest_framework.decorators import api_view

from . import serializers
from . import models
from . import permissions
from .forms import InfoForm


class HomePageView(TemplateView):
    template_name = "home.html"


@api_view(['POST', 'GET'])
def signup(request):
    if request.method == 'POST':
        try:
            serializer = serializers.UserSerializer(data=request.POST)
            serializer.is_valid(raise_exception=True)

        except (serializers.ValidationError) as e:
            return Response(data={'request': request, 'error_message': e}, status=status.HTTP_400_BAD_REQUEST)

        user = serializer.save()
        data = {'user': 'user'}
        return Response(data, status=status.HTTP_201_CREATED)

    elif request.method == 'GET':
        return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        print(request.POST)
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
    def get(self, request):
        return render(request, 'info_form')

    def post(self, request):
        form = InfoForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            birthdate = form.cleaned_data['birthdate']
            gender = form.cleaned_data['gender']
            occupation = form.cleaned_data['occupation']
            smoking = form.cleaned_data['smoking']
            diet = form.cleaned_data['diet']
            kosher = form.cleaned_data['kosher']
            single = form.cleaned_data['single']
            hospitality = form.cleaned_data['hospitality']
            shopping = form.cleaned_data['shopping']

            # Create the personal info object and associate it with the user object
            try:
                serializer = serializers.InfoSerializer(data={'first_name': first_name,
                                                              'last_name': last_name,
                                                              'phone_number': phone_number,
                                                              'birthdate': birthdate,
                                                              'gender': gender,
                                                              'occupation': occupation,
                                                              'smoking': smoking,
                                                              'diet': diet,
                                                              'kosher': kosher,
                                                              'single': single,
                                                              'hospitality': hospitality,
                                                              'shopping': shopping, })
                serializer.is_valid(raise_exception=True)
            except (serializers.ValidationError, AttributeError) as e:
                return render(self.request, 'info_form', {'error_message': "This is an Error"}, status=status.HTTP_400_BAD_REQUEST)
            info = models.Info(first_name=first_name, last_name=last_name, phone_number=phone_number, bitrhdate=bitrhdate, gender=gender,
                               occupation=occupation, smoking=smoking, diet=diet, kosher=kosher, single=single, hospitality=hospitality, shopping=shopping)
            info.save()

            # Store the user ID in the form data so we can check if the user has already been created
            # self.storage.extra_data['user_id'] = user.id

            # Return a response to the user
            return render(self.request, 'user_homepage')
        return render(request, 'info_form.html', {'form': form})


class UserHomepageView(APIView):
    def get(self, request):
        return render(request, 'user_homepage.html')
