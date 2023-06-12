from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from infscroll.utils import get_pagination
from infscroll.views import more_items
from rest_framework.views import APIView
from users.forms import ProfileUpdateForm, UserUpdateForm
from users.models import Profile, PropertyForOffer, Image
from .forms import UpdateRequirementsRForm, UpdateRequirementsPForm
from .matches.calculate_score import update_scores
from .models import RequirementsP, RequirementsR, Scores, Likes
from .matches.requirements import YNReq, RangReq, ListReq
from .filters import PropertyOfferFilter, RoommateFilter
from .recommendation_system import recommendations as rec_sys
from roomit_app.matches.requirements.LocationReq import LocationReq


def home(request):
    return render(request, 'roomit_app/post_list.html')


@login_required
def requirementsP(request, username):
    try:
        user = get_object_or_404(User, username=request.user.username)
        try:
            requirements = RequirementsP.objects.get(user=user)
        except RequirementsP.DoesNotExist:
            requirements = RequirementsP(user=user)
            requirements.save()

        if request.method == 'POST':
            form = UpdateRequirementsPForm(request.POST, instance=requirements)
            if form.is_valid():
                selectedArea = request.POST.get('selectedArea')
                if selectedArea:
                    print("in if selected area")
                    requirements.Location = selectedArea  # Update the Location field
                form.save()
                messages.success(request, f'Your Requirements have been saved!')
                update_scores(request)
                return redirect('requirementsR', user)
        else:
            try:
                pl = requirements.Location
            except:
                pl = None
            form = UpdateRequirementsPForm(instance=requirements)
        return render(request, 'status/requirementsP.html', {'form': form, 'user_profile': username, 'property_location': pl,})
    except Exception as e:
        print(" error   --   ", e)
        return e


@login_required
def requirementsR(request, username):
    print("in reqR")
    try:
        user = get_object_or_404(User,username=request.user.username)
        try:
            print("in try")
            requirements = RequirementsR.objects.get(user=user)
        except RequirementsR.DoesNotExist:
            requirements = RequirementsR(user=user)
            requirements.save()
        print("finished try")
        if request.method == 'POST':
            print("in post")
            form = UpdateRequirementsRForm(request.POST, instance=requirements)
            if form.is_valid():
                print("its valid")
                form.save()
                messages.success(request, f'Your Requirements have been saved!')
                update_scores(request)
            return redirect('profile', user)
        else:
            print('not post')
            form = UpdateRequirementsRForm(instance=requirements)
        return render(request, 'status/requirementsR.html', {'form': form, 'user_profile': username})
    except Exception as e:
        print("is exception - ", e)
        return e

@login_required
def likes_me(request):
    try:
        user = get_object_or_404(User, username=request.user.username)
        list_items = Likes.objects.all()
        profile = Profile.objects.get(user=user)
        online_status = profile.profile_status
        items_to_return =[]
        if online_status == "StatusEnter":
            list_items = list_items.filter(User_enter=user)
            list_items = list_items.filter(insert_likes_enter=True)
            for item in list_items:
                score = Scores.objects.get(Username_enter = user, Username_insert = item.User_insert)
                prop = PropertyForOffer.objects.get(user = item.User_insert)
                image = Image.objects.filter(property = prop).first()
                items_to_return.append(Posts(score, image, True))
        else:
            list_items = list_items.filter(User_insert=user)
            list_items = list_items.filter(enter_likes_insert=True)
            for item in list_items:
                score = Scores.objects.get(Username_insert = user, Username_enter = item.User_enter)
                items_to_return.append(Posts(score, None, True))
        return render(request, 'likes_me.html', {"list_items": items_to_return})
    except Exception as e:
        return e


@login_required
def i_like(request):
    try:
        user = get_object_or_404(User, username=request.user.username)
        list_items = Likes.objects.all()
        profile = Profile.objects.get(user=user)
        online_status = profile.profile_status
        items_to_return =[]
        if online_status == "StatusEnter":
            list_items = list_items.filter(User_enter=user)
            list_items = list_items.filter(enter_likes_insert=True)
            for item in list_items:
                score = Scores.objects.get(Username_enter = user, Username_insert = item.User_insert)
                prop = PropertyForOffer.objects.get(user = item.User_insert)
                image = Image.objects.filter(property = prop).first()
                items_to_return.append(Posts(score, image, True))
        else:
            list_items = list_items.filter(User_insert=request.user)
            list_items = list_items.filter(insert_likes_enter=True)
            for item in list_items:
                score = Scores.objects.get(Username_insert = user, Username_enter = item.User_enter)
                items_to_return.append(Posts(score, None, True))
        return render(request, 'i_like.html', {"list_items": items_to_return})
    except Exception as e:
        return e

