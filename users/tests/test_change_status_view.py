from django.contrib.auth.models import User
# from django.contrib.messages import get_messages
from django.test import TestCase, RequestFactory
from django.urls import reverse

from users.views import change_status
from users.models import Profile


class ChangeStatusViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.user.profile_status_profile= 'StatusInsert'

    def test_change_status_get_insert_to_enter(self):
        url = reverse('change-status')
        request = self.factory.get(url)
        request.user = self.user

        response = change_status(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('property-reqs-display', args=[self.user.username]))

        profile = Profile.objects.get(user=self.user)
        self.assertEqual(profile.profile_status, 'StatusEnter')

        # messages = list(get_messages(response.wsgi_request))
        # self.assertEqual(len(messages), 1)
        # self.assertEqual(str(messages[0]), "Your status has been changed. Please fill in your property's requirements")

    def test_change_status_get_enter_to_insert(self):
        self.profile.profile_status = 'StatusEnter'
        self.profile.save()

        url = reverse('change-status')
        request = self.factory.get(url)
        request.user = self.user

        response = change_status(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('property-offer-display', args=[self.user.username]))

        profile = Profile.objects.get(user=self.user)
        self.assertEqual(profile.profile_status, 'StatusInsert')

        # messages = list(get_messages(response.wsgi_request))
        # self.assertEqual(len(messages), 1)
        # self.assertEqual(str(messages[0]), "Your status has been changed. Please fill in your property's info")
