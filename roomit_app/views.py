from typing import Any, Dict
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.http import JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from infscroll.utils import get_pagination
from infscroll.views import more_items
from rest_framework.views import APIView

from users.models import Profile, PropertyForOffer, Image
from .forms import UpdateRequirementsRForm, UpdateRequirementsPForm
from .models import RequirementsP, RequirementsR, Scores, Likes
from .requirements import ListReq, RangReq
from django.views.generic.list import ListView
from .filters import PropertyOfferFilter, RoommateFilter
from.models import RequirementsR

def home(request):
    return render(request, 'roomit_app/post_list.html')


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
                print("\n\nrequirementsP saved\n\n")
                update_scores(request)
                return redirect('requirementsR', request.user)
        else:
            form = UpdateRequirementsPForm(instance=requirements)
        return render(request, 'status/requirementsP.html', {'form': form, 'user_profile': username})


@login_required
def requirementsR(request, username):
    print(username)
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

    return render(request, 'status/requirementsR.html', {'form': form, 'user_profile': username})


@login_required
def likes_me(request):
    list_items = Likes.objects.all()
    profile = Profile.objects.get(user=request.user)
    online_status = profile.profile_status
    if online_status == "StatusEnter":
        list_items = list_items.filter(User_enter=request.user)
    else:
        list_items = list_items.filter(User_insert=request.user)

    return render(request, 'likes_me.html')


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


@login_required
def post_list(request):
    list_items = Scores.objects.all()
    username = request.user.username
    profile = Profile.objects.get(user=request.user)
    if profile.profile_status == 'StatusInsert':
        list_items = list_items.filter(Username_insert=request.user)
        list_items = list_items.order_by('-Insert_score')
    else:
        lst = list_items.filter(Username_enter=request.user)
        lst = lst.order_by('-Enter_score')
        list_items = []
        for item in lst:
            user_insert = item.Username_insert
            prop = PropertyForOffer.objects.get(user=user_insert)
            images = Image.objects.all()
            images = images.filter(property=prop).first()
            list_items.append(Posts(item, images))
    paginated = get_pagination(request, list_items)
    data = {
        'more_posts_url': reverse('more'),
    }
    data.update(paginated)
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
    reqR = make_requirementsR(online_user)
    if online_status == 'StatusEnter':
        reqP = make_requirementsP(request.user)
        for user in potential_profiles:
            score_enter = update_scores_enter(reqR, reqP, user)
            requirement = make_requirementsR(user.user)
            score_insert = update_scores_insert(requirement, online_user.profile)
            score = Scores(Username_enter=online_user, Username_insert=user.user, Enter_score=score_enter, Insert_score=score_insert)
            # print("\n\nscore updated\n\n")
            score.save()
    else:
        for user in potential_profiles:
            requirement = make_requirementsR(user.user)
            reqP = make_requirementsP(user.user)
            score_enter = update_scores_enter(requirement, reqP, online_user.profile)
            score_insert = update_scores_insert(reqR, user)
            score = Scores(Username_enter=user.user, Username_insert=online_user, Enter_score=score_enter, Insert_score=score_insert)
            # print("\n\nscore updated\n\n")
            score.save()


def update_scores_enter(requirementsR, requirementsP, user):
    if requirementsR is None and requirementsP is None:
        # print("both none\n \n")
        return 100
    elif requirementsR is None:
        personal_scoreP = calculate_score(requirementsP, user)
        # print("requirementsR none\n\n")
        return (personal_scoreP + 100) / 2
    elif requirementsP is None:
        personal_score = calculate_score(requirementsR, user)
        # print("requirementsP none\n\n")
        return (personal_score + 100) / 2
    else:
        personal_scoreR = calculate_score(requirementsR, user)
        personal_scoreP = calculate_score(requirementsP, user)
        personal_score = (personal_scoreR + personal_scoreP)/2
        return personal_score


def update_scores_insert(requirementsR, user):
    if requirementsR is None:
        return 100
    else:
        personal_score = calculate_score(requirementsR, user)
        return personal_score


@login_required
def like_picture(request, username):
    print("in like picture")
    # other_user = request.POST.get('userw')
    other_user = User.objects.get(username=username)
    print("other user   ---    ", other_user)
    profile = Profile.objects.get(user=request.user)
    online_status = profile.profile_status

    if online_status == "StatusEnter":
        like = Likes.objects.get_or_create(User_enter=request.user, User_insert=other_user)[0]
        like.enter_likes_insert = True
        like.save()
    else:
        like = Likes.objects.get_or_create(User_enter=request.user, User_insert=other_user)[0]
        like.insert_likes_enter = True
        like.save()
    return redirect('post_list_page')