@login_required
def more(request):
    context = {}
    items = get_queryset(request, User.objects.all())
    if request.user.profile.profile_status == 'StatusEnter':
        context['offerP_form'] = PropertyOfferFilter(request.GET, PropertyForOffer.objects.all())
        context['reqsR_form'] = RoommateFilter(request.GET, Profile.objects.all())
    else:
        context['offerP_form'] = None
        context['reqsR_form'] = RoommateFilter(request.GET, Profile.objects.all())
    print("in more - ", len(items))
    return more_items(request, items, template='more.html')



    # return more_items(request, users,
    #                       # (optional) your custom template
    #                       template='more.html')


@login_required
# def post_list(request):
#     data = {
#         'more_posts_url': reverse('more'),
#     }
#     items = get_queryset(request, User.objects.all())
#     if request.user.profile.profile_status == 'StatusEnter':
#         data['offerP_form'] = PropertyOfferFilter(request.GET, PropertyForOffer.objects.all())
#         data['reqsR_form'] = RoommateFilter(request.GET, Profile.objects.all())
#     else:
#         data['offerP_form'] = None
#         data['reqsR_form'] = RoommateFilter(request.GET, Profile.objects.all())
#     paginated = get_pagination(request, items)
#     print("in post list - ", len(items))
#     # data = {
#     #     'more_posts_url': reverse('more'),
#     # }
#     data.update(paginated)
#     # context['data']= data
#     return render(request, 'post_list.html', data)
#         # return render(request, 'tests_templates/post_list_test.html', data)

def post_list(request):
    data = {
        'more_posts_url': reverse('more'),
    }
    if request.method == 'GET':
        if request.user.profile.profile_status == 'StatusEnter':
            not_display = Likes.objects.filter(User_enter=request.user, enter_likes_insert=False)
            not_display = [like.User_insert.username for like in not_display]
            data['offerP_form'] = PropertyOfferFilter(request.GET, PropertyForOffer.objects.all())
            data['reqsR_form'] = RoommateFilter(request.GET, Profile.objects.all())
        else:
            not_display = Likes.objects.filter(User_insert=request.user, insert_likes_enter=False)
            not_display = [like.User_enter.username for like in not_display]
            data['offerP_form'] = None
            data['reqsR_form'] = RoommateFilter(request.GET, Profile.objects.all())

        items = get_queryset(request, User.objects.exclude(username__in=not_display))
        data['recommended_roommates'] = rec_sys.recommend_roommates(request.user)
        paginated = get_pagination(request, items)
        data.update(paginated)
        return render(request, 'post_list.html', data)

 
def get_queryset(request, users):
    data_to_return = []
    # print(f'\nrequest_data: {request.GET}\n')
    # print(f'users: {users}\n')
    if request.user.profile.profile_status == 'StatusEnter':
        profiles_filterset = RoommateFilter(request.GET, Profile.objects.filter(user__in = users))
        if profiles_filterset.is_valid():
            # print(f'profiles_filterset: {profiles_filterset.qs}\n' )
            filter_users= [profile.user for profile in profiles_filterset.qs]
            # print(f'filter_users: {filter_users}\n')
            prop_filterset = PropertyOfferFilter(request.GET, queryset=PropertyForOffer.objects.filter(user__in = filter_users))
            if prop_filterset.is_valid():
                # print(f'prop_filterset: {prop_filterset.qs}\n')
                for prop in prop_filterset.qs:
                    scores = Scores.objects.filter(Username_insert=prop.user, Username_enter=request.user)
                    if scores:
                        score = scores[0]
                        image = Image.objects.filter(property=prop).first()
                        like = Likes.objects.get_or_create(User_enter=request.user, User_insert=score.Username_insert)[0]
                        context = {
                            'score': score.Enter_score,
                            'user': score.Username_insert,
                            'image': image,
                            'like': like.enter_likes_insert}
                        data_to_return.append(context)
    else:
        profiles_filterset = RoommateFilter(request.GET, Profile.objects.filter(user__in = users)) 
        if profiles_filterset.is_valid():
            for profile in profiles_filterset.qs:
                score = Scores.objects.filter(Username_enter=profile.user, Username_insert=request.user)
                if score:
                    score = score[0]
                    like = Likes.objects.get_or_create(User_enter=profile.user, User_insert=request.user)[0]
                    context = {
                        'score': score.Insert_score,
                        'user': score.Username_enter,
                        'image': None,
                        'like': like.insert_likes_enter}
                    data_to_return.append(context)
        # print(f'data_to_return: {data_to_return}\n')

    data_to_return = sorted(data_to_return, key=lambda x: x['score'], reverse=True)
    return data_to_return
   

