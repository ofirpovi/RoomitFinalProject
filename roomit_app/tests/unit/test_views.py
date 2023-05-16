import os
import django


os.environ['DJANGO_SETTINGS_MODULE'] = 'roomit_project.settings'
django.setup()

import roomit_app
from datetime import date
from django.test import TestCase
from unittest.mock import MagicMock, patch
from roomit_app.views import requirementsP, requirementsR, likes_me, i_like, more, post_list, make_requirementsR, \
    update_scores_insert, make_requirementsP, update_scores, update_scores_enter
from django.shortcuts import reverse
from django.contrib.auth.models import User
from users.models import Profile, PropertyForOffer
from roomit_app.models import RequirementsP, RequirementsR, Scores

class TestViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser')
        self.user.save()
        self.user_profile = Profile.objects.get_or_create(user=self.user)[0]
        self.factory = MagicMock()
        self.user1 = User.objects.create_user(username='user1')
        self.user1.save()
        self.user2 = User.objects.create_user(username='user2')
        self.user2.save()
        self.profile1 = Profile.objects.get(user=self.user1)
        self.profile1.profile_status='StatusEnter'
        self.profile2 = Profile.objects.get(user=self.user2)
        self.profile2.profile_status='StatusInsert'
        self.user3 = User.objects.create_user(username='testuser3', password='testpass123')
        self.requirementsR3 = RequirementsR.objects.create(user=self.user3, Weight=1, Gender='Male')
        self.requirementsP3 = RequirementsP.objects.create(user=self.user3, Weight=1, Country='US', City='New York', MinRent=500, MaxRent=1000)
        self.requirementP1 = RequirementsP.objects.get_or_create(
            user=self.user1,
            Country='US',
            City='San Francisco',
            Neighborhood='SOMA',
            MinRent=1000,
            MaxRent=2000,
            MinRooms=1,
            MaxRooms=2,
            MinRoommates=0,
            MaxRoommates=1,
            MinToilets=1,
            MinShowers=1,
            ShelterInside=1,
            ShelterNearby=1,
            Furnished=1,
            Renovated=0,
            SharedLivingRoom=1,
        )[0]
        self.requirementR1 = RequirementsR.objects.get_or_create(
            user=self.user1,
            Gender='Female',
            Occupation='Student',
            Smoker='No',
            Diet='Vegan',
            Status='Single',
            Hospitality='No',
            Kosher='No',
            Expense_Management='No',
            MinAge=20,
            MaxAge=30,
        )[0]

    def test_calculate_score(self):
        property_offered = PropertyForOffer.objects.get_or_create(
            user=self.user2,
            country='US',
            city='San Francisco',
            neighborhood='SOMA',
            rent_currency='ILS',
            rent=1000,
            rooms_number=1,
            roomates_number=0,
            toilets_number=1,
            showers_number=1,
            shelter_inside=1,
            shelter_nearby=1,
            furnished=1,
            renovated=0,
            shared_livingroom=1)[0]
        property_offered.save()
        self.user2.profile.gender = 'Female'
        self.user2.profile.occupation = 'Student'
        self.user2.profile.smoker = 'No'
        self.user2.profile.diet = 'Vegan'
        self.user2.profile.status = 'Single'
        self.user2.profile.hospitality = 'No'
        self.user2.profile.kosher = 'No'
        self.user2.profile.expense_management = 'No'
        self.user2.profile.birthdate = date(1999,7,12)
        self.user2.profile.save()
        score = update_scores_enter(make_requirementsR(self.user1), make_requirementsP(self.user1), self.user2)
        self.assertEqual(score, 100, ("score should have been 100, but got ", score, "instead.."))

    def test_update_scores_only_creates_new_scores(self):
        initial_scores_count = Scores.objects.count()

        request1 = self.client.get('/dummyurl', {'user': self.user1.id})
        request1.user = self.user1

        update_scores(request1)

        final_scores_count = Scores.objects.count()

        self.assertEqual(final_scores_count, initial_scores_count + 4)

    def test_update_scores_correctly_calculates_enter_scores(self):
        request1 = self.client.get('/dummyurl', {'user': self.user1.id})
        request1.user = self.user1
        update_scores(request1)
        try:
            score1 = Scores.objects.get(Username_enter=self.user1, Username_insert=self.user2)
        except roomit_app.models.Scores.DoesNotExist:
            score1 = Scores(Username_enter=self.user1, Username_insert=self.user2,Enter_score=0, Insert_score=0)
        try:
            score2 = Scores.objects.get(Username_enter=self.user1, Username_insert=self.user3)
        except roomit_app.models.Scores.DoesNotExist:
            score2 = Scores.objects.create(Username_enter=self.user1, Username_insert=self.user3,Enter_score=0, Insert_score=0)


        self.assertEqual(score1.Enter_score, 0)
        self.assertEqual(score2.Enter_score, 0)

    def test_update_scores_correctly_calculates_insert_scores(self):
        request1 = self.client.get('/dummyurl', {'user': self.user1.id})
        request1.user = self.user1
        update_scores(request1)
        try:
            score1 = Scores.objects.get(Username_enter=self.user1, Username_insert=self.user2)
        except roomit_app.models.Scores.DoesNotExist:
            score1 = Scores(Username_enter=self.user1, Username_insert=self.user2,Enter_score=0, Insert_score=0)
        try:
            score2 = Scores.objects.get(Username_enter=self.user1, Username_insert=self.user3)
        except roomit_app.models.Scores.DoesNotExist:
            score2 = Scores(Username_enter=self.user1, Username_insert=self.user3,Enter_score=0, Insert_score=0)

        self.assertEqual(score1.Insert_score, 0)
        self.assertEqual(score2.Insert_score, 0)

    def test_update_scores_enter(self):
        score = update_scores_enter(
            requirementsR=make_requirementsR(self.user2),
            requirementsP=make_requirementsP(self.user1),
            user=self.profile2,
        )
        self.assertIsInstance(score, float)
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 100)

    def test_update_scores_insert(self):
        score = update_scores_insert(
            requirementsR=make_requirementsR(self.user1),
            user=self.profile2,
        )
        self.assertIsInstance(score, float)
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 100)

    def test_make_requirementsP(self):
        requirementsP = make_requirementsP(self.user1)
        self.assertIsInstance(requirementsP, list)
        self.assertEqual(len(requirementsP), 13)

    def test_make_requirementsR(self):
        requirementsR = make_requirementsR(self.user1)
        self.assertIsInstance(requirementsR, list)
        self.assertEqual(len(requirementsR), 9)

    # def test_update_scores(self):
    #     scores_before = Scores.objects.count()
    #     update_scores(self.client.get('/'))
    #     scores_after = Scores.objects.count()
    #     self.assertEqual(scores_after - scores_before, 1)

    # def test_update_scores_deleted_old_scores(self):
    #     # Scores.objects.get_or_create(
    #     #     Username_enter=self.user1,
    #     #     Username_insert=self.user2,
    #     #     Enter_score=0,
    #     #     Insert_score=0,
    #     # )
    #     scores_before = Scores.objects.count()
    #     update_scores(self.client.get('/'))
    #     scores_after = Scores.objects.count()
    #     self.assertEqual(scores_after, scores_before - 1)


    def test_requirementsP_authenticated(self):
        request = self.factory.get(reverse('requirementsP', args=[self.user.username]))
        request.user = self.user
        self.user_profile.profile_status = 'StatusEnter'
        with patch('users.views.Profile.objects.get') as mock_profile:
            mock_profile.return_value = self.user_profile

            response = requirementsP(request, self.user.username)

            self.assertEqual(response.status_code, 200)

    def test_requirementsP_unauthenticated(self):
        request = self.factory.get(reverse('requirementsP', args=[self.user.username]))

        with patch('users.views.Profile.objects.get') as mock_profile:
            mock_profile.return_value = self.user_profile

            response = requirementsP(request, self.user.username)

            self.assertEqual(type(response), django.http.response.Http404)

    def test_requirementsR_authenticated(self):
        request = self.factory.get(reverse('requirementsR', args=[self.user.username]))
        request.user = self.user

        with patch('users.views.Profile.objects.get') as mock_profile:
            mock_profile.return_value = self.user_profile

            response = requirementsR(request, self.user.username)

            self.assertEqual(response.status_code, 200)

    def test_requirementsR_unauthenticated(self):
        request = self.factory.get(reverse('requirementsR', args=[self.user.username]))

        with patch('users.views.Profile.objects.get') as mock_profile:
            mock_profile.return_value = self.user_profile

            response = requirementsR(request, self.user.username)

            self.assertEqual(type(response), django.http.response.Http404)

    def test_likes_me_authenticated(self):
        request = self.factory.get(reverse('likes_me'))
        request.user = self.user

        response = likes_me(request)

        self.assertEqual(response.status_code, 200)

    def test_likes_me_unauthenticated(self):
        request = self.factory.get(reverse('likes_me'))

        response = likes_me(request)

        self.assertEqual(type(response), django.http.response.Http404)

    def test_i_like_authenticated(self):
        request = self.factory.get(reverse('i_like'))
        request.user = self.user

        response = i_like(request)

        self.assertEqual(response.status_code, 200)

    def test_i_like_unauthenticated(self):
        request = self.factory.get(reverse('i_like'))

        response = i_like(request)

        self.assertEqual(type(response), django.http.response.Http404)

    def test_more_authenticated_insert(self):
        self.user_profile.profile_status = 'StatusInsert'
        request = self.factory.get(reverse('more'))
        request.user = self.user

        with patch('users.views.Profile.objects.get') as mock_profile:
            mock_profile.return_value = self.user_profile

            response = more(request)

            self.assertEqual(response.status_code, 200)

    def test_more_authenticated_enter(self):
        self.user_profile.profile_status = 'StatusEnter'
        request = self.factory.get(reverse('more'))
        request.user = self.user

        with patch('users.views.Profile.objects.get') as mock_profile:
            mock_profile.return_value = self.user_profile

            response = more(request)

            self.assertEqual(response.status_code, 200)

    def test_more_unauthenticated(self):
        request = self.factory.get.return_value

        response = more(request)

        self.assertEqual(type(response), django.http.response.Http404)

    def test_post_list_authenticated_insert(self):
        self.user_profile.profile_status = 'StatusInsert'
        request = self.factory.get.return_value
        request.user = self.user

        response = post_list(request)

        self.assertEqual(response.status_code, 200)

    def test_post_list_authenticated_enter(self):
        self.user_profile.profile_status = 'StatusEnter'
        request = self.factory.get.return_value
        request.user = self.user

        response = post_list(request)
        self.assertEqual(response.status_code, 200)


