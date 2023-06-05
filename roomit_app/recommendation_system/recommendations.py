from django.contrib.auth.models import User
from roomit_app.models import Likes, RequirementsP, RequirementsR
from roomit_app.recommendation_system.compare_profiles import compare_profiles
from roomit_app.recommendation_system.compare_reqs import compare_reqP, compare_reqR

# lower bound of similarity score to recommend
matching_score_to_pass = 0.85


def recommend_roommates(user):
    status = user.profile.profile_status

    # Get all the users that the given user has liked
    same_status_users = get_other_users(user, status)

    # Initialize an empty list to store recommended roommates
    recommended_roommates = []

    # Iterate over all the users that the given user has liked
    for liked_user in same_status_users:

        # Compare the liked user's profile with the given user's profile
        similarity_score = compare_users(user, liked_user)

        print("SCORE :  ", similarity_score, "\t USER :  ", liked_user)

        # If the similarity score is high enough, add the liked user's likes to the recommended roommates list
        print("similarity_score  -  ", similarity_score, "  >=  matching_score_to_pass  -   ",matching_score_to_pass, "\t", similarity_score >= matching_score_to_pass)
        if similarity_score >= matching_score_to_pass:
            users_to_append = get_liked_users(liked_user, status, user)
            recommended_roommates.extend(users_to_append)
            print(users_to_append)

    # Remove duplicates from the recommended roommates list
    recommended_roommates = list(set(recommended_roommates))

    if user in recommended_roommates:
        recommended_roommates.remove(user)

    # print("RECOMMENDED ROOMMATES")
    # print(recommended_roommates)

    return recommended_roommates


def compare_users(user1, user2):
    # get profile similarity score
    profile_score, fields_in_profile = compare_profiles(user1.profile, user2.profile)
    # print("PROFILE :  \t", profile_score, fields_in_profile)

    # get property requirements similarity score
    if user1.profile.profile_status == "StatusEnter":
        reqP1, reqP2 = RequirementsP.objects.get(user=user1), RequirementsP.objects.get(user=user2)
        reqP_score, fields_in_reqP = compare_reqP(reqP1, reqP2)
        # print("reqP :  \t", reqP_score, fields_in_reqP)
    else:
        reqP_score, fields_in_reqP = 0, 0

    # get roommate requirements similarity score
    reqR1, reqR2 = RequirementsR.objects.get(user=user1), RequirementsR.objects.get(user=user2)
    reqR_score, fields_in_reqR = compare_reqR(reqR1, reqR2)
    # print("reqR :  \t", reqR_score, fields_in_reqR)

    # calc numerator & denominator
    numerator = profile_score + reqP_score + reqR_score
    denominator = fields_in_profile + fields_in_reqP + fields_in_reqR

    # return the similarity score avg
    return numerator / denominator


# returns all users liked by user
# for each user check if he was already liked by the online user
# only the users that he didn't like already will be added
def get_liked_users(user, status, online_user):
    users_list = []
    if status == "StatusEnter":
        liked_users = Likes.objects.filter(User_enter=user, enter_likes_insert=True)
        for like in liked_users:
            liked_user = like.User_insert
            try:
                Likes.objects.get(User_enter=online_user, User_insert=liked_user ,enter_likes_insert=True)
            except Likes.DoesNotExist:
                users_list.append(liked_user)
    else:
        liked_users = Likes.objects.filter(User_insert=user, insert_likes_enter=True)
        for like in liked_users:
            liked_user = like.User_enter
            try:
                Likes.objects.get(User_insert=online_user, User_enter=liked_user ,insert_likes_enter=True)
            except Likes.DoesNotExist:
                users_list.append(liked_user)
    return list(users_list)


# returns all users with similar profiles, sorted in descending order keyed by the number of users they liked
def get_other_users(online_user, status):
    users = User.objects.filter(profile__profile_status=status)

    # Create an empty dictionary to store the like counts for each user
    user_like_counts = {}
    # create list of users to compare
    for user in users:
        # if online user is the current user, don't add him to the list
        if not (online_user.username == user.username):
            # Count the number of likes for the current user
            if status == "StatusEnter":
                like_count = Likes.objects.filter(User_enter=user, enter_likes_insert=True).count()
            else:
                like_count = Likes.objects.filter(User_insert=user, insert_likes_enter=True).count()

            # Store the like count for the user in the dictionary
            user_like_counts[user] = like_count

    # Sort the users based on the like counts in descending order
    sorted_users = sorted(user_like_counts, key=user_like_counts.get, reverse=True)

    return sorted_users



# user_check = User.objects.get(username="Eylon")
# user_list = recommend_roommates(user_check)
# print(user_list)
