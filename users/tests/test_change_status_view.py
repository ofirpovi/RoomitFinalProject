from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import Client, TestCase, RequestFactory
from django.urls import reverse

from users.views import change_status
from users.models import Profile


class ChangeStatusViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testusername', password='testpassword')
        self.user.profile.profile_status= 'StatusInsert'
        print(f'user status in setup: {self.user.profile.profile_status}\n')

    def tearDown(self):
        self.user.delete()

    def test_change_status_get_insert_to_enter(self):
        self.client.login(username='testusername', password='testpassword')
        url = reverse('change-status')
        request = self.factory.get(url)
        request.user = self.user
        
        response = change_status(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('property-reqs-display', args=[self.user.username]))
        self.assertEqual(self.user.profile.profile_status, 'StatusEnter')

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Your status has been changed. Please fill in your property's requirements")
        self.client.logout()

    def test_change_status_get_enter_to_insert(self):
        self.client.login(username='testusername', password='testpassword')
        self.user.profile.profile_status = 'StatusEnter'
        url = reverse('change-status')
        request = self.factory.get(url)
        request.user = self.user
        
        response = change_status(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('property-offer-display', args=[self.user.username]))
        self.assertEqual(self.user.profile.profile_status, 'StatusInsert')

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Your status has been changed. Please fill in your property's info")
        self.client.logout()