# def update_scores(request):
#     # print("    -----------------    SCORE UPDATE    -----------------    ")
#     online_user = request.user
#     Scores.objects.filter(Username_enter=online_user).delete()
#     Scores.objects.filter(Username_insert=online_user).delete()
#     profile = Profile.objects.get(user=online_user)
#     online_status = profile.profile_status
#     status_match = 'StatusEnter' if online_status == 'StatusInsert' else 'StatusInsert'
#     potential_profiles = Profile.objects.filter(profile_status=status_match)
#     reqR = make_requirementsR(online_user)
#     if online_status == 'StatusEnter':
#         reqP = make_requirementsP(request.user)
#         for user in potential_profiles:
#             score_enter = round(update_scores_enter(reqR, reqP, user.user))
#             requirement = make_requirementsR(user.user)
#             score_insert = round(update_scores_insert(
#                 requirement, online_user))
#             score = Scores(Username_enter=online_user, Username_insert=user.user,
#                            Enter_score=score_enter, Insert_score=score_insert)
#             score.save()
#             # print("score insert - (", online_user.username,")\t", score_insert, "\nscore enter (", user.user.username,")- \t", score_enter)
#     else:
#         for user in potential_profiles:
#             requirement = make_requirementsR(user.user)
#             reqP = make_requirementsP(user.user)
#             score_enter = round(update_scores_enter(
#                 requirement, reqP, online_user))
#             score_insert = round(update_scores_insert(reqR, user.user))
#             score = Scores(Username_enter=user.user, Username_insert=online_user,
#                            Enter_score=score_enter, Insert_score=score_insert)
#             score.save()
#             # print("score insert - (", user.user.username,")\t\n", score_insert, "score enter (", online_user.username,")- \t", score_enter)
#

def after_status_update(request):
    online_user = request.user
    profile = Profile.objects.get(user=online_user)
    online_status = profile.profile_status
    if online_status == 'StatusEnter':
        # Scores.objects.filter(Username_insert=online_user).delete()
        PropertyForOffer.objects.filter(user=online_user).delete()
        Likes.objects.filter(User_insert=online_user).delete()
        PropertyForOffer.objects.filter(user=online_user).delete()
        # todo: check if need to delete image or cascade?
    else:
        # Scores.objects.filter(Username_enter=online_user).delete()
        RequirementsP.objects.filter(user=request.user).delete()
        Likes.objects.filter(User_enter=online_user).delete()
    update_scores(request)


# def update_scores_enter(requirementsR, requirementsP, user):
#     if requirementsR is None and requirementsP is None:
#         return 100
#     elif requirementsR is None:
#         personal_scoreP = calculate_score(requirementsP, user)
#         return (personal_scoreP + 100) / 2
#     elif requirementsP is None:
#         personal_score = calculate_score(requirementsR, user)
#         return (personal_score + 100) / 2
#     else:
#         personal_scoreR = calculate_score(requirementsR, user)
#         personal_scoreP = calculate_score(requirementsP, user)
#         personal_score = (personal_scoreR + personal_scoreP)/2
#         return personal_score


# def update_scores_insert(requirementsR, user):
#     if requirementsR is None:
#         return 100
#     else:
#         personal_score = calculate_score(requirementsR, user)
#         return personal_score


