from django.test import TestCase, RequestFactory, Client
from django.contrib.auth.models import User
from django.shortcuts import reverse
from users.models import Profile
from users.forms import UserUpdateForm, ProfileUpdateForm


class ProfileViewTest(TestCase):
    def setUp(self):
        # self.factory = RequestFactory()
        # self.username = 'testuser'
        # self.password = 'testpassword'
        self.client = Client()
        self.user = User.objects.create_user('testusername', 'testemail@test.com', 'testpassword')
        self.other_user = User.objects.create_user('testotherusername', 'testotheremail@test.com', 'testotherpassword')

    def tearDown(self):
        self.user.delete()
        self.other_user.delete()

    def test_profile_get_user_logged(self):
        self.client.login(username='testusername', password='testpassword')
        url = reverse('profile', args=['testusername'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/profile.html')
        self.assertIsInstance(response.context['u_form'], UserUpdateForm)
        self.assertIsInstance(response.context['p_form'], ProfileUpdateForm)
        self.assertEqual(response.context['user_profile'], self.user)
        self.assertFalse(response.context['read_only'])
        self.client.logout()

    def test_profile_get_user_unlogged(self):
        url = reverse('profile', args=['testusername'])
        response = self.client.get(url, follow=True)
        self.assertRedirects(response, '/user/login/?next=' + url , status_code=302, target_status_code=200, fetch_redirect_response=True)

    def test_profile_get_read_only(self):
        self.client.login(username='testusername', password='testpassword')
        url = reverse('profile', args=['testotherusername'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/profile.html')
        self.assertIsInstance(response.context['u_form'], UserUpdateForm)
        self.assertIsInstance(response.context['p_form'], ProfileUpdateForm)
        self.assertEqual(response.context['user_profile'], self.other_user)
        self.assertTrue(response.context['read_only'])
        self.client.logout()

    def test_profile_post(self):
        self.client.login(username='testusername', password='testpassword')
        url = reverse('profile', args=['testusername'])
        response = self.client.post(url, {'first_name': 'John', 'last_name': 'Doe'}, follow= True, content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 200)  # Check the status code of the final response
        updated_user_profile = Profile.objects.get(user=self.user)
        self.assertEqual(updated_user_profile.first_name, 'John')
        self.assertEqual(updated_user_profile.last_name, 'Doe')
        self.client.logout()

