from django.contrib.auth.models import User
from roomit_app.models import Likes
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

        # If the similarity score is high enough, add the liked user's likes to the recommended roommates list
        if similarity_score >= matching_score_to_pass:
            recommended_roommates.extend(get_liked_users(liked_user, status))

    # Remove duplicates from the recommended roommates list
    recommended_roommates = list(set(recommended_roommates))

    return recommended_roommates


def compare_users(user1, user2):
    # get profile, roommate requirements, and property requiremenets similarity score
    profile_score, fields_in_profile = compare_profiles(user1, user2)
    reqP_score, fields_in_reqP = compare_reqP(user1, user2)
    reqR_score, fields_in_reqR = compare_reqR(user1, user2)

    # calc numerator & denominator
    numerator = profile_score + reqP_score + reqR_score
    denominator = fields_in_profile + fields_in_reqP + fields_in_reqR

    # return the similarity score avg
    return numerator / denominator


# returns all users liked by user
def get_liked_users(user, status):
    if status == "StatusEnter":
        liked_users = Likes.objects.filter(User_enter=user, enter_likes_insert=True)
    else:
        liked_users = Likes.objects.filter(User_insert=user, insert_likes_enter=True)
    return liked_users


# returns all users with similar profiles, sorted in descending order keyed by the number of users they liked
def get_other_users(status):
    users = User.objects.filter(profile__profile_status=status)

    # Create an empty dictionary to store the like counts for each user
    user_like_counts = {}

    for user in users:
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
