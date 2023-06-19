from roomit_app.matches.requirements.RangReq import RangeReq
from roomit_app.matches.requirements.ListReq import ListReq
from roomit_app.matches.requirements.LocationReq import LocationReq
from roomit_app.matches.requirements.YNReq import YNReq
from roomit_app.models import RequirementsR, RequirementsP, Scores
from users.models import PropertyForOffer, Profile


def update_scores(request):
    online_user = request.user
    Scores.objects.filter(Username_enter=online_user).delete()
    Scores.objects.filter(Username_insert=online_user).delete()
    profile = Profile.objects.get(user=online_user)
    online_status = profile.profile_status
    status_match = 'StatusEnter' if online_status == 'StatusInsert' else 'StatusInsert'
    potential_profiles = Profile.objects.filter(profile_status=status_match)
    reqR = make_requirementsR(online_user)
    if online_status == 'StatusEnter':
        reqP = make_requirementsP(request.user)
        for user in potential_profiles:
            score_enter = round(update_scores_enter(reqR, reqP, user.user))
            if score_enter == -1:
                score_insert = -1
                score = Scores(Username_enter=online_user, Username_insert=user.user,
                           Enter_score=score_enter, Insert_score=score_insert)
            else:
                requirement = make_requirementsR(user.user)
                score_insert = round(update_scores_insert(
                    requirement, online_user))
                score = Scores(Username_enter=online_user, Username_insert=user.user,
                           Enter_score=score_enter, Insert_score=score_insert)
            score.save()
    else:
        for user in potential_profiles:
            requirement = make_requirementsR(user.user)
            reqP = make_requirementsP(user.user)
            score_enter = round(update_scores_enter(
                requirement, reqP, online_user))
            if score_enter == -1:
                score_insert = -1
                score = Scores(Username_enter=online_user, Username_insert=user.user,
                           Enter_score=score_enter, Insert_score=score_insert)
            else:
                score_insert = round(update_scores_insert(reqR, user.user))
                score = Scores(Username_enter=user.user, Username_insert=online_user,
                           Enter_score=score_enter, Insert_score=score_insert)
            score.save()


def update_scores_enter(requirementsR, requirementsP, user):
    if requirementsR is None and requirementsP is None:
        return 100
    elif requirementsR is None:
        personal_scoreP = calculate_score(requirementsP, user)
        if personal_scoreP == -1:
            return -1
        return (personal_scoreP + 100) / 2
    elif requirementsP is None:
        personal_score = calculate_score(requirementsR, user)
        return (personal_score + 100) / 2
    else:
        personal_scoreR = calculate_score(requirementsR, user)
        personal_scoreP = calculate_score(requirementsP, user)
        if personal_scoreP == -1:
            return -1
        personal_score = (personal_scoreR + personal_scoreP)/2
        return personal_score


def update_scores_insert(requirementsR, user):
    if requirementsR is None:
        return 100
    else:
        personal_score = calculate_score(requirementsR, user)
        return personal_score


# todo: need to add somehow functionality for disqualifiers
def make_requirementsP(user):
    try:
        reqP = []
        requirementP = RequirementsP.objects.get_or_create(user=user)[0]

        field_mappings = {
            "rent": ((requirementP.MinRent), requirementP.MaxRent),
            "rooms_number": (requirementP.MinRooms, requirementP.MaxRooms),
            "roomates_number": (requirementP.MinRoommates, requirementP.MaxRoommates),
            "toilets_number": (requirementP.MinToilets, None),
            "showers_number": (requirementP.MinShowers, None),
            "shelter_inside": requirementP.ShelterInside,
            "shelter_nearby": requirementP.ShelterNearby,
            "furnished": requirementP.Furnished,
            "renovated": requirementP.Renovated,
            "shared_livingroom": requirementP.SharedLivingRoom,
            "Location": requirementP.Location
        }

        for field, value in field_mappings.items():
            if field in ["rent", "rooms_number", "roomates_number", "toilets_number", "showers_number"]:
                if field == "rent":
                    reqP.append(RangeReq(False, requirementP.Weight, field, *value))
                else:
                    reqP.append(RangeReq(False, requirementP.Weight, field, *value))
            elif field == "location":
                reqP.append(LocationReq(False, requirementP.Weight, field, value))
            elif field in ["shared_livingroom", "renovated", "furnished", "shelter_nearby", "shelter_inside"]:
                reqP.append((YNReq(False, requirementP.Weight, field, value)))
            else:
                reqP.append(ListReq(False, requirementP.Weight, field, value))

        return reqP
    except Exception as e:
        print(e)
        return []


# todo: need to add somehow functionality for disqualifiers
def make_requirementsR(user):
    try:
        reqR = []
        requirementR = RequirementsR.objects.get_or_create(user=user)[0]

        field_mappings = {
            "gender": requirementR.Gender,
            "occupation": requirementR.Occupation,
            "smoker": requirementR.Smoker,
            "diet": requirementR.Diet,
            "status": requirementR.Status,
            "hospitality": requirementR.Hospitality,
            "kosher": requirementR.Kosher,
            "expense_management": requirementR.Expense_Management,
            "birthdate": (requirementR.MinAge, requirementR.MaxAge),
        }

        for field, value in field_mappings.items():
            if field == "birthdate":
                reqR.append(RangeReq(False, requirementR.Weight, field, *value))
            else:
                reqR.append(ListReq(False, requirementR.Weight, field, value))

        return reqR
    except Exception as e:
        print(e)
        return []


def calculate_score(reqs, user):
    score = 0
    req_counter = 0
    try:
        property = PropertyForOffer.objects.get(user=user)
    except Exception as e1:
        property = None
    for req in reqs:
        req_text = req._text
        try:
            req_score = req.calculate_score(getattr(user, req_text))
        except Exception as e2:
            try:
                req_score = req.calculate_score(
                    getattr(user.profile, req_text))
            except Exception as e3:
                try:
                    req_score = req.calculate_score(
                        getattr(property, req_text))
                except Exception as e4:
                    req_score = None
        if req_score is not None:
            score += req_score
            req_counter += 1
            req_score = None
    if req_counter == 0:
        return 0
    else:
        return score / req_counter
