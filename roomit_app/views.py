from django.shortcuts import render, redirect
from django.template.loader import render_to_string
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
from .forms import UpdateRequirementsRForm, UpdateRequirementsPForm
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from infscroll.utils import get_pagination
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from infscroll.views import more_items
from . import serializers
from . import models
from . import permissions
from .models import RequirementsP, RequirementsR, Scores
from users.models import Profile
from .requirements import Requirement, RangReq, ListReq, YNReq

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


@login_required
def requirementsP(request, username):
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)
    if profile.profile_status == 'StatusInsert':
        return redirect(requirementsR, request.user)
    else:
        try:
            requirements = RequirementsP.objects.get(user=user)
        except RequirementsP.DoesNotExist:
            requirements = RequirementsP(user=request.user)
            requirements.save()

        if request.method == 'POST':
            form = UpdateRequirementsPForm(request.POST, instance=requirements)
            if form.is_valid():
                form.save()
                return redirect('requirementsR', request.user)
        else:
            form = UpdateRequirementsPForm(instance=requirements)
        return render(request, 'requirementsP.html', {'form': form})


@login_required
def requirementsR(request, username):
    user = User.objects.get(username=request.user.username)
    try:
        requirements = RequirementsR.objects.get(user=user)
    except RequirementsR.DoesNotExist:
        requirements = RequirementsR(user=request.user)
        requirements.save()

    if request.method == 'POST':
        form = UpdateRequirementsRForm(request.POST, instance=requirements)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your Requirements have been updated!')
            return redirect('profile', request.user)
    else:
        form = UpdateRequirementsRForm(instance=requirements)

    return render(request, 'requirementsR.html', {'form': form})

@login_required
def more(request, page):
    # This is the list that will be paginated.
    list_items = User.objects.all()
    return more_items(request, list_items,template='more.html')

@login_required
def post_list(request, page):
    scores = User.objects.all()
    paginated = get_pagination(request, scores)
    page += 1
    data = {
            'more_posts_url': reverse('more', kwargs={"page": page}),
            }
    data.update(paginated)
    return render(request, 'post_list.html', data)

def updateScores(request):
    username = request.user.username
    Scores.objects.filter(username1=username).delete()
    Scores.objects.filter(username2=username).delete()
    profile = Profile.objects.get(username=username)
    status_match = 'StatusEnter' if profile.profile_status == 'StatusInsert' else 'StatusInsert'
    potential_profiles = Profile.objects.filter(profile_status=status_match)
    requirements = []
    if profile.profile_status == 'StatusEnter':
        requirementP = RequirementsP.objects.get(user=request.user)
        requirements.append(ListReq(True, requirementP.Weight, "Country", requirementP.Country))
        requirements.append(ListReq(True, requirementP.Weight, "City", requirementP.City))
        requirements.append(ListReq(True, requirementP.Weight, "Neighborhood", requirementP.Neighborhood))
        requirements.append(RangReq(False, requirementP.Weight, "Rent", requirementP.MinRent, requirementP.MaxRent))
        requirements.append(RangReq(False, requirementP.Weight, "Number of rooms", requirementP.MinRooms, requirementP.MaxRooms))
        requirements.append(RangReq(False, requirementP.Weight, "Number of roommates", requirementP.MinRoommates, requirementP.MaxRoommates))
        requirements.append(RangReq(False, requirementP.Weight, "Number of toilets", requirementP.MinToilets, None))
        requirements.append(RangReq(False, requirementP.Weight, "Number of showers", requirementP.MinShowers, None))
    requirementR = RequirementsR.objects.get(user=request.user)
    requirements.append()




class UserHomepageView(APIView):
    def get(self, request):
        return render(request, 'user_homepage.html')