def make_requirementsP(user):
    reqP = []
    # print("---------------------------------     make_requirementsP  -->  ", user.username, "     -----------------------------------------------------------")
    requirementP = RequirementsP.objects.get_or_create(user=user)[0]
    # print("-------------------------------------------------------------------------------------------")
    reqP.append(ListReq.ListReq(True, requirementP.Weight, "Country", requirementP.Country))
    reqP.append(ListReq.ListReq(True, requirementP.Weight, "City", requirementP.City))
    reqP.append(ListReq.ListReq(True, requirementP.Weight, "Neighborhood", requirementP.Neighborhood))
    reqP.append(RangReq.RangeReq(False, requirementP.Weight, "rent", requirementP.MinRent, requirementP.MaxRent))
    reqP.append(RangReq.RangeReq(False, requirementP.Weight, "rooms_number", requirementP.MinRooms, requirementP.MaxRooms))
    reqP.append(RangReq.RangeReq(False, requirementP.Weight, "roomates_number", requirementP.MinRoommates, requirementP.MaxRoommates))
    reqP.append(RangReq.RangeReq(False, requirementP.Weight, "toilets_number", requirementP.MinToilets, None))
    reqP.append(RangReq.RangeReq(False, requirementP.Weight, "showers_number", requirementP.MinShowers, None))
    # reqP.append(RangReq.RangeReq(False, requirementP.Weight, "shelter_inside", requirementP.MinShowers, None))
    # reqP.append(RangReq.RangeReq(False, requirementP.Weight, "shelter_nerbay", requirementP.MinShowers, None))
    # reqP.append(RangReq.RangeReq(False, requirementP.Weight, "furnished", requirementP.MinShowers, None))
    # reqP.append(RangReq.RangeReq(False, requirementP.Weight, "renovated", requirementP.MinShowers, None))
    # reqP.append(RangReq.RangeReq(False, requirementP.Weight, "shared_livingroom", requirementP.MinShowers, None))
    return reqP
    # except:
    #     return None


def make_requirementsR(user):
    try:
        reqR = []
        # print("--------------------------------     ", user.username, "     -----------------------------------------------------------")

        requirementR = RequirementsR.objects.get_or_create(user=user)[0]
        reqR.append(ListReq.ListReq(False, requirementR.Weight, "gender", requirementR.Gender))
        reqR.append(ListReq.ListReq(False, requirementR.Weight, "occupation", requirementR.Occupation))
        reqR.append(ListReq.ListReq(False, requirementR.Weight, "smoker", requirementR.Smoker))
        reqR.append(ListReq.ListReq(False, requirementR.Weight, "diet", requirementR.Diet))
        reqR.append(ListReq.ListReq(False, requirementR.Weight, "status", requirementR.Status))
        # reqR.append(ListReq.ListReq(False, requirementR.Weight, "hospitality", requirementR.hospitality))
        reqR.append(ListReq.ListReq(False, requirementR.Weight, "kosher", requirementR.Kosher))
        reqR.append(ListReq.ListReq(False, requirementR.Weight, "expense_management", requirementR.Expense_Management))
        # reqR.append(RangReq.RangeReq(False, requirementR.Weight, "age", requirementR.age))
        return reqR
    except Exception as e:
        print(e)
        # print(reqR)
        return reqR


def calculate_score(reqs, user):
    score = 0
    answers_info = {}
    try:
        property = PropertyForOffer.objects.get(user=user)
    except:
        property = None
    for req in reqs:
        req_text = req._text
        try:
            req_score = req.calculate_score(getattr(user, req_text))
        except AttributeError:
            try:
                req_score = req.calculate_score(getattr(property, req_text))
            except AttributeError:
                req_score = 0

        score += req_score

    # return weight, score, answers_info
    return score


class UserHomepageView(APIView):
    def get(self, request):
        return render(request, 'post_list.html')

class PropertyFilterListView(ListView):
    queryset = PropertyForOffer.objects.all()
    template_name = 'filter_results.html'
    context_object_name = 'data'

    def dispatch(self, request, *args, **kwargs):
        self.user = request.user  # set the user attribute
        return super().dispatch(request, *args, **kwargs)
    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PropertyOfferFilter(self.request.GET, queryset=queryset)
        data_to_return =[]
        for prop in self.filterset.qs:
            scores = Scores.objects.filter(Username_insert=prop.user, Username_enter=self.request.user)
            if scores:
                score = scores[0]
                image = Image.objects.filter(property=prop).first()
                if image:
                    print(f'prop_image: {image.image}, {image}')
                else:
                    print('no image')
                context = {
                    'score': score.Enter_score, 
                    'username': score.Username_insert,
                    'image': image}
                data_to_return.append(context)
               
        return data_to_return
    
    def get_context_data(self, **kwargs):
        print('in get_context_data')
        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset.form
        return context


class RoommateFilterListView(ListView):
    queryset = Profile.objects.all()
    template_name = 'filter_results.html'
    context_object_name = 'data'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = RoommateFilter(self.request.GET, queryset=queryset)
        data_to_return =[]
        for profile in self.filterset.qs:
            image = profile.image
            context = {}
            if(self.request.user.profile.profile_status == 'StatusEnter'):
                score = Scores.objects.filter(Username_insert=profile.user, Username_enter=self.request.user)
                if score:
                    score = score[0]
                    context = {
                            'score': score.Enter_score, 
                            'username': score.Username_insert.username,
                            'image': image}
                    data_to_return.append(context)
            else:
                score = Scores.objects.filter(Username_enter=profile.user, Username_insert=self.request.user)
                if score:
                    score = score[0]
                    context = {
                            'score': score.Insert_score, 
                            'username': score.Username_enter.username,
                            'image': image}
                    data_to_return.append(context)
        return data_to_return
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset.form
        return context
    
class Posts:
    def __init__(self, item, image):
        self.image = image
        self.item = item


    