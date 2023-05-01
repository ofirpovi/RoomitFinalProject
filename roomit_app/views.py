from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from infscroll.utils import get_pagination
from infscroll.views import more_items
from rest_framework.views import APIView

from users.models import Profile, PropertyForOffer
from .forms import UpdateRequirementsRForm, UpdateRequirementsPForm
from .models import RequirementsP, RequirementsR, Scores
from .requirements import ListReq, RangReq


def home(request):
    return render(request, 'roomit_app/post_list.html')

@login_required
def requirementsP(request, username):
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)
    if profile.profile_status == 'insert in':
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
        return render(request, 'status/requirementsP.html', {'form': form})


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

    return render(request, 'status/requirementsR.html', {'form': form})


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
    #list_items = User.objects.all()
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
    reqR = make_requirementsR(request.user)
    if online_status == 'StatusEnter':
        reqP = make_requirementsP(request.user)
        for user in potential_profiles:
            score_enter = update_scores_enter(reqR, reqP, user)
            requirement = make_requirementsR(user.user)
            score_insert = update_scores_insert(requirement, online_user.profile)
            score = Scores(Username_enter=online_user, Username_insert=user.user, Enter_score=score_enter, Insert_score=score_insert)
            print("\n\nscore updated\n\n")
            score.save()
    else:
        for user in potential_profiles:
            requirement = make_requirementsR(user.user)
            reqP = make_requirementsP(user.user)
            score_enter = update_scores_enter(requirement, reqP, online_user.profile)
            score_insert = update_scores_insert(reqR, user)
            score = Scores(Username_enter=user.user, Username_insert=online_user, Enter_score=score_enter, Insert_score=score_insert)
            print("\n\nscore updated\n\n")
            score.save()


def update_scores_enter(requirementsR, requirementsP, user):
    if requirementsR is None and requirementsP is None:
        print("\n\nboth none\n\n")
        return 100
    elif requirementsR is None:
        personal_scoreP = calculate_score(requirementsP, user)
        print("\n\nrequirementsR none\n\n")
        return personal_scoreP
    elif requirementsP is None:
        personal_score = calculate_score(requirementsR, user)
        print("\n\nrequirementsP none\n\n")
        return personal_score
    else:
        personal_score = calculate_score(requirementsR, user)
        personal_scoreP = calculate_score(requirementsP, user)
        personal_score = (personal_score + personal_scoreP)/2
        return personal_score


def update_scores_insert(requirementsR, user):
    if requirementsR is None:
        print("\n\nstatus insert score - requirementsR none\n\n")
        return 100
    else:
        personal_score = calculate_score(requirementsR, user)
        return personal_score


def make_requirementsP(user):
    # try:
    reqP = []
    print("--------------------------------     ", user.username, "     -----------------------------------------------------------")
    requirementP = RequirementsP.objects.get(user=user)
    print("-------------------------------------------------------------------------------------------")
    reqP.append(ListReq.ListReq(True, requirementP.Weight, "Country", requirementP.Country))
    reqP.append(ListReq.ListReq(True, requirementP.Weight, "City", requirementP.City))
    reqP.append(ListReq.ListReq(True, requirementP.Weight, "Neighborhood", requirementP.Neighborhood))
    # rq =
    reqP.append(RangReq.RangeReq(False, requirementP.Weight, "rent", requirementP.MinRent, requirementP.MaxRent))
    reqP.append(RangReq.RangeReq(False, requirementP.Weight, "rooms_number", requirementP.MinRooms, requirementP.MaxRooms))
    reqP.append(RangReq.RangeReq(False, requirementP.Weight, "roommates_number", requirementP.MinRoommates, requirementP.MaxRoommates))
    reqP.append(RangReq.RangeReq(False, requirementP.Weight, "toilets_number", requirementP.MinToilets, None))
    reqP.append(RangReq.RangeReq(False, requirementP.Weight, "showers_number", requirementP.MinShowers, None))
    reqP.append(RangReq.RangeReq(False, requirementP.Weight, "showers_number", requirementP.MinShowers, None))
    reqP.append(RangReq.RangeReq(False, requirementP.Weight, "showers_number", requirementP.MinShowers, None))
    reqP.append(RangReq.RangeReq(False, requirementP.Weight, "showers_number", requirementP.MinShowers, None))
    return reqP
    # except:
    #     return None


def make_requirementsR(user):
    try:
        reqR = []
        print("--------------------------------     ", user.username, "     -----------------------------------------------------------")

        requirementR = RequirementsR.objects.get(user=user.username)
        reqR.append(ListReq.ListReq(False, requirementR.Weight, "gender", requirementR.Gender))
        reqR.append(ListReq.ListReq(False, requirementR.Weight, "occupation", requirementR.Occupation))
        reqR.append(ListReq.ListReq(False, requirementR.Weight, "smoker", requirementR.Smoker))
        reqR.append(ListReq.ListReq(False, requirementR.Weight, "diet", requirementR.Diet))
        reqR.append(ListReq.ListReq(False, requirementR.Weight, "status", requirementR.Status))
        # reqR.append(ListReq.ListReq(False, requirementR.Weight, "hospitality", requirementR.hospitality))
        reqR.append(ListReq.ListReq(False, requirementR.Weight, "kosher", requirementR.Kosher))
        reqR.append(ListReq.ListReq(False, requirementR.Weight, "expense_management", requirementR.expense_management))
        reqR.append(ListReq.ListReq(False, requirementR.Weight, "renovated", requirementR.expense_management))
        reqR.append(ListReq.ListReq(False, requirementR.Weight, "shelter_inside", requirementR.expense_management))
        reqR.append(ListReq.ListReq(False, requirementR.Weight, "shelter_nerbay", requirementR.expense_management))
        reqR.append(ListReq.ListReq(False, requirementR.Weight, "furnished", requirementR.expense_management))
        reqR.append(ListReq.ListReq(False, requirementR.Weight, "shared_livingroom", requirementR.expense_management))
        # reqR.append(ListReq.ListReq(False, requirementR.Weight, "age", requirementR.age))

        return reqR
    except :
        return None

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

def search(request):
    return render(request, 'post_list.html')
