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
                print("\n\nrequirementR saved\n\n")
                update_scores(request)
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
            print("\n\nrequirementR saved\n\n")
            update_scores(request)
            return redirect('profile', request.user)
    else:
        form = UpdateRequirementsRForm(instance=requirements)

    return render(request, 'requirementsR.html', {'form': form})


@login_required
def more(request):
    # This is the list that will be paginated.
    users = User.objects.all()
    list_items = Scores.objects.all()
    print("\n\nin more\n\n")
    profile = Profile.objects.get(user=request.user)
    # list_items = list_items.filter(Username_insert=request.user) | list_items.filter(Username_enter=request.user)
    # # list_items = list_items.order_by('-Insert_score')
    if profile.profile_status == 'StatusInsert':
        list_items = list_items.filter(Username_insert=request.user)
        list_items = list_items.order_by('-Insert_score')
    else:
        list_items = list_items.filter(Username_enter=request.user)
        list_items = list_items.order_by('-Enter_score')
    return more_items(request, list_items, template='more.html')
    # return more_items(request, users,
    #                       # (optional) your custom template
    #                       template='more.html')


@login_required
def post_list(request):
    list_items = User.objects.all()
    list_items = Scores.objects.all()
    username = request.user.username
    print("\n\nin post_list\n\n")
    profile = Profile.objects.get(user=request.user)
    if profile.profile_status == 'StatusInsert':
        list_items = list_items.filter(Username_insert=request.user)
        list_items = list_items.order_by('-Insert_score')
    else:
        list_items = list_items.filter(Username_enter=request.user)
        list_items = list_items.order_by('-Enter_score')
    paginated = get_pagination(request, list_items)
    data = {
        'more_posts_url': reverse('more'),
        }
    data.update(paginated)
    print("\n\nout of post_list\n\n")
    return render(request, 'post_list.html', data)


def update_scores(request):
    online_user = request.user
    Scores.objects.filter(Username_enter=online_user).delete()
    Scores.objects.filter(Username_insert=online_user).delete()
    # Scores.objects.filter(Username_enter=username).delete()
    # Scores.objects.filter(Username_insert=username).delete()
    profile = Profile.objects.get(user=online_user)
    online_status = profile.profile_status
    status_match = 'StatusEnter' if online_status == 'StatusInsert' else 'StatusInsert'
    potential_profiles = Profile.objects.filter(profile_status=status_match)
    requirementsR = make_requirementsR(request.user)
    if online_status == 'StatusEnter':
        requirementsP = make_requirementsP(request.user)
        for user in potential_profiles:
            score_enter = update_scores_enter(requirementsR, requirementsP, user)
            requirement = make_requirementsR(user.user)
            score_insert = update_scores_insert(requirement, online_user.profile)
            score = Scores(Username_enter=online_user, Username_insert=user.user, Enter_score=score_enter, Insert_score=score_insert)
            print("\n\nscore updated\n\n")
            score.save()
    else:
        for user in potential_profiles:
            requirement = make_requirementsR(user.user)
            requirementsP = make_requirementsP(user.user)
            score_enter = update_scores_enter(requirement, requirementsP, online_user.profile)
            score_insert = update_scores_insert(requirementsR, user)
            score = Scores(Username_enter=user.user, Username_insert=online_user, Enter_score=score_enter, Insert_score=score_insert)
            print("\n\nscore updated\n\n")
            score.save()


def update_scores_enter(requirementsR, requirementsP, user):
    if requirementsR is None or requirementsP is None:
        return -1
    else:
        personal_score = calculate_score(requirementsR, user)
        personal_scoreP = calculate_score(requirementsP, user)
        personal_score = (personal_score + personal_scoreP)/2
        return personal_score


def update_scores_insert(requirementsR, user):
    if requirementsR is None:
        return -1
    else:
        personal_score = calculate_score(requirementsR, user)
        return personal_score


def make_requirementsP(user):
    try:
        reqP = []
        requirementP = RequirementsP.objects.get(user=user)
        reqP.append(ListReq.ListReq(True, requirementP.Weight, "Country", requirementP.Country))
        reqP.append(ListReq.ListReq(True, requirementP.Weight, "City", requirementP.City))
        reqP.append(ListReq.ListReq(True, requirementP.Weight, "Neighborhood", requirementP.Neighborhood))
        reqP.append(RangReq.RangReq(False, requirementP.Weight, "rent", requirementP.MinRent, requirementP.MaxRent))
        reqP.append(RangReq.RangReq(False, requirementP.Weight, "rooms_number", requirementP.MinRooms, requirementP.MaxRooms))
        reqP.append(RangReq.RangReq(False, requirementP.Weight, "roommates_number", requirementP.MinRoommates, requirementP.MaxRoommates))
        reqP.append(RangReq.RangReq(False, requirementP.Weight, "toilets_number", requirementP.MinToilets, None))
        reqP.append(RangReq.RangReq(False, requirementP.Weight, "showers_number", requirementP.MinShowers, None))
        return reqP
    except:
        return None


def make_requirementsR(user):
    try:
        reqR = []
        requirementR = RequirementsR.objects.get(user=user)
        reqR.append(ListReq.ListReq(False, requirementR.Weight, "gender", requirementR.Gender))
        reqR.append(ListReq.ListReq(False, requirementR.Weight, "occupation", requirementR.Occupation))
        reqR.append(ListReq.ListReq(False, requirementR.Weight, "smoker", requirementR.Smoker))
        reqR.append(ListReq.ListReq(False, requirementR.Weight, "diet", requirementR.Diet))
        reqR.append(ListReq.ListReq(False, requirementR.Weight, "status", requirementR.Status))
        # reqR.append(ListReq.ListReq(False, requirementR.Weight, "hospitality", requirementR.hospitality))
        reqR.append(ListReq.ListReq(False, requirementR.Weight, "kosher", requirementR.Kosher))
        # reqR.append(ListReq.ListReq(False, requirementR.Weight, "expense_management", requirementR.expense_management))
        # reqR.append(ListReq.ListReq(False, requirementR.Weight, "age", requirementR.age))
        return reqR
    except:
        return None

def calculate_score(reqs, user):
    weight, score = 0, 0
    answers_info = {}
    for req in reqs:
        req_text = req._text
        req_weight = req._weight
        weight += req_weight
        req_score = req.calculate_score(getattr(user, req_text))
        score += req_score
        answers_info[req_text] = [req_text, req_score,
                                req_weight, req.convert_answer_to_str(getattr(user, req_text))]
    # return weight, score, answers_info
    return score

class UserHomepageView(APIView):
    def get(self, request):
        return render(request, 'user_homepage.html')
