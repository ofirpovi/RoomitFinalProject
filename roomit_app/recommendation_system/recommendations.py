# from compare_profiles import *
# from compare_reqs import compare_reqP, compare_reqR
from django.db.models import Count
from django.contrib.auth.models import User


def recommend_roommates(user):
    # Get all the users that the given user has liked
    liked_users = get_another_user(user)

    # Initialize an empty list to store recommended roommates
    recommended_roommates = []

    # Iterate over all the users that the given user has liked
    for liked_user in liked_users:
        # Compare the liked user's profile with the given user's profile
        # similarity_score = compare_profiles(user, liked_user)
        similarity_score = 1
        # If the similarity score is high enough, add the liked user's likes to the recommended roommates list
        if similarity_score >= 0.8:  # you can adjust the threshold as needed
            recommended_roommates.extend(get_another_user(liked_user))

    # Remove duplicates from the recommended roommates list
    recommended_roommates = list(set(recommended_roommates))

    return recommended_roommates


def get_liked_users(user):
    # Your code here to retrieve a list of users that user has liked
    return


def get_another_user(status):
    users = User.objects.filter(
        profile__profile_status=status,
        enter_likes_insert__like_field=True
    ).annotate(
        like_count=Count('enter_likes_insert__User_insert')
    ).order_by('-like_count')
    for user in users:
        print(user)
    return users
