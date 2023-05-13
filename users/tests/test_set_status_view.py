from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from django.urls import reverse

from users.views import set_status
from users.models import Profile

from django.contrib import messages

class SetStatusViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_set_status_get_redirect_insert(self):
        url = reverse('set-status')
        request = self.factory.get(url, {'status': 'StatusInsert'})
        request.user = self.user

        response = set_status(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('property-offer-create', args=[self.user.username]))

        profile = Profile.objects.get(user=self.user)
        self.assertEqual(profile.profile_status, 'StatusInsert')

    def test_set_status_get_redirect_enter(self):
        url = reverse('set-status')
        request = self.factory.get(url, {'status': 'StatusEnter'})
        request.user = self.user

        response = set_status(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('requirementsP', args=[self.user.username]))

        profile = Profile.objects.get(user=self.user)
        self.assertEqual(profile.profile_status, 'StatusEnter')

   