@login_required
def like_picture(request, username):
    other_user = User.objects.get(username=username)
    profile = Profile.objects.get(user=request.user)
    online_status = profile.profile_status
    if online_status == "StatusEnter":
        like = Likes.objects.get_or_create(
            User_enter=request.user, User_insert=other_user)[0]
        like.enter_likes_insert = True
        like.save()
    else:
        like = Likes.objects.get_or_create(
            User_enter=other_user, User_insert=request.user)[0]
        like.insert_likes_enter = True
        like.save()
    return redirect('post_list_page')


@login_required
def unlike_picture(request, username):
    other_user = User.objects.get(username=username)
    profile = Profile.objects.get(user=request.user)
    online_status = profile.profile_status
    if online_status == "StatusEnter":
        like = Likes.objects.get_or_create(
            User_enter=request.user, User_insert=other_user)[0]
        like.enter_likes_insert = None
        like.save()
    else:
        like = Likes.objects.get_or_create(
            User_enter=other_user, User_insert=request.user)[0]
        like.insert_likes_enter = None
        like.save()
    return redirect('post_list_page')

@login_required
def remove_picture(request, username):
    print('in remove_picture')
    other_user = User.objects.get(username=username)
    profile = Profile.objects.get(user=request.user)
    online_status = profile.profile_status
    if online_status == "StatusEnter":
        like = Likes.objects.get_or_create(
            User_enter=request.user, User_insert=other_user)[0]
        like.enter_likes_insert = False
        like.save()
    else:
        like = Likes.objects.get_or_create(
            User_enter=other_user, User_insert=request.user)[0]
        like.insert_likes_enter = False
        like.save()
    return redirect('post_list_page')

@login_required
def like_profile(request, username):
    other_user = User.objects.get(username=username)
    profile = Profile.objects.get(user=request.user)
    online_status = profile.profile_status
    if online_status == "StatusEnter":
        like = Likes.objects.get_or_create(
            User_enter=request.user, User_insert=other_user)[0]
        like.enter_likes_insert = True
        like.save()
    else:
        like = Likes.objects.get_or_create(
            User_enter=other_user, User_insert=request.user)[0]
        like.insert_likes_enter = True
        like.save()
    context={
        'user_profile':other_user,
        'u_form': UserUpdateForm(instance=other_user),
        'p_form': ProfileUpdateForm(instance=other_user.profile),
        'like': True}
    return render(request, 'users/profile.html', context)

@login_required
def unlike_profile(request, username):
    other_user = User.objects.get(username=username)
    profile = Profile.objects.get(user=request.user)
    online_status = profile.profile_status
    if online_status == "StatusEnter":
        like = Likes.objects.get_or_create(
            User_enter=request.user, User_insert=other_user)[0]
        like.enter_likes_insert = None
        like.save()
    else:
        like = Likes.objects.get_or_create(
            User_enter=other_user, User_insert=request.user)[0]
        like.insert_likes_enter = None
        like.save()
    context={
        'user_profile':other_user,
        'u_form': UserUpdateForm(instance=other_user),
        'p_form': ProfileUpdateForm(instance=other_user.profile),
        'like': False}
    return render(request, 'users/profile.html', context)

@login_required
def remove_recommand(request, username):
    print('in remove_recommand')
    other_user = User.objects.get(username=username)
    profile = Profile.objects.get(user=request.user)
    online_status = profile.profile_status
    if online_status == "StatusEnter":
        like = Likes.objects.get_or_create(
            User_enter=request.user, User_insert=other_user)[0]
        like.enter_likes_insert = False
        like.save()
    else:
        like = Likes.objects.get_or_create(
            User_enter=other_user, User_insert=request.user)[0]
        like.insert_likes_enter = False
        like.save()
    return redirect('post_list_page')


# # todo: need to add somehow functionality for disqualifiers
# def make_requirementsP(user):
#     try:
#         reqP = []
#         requirementP = RequirementsP.objects.get_or_create(user=user)[0]
#
#         field_mappings = {
#             "rent": ((requirementP.MinRent), requirementP.MaxRent),
#             "rooms_number": (requirementP.MinRooms, requirementP.MaxRooms),
#             "roomates_number": (requirementP.MinRoommates, requirementP.MaxRoommates),
#             "toilets_number": (requirementP.MinToilets, None),
#             "showers_number": (requirementP.MinShowers, None),
#             "shelter_inside": requirementP.ShelterInside,
#             "shelter_nearby": requirementP.ShelterNearby,
#             "furnished": requirementP.Furnished,
#             "renovated": requirementP.Renovated,
#             "shared_livingroom": requirementP.SharedLivingRoom,
#             "Location": requirementP.Location
#         }
#
#         for field, value in field_mappings.items():
#             if field in ["rent", "rooms_number", "roomates_number", "toilets_number", "showers_number"]:
#                 if field == "rent":
#                     reqP.append(RangReq.RangeReq(False, requirementP.Weight, field, *value))
#                 else:
#                     reqP.append(RangReq.RangeReq(False, requirementP.Weight, field, *value))
#             elif field == "location":
#                 reqP.append(LocationReq(False, requirementP.Weight, field, value))
#             elif field in ["shared_livingroom", "renovated", "furnished", "shelter_nearby", "shelter_inside"]:
#                 reqP.append((YNReq.YNReq(False, requirementP.Weight, field, value)))
#             else:
#                 reqP.append(ListReq.ListReq(False, requirementP.Weight, field, value))
#
#         return reqP
#     except Exception as e:
#         print(e)
#         return []


# # todo: need to add somehow functionality for disqualifiers
# def make_requirementsR(user):
#     try:
#         reqR = []
#         requirementR = RequirementsR.objects.get_or_create(user=user)[0]
#
#         field_mappings = {
#             "gender": requirementR.Gender,
#             "occupation": requirementR.Occupation,
#             "smoker": requirementR.Smoker,
#             "diet": requirementR.Diet,
#             "status": requirementR.Status,
#             "hospitality": requirementR.Hospitality,
#             "kosher": requirementR.Kosher,
#             "expense_management": requirementR.Expense_Management,
#             "birthdate": (requirementR.MinAge, requirementR.MaxAge),
#         }
#
#         for field, value in field_mappings.items():
#             if field == "birthdate":
#                 reqR.append(RangReq.RangeReq(False, requirementR.Weight, field, *value))
#             else:
#                 reqR.append(ListReq.ListReq(False, requirementR.Weight, field, value))
#
#         return reqR
#     except Exception as e:
#         print(e)
#         return []
#
#
# def calculate_score(reqs, user):
#     # print("in calculate score")
#     print("\t\t---------------------\t\t", user.username,"\t\t---------------------\t\t")
#     score = 0
#     req_counter = 0
#     try:
#         property = PropertyForOffer.objects.get(user=user)
#     except Exception as e1:
#         # print("property error - \t",e1)
#         property = None
#         # print("property is none")
#     for req in reqs:
#         req_text = req._text
#         try:
#             req_score = req.calculate_score(getattr(user, req_text))
#             # print("in first try")
#         except Exception as e2:
#             # print("2.\t",e2)
#             try:
#                 req_score = req.calculate_score(
#                     getattr(user.profile, req_text))
#                 # print("in second try")
#             except Exception as e3:
#                 # print("3.\t",e3)
#                 try:
#                     req_score = req.calculate_score(
#                         getattr(property, req_text))
#                     # print("in third try")
#                 except Exception as e4:
#                     print("\t\t-------------\t\tDOESNT WORK\t\t-------------\t\t")
#                     print("req text  -  ", req_text)
#                     print(e2,'\n', e3,'\n', e4,'\n')
#                     req_score = None
#         if req_score is not None:
#             score += req_score
#             req_counter += 1
#             req_score = None
#     if req_counter == 0:
#         # print("counter = 0,\tscore = ", score)
#         # print("\t\t-------------------------------------------------------------------\t\t\n\n")
#         return 0
#     else:
#         # print("counter = ",req_counter,"\tscore = ", score)
#         # print("\t\t-------------------------------------------------------------------\t\t\n\n")
#         return score / req_counter


class Posts:
    def __init__(self, item=None, prop=None,image=None, like=None):
        self.prop = prop
        self.image = image
        self.item = item
        self.like = like


class UserHomepageView(APIView):
    def get(self, request):
        return render(request, 'post_list_test.html')
