import datetime
from django.http import HttpRequest
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.shortcuts import reverse
from users.forms import UserUpdateForm, ProfileUpdateForm
from users.views import profile
from django.contrib import messages


class ProfileViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testusername', email= 'testemail@test.com', password= 'testpassword')
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

    def test_profile_post_valid_form(self):
        self.client.login(username='testusername', password='testpassword')
        request = HttpRequest()
        request.user = self.user
        request.method = 'POST'
        request.POST = {
            'first_name': 'John',
            'last_name': 'Doe',
            'birthdate': '05/05/2022',
            'phone_number': '+972526083915',
            'gender': 'M',
        }
        request.META['HTTP_HOST'] = 'localhost'
        response = profile(request, self.user.username)

        self.assertEqual(response.status_code, 200)
        # assertions to check if the form data was saved correctly
        updated_user = self.user.profile
        self.assertEqual(updated_user.first_name, 'John')
        self.assertEqual(updated_user.last_name, 'Doe')
        self.assertEqual(updated_user.birthdate, datetime.date(2022, 5, 5))
        self.assertEqual(updated_user.phone_number, '+972526083915')
        self.assertEqual(updated_user.gender, 'M')
        self.client.logout()


    def test_info_post_invalid_form(self):
            self.client.login(username='testusername', password='testpassword')
            url = reverse('profile', args=['testusername'])
            response = self.client.post(url, data={'first_name': 'Jon'}, content_type= "application/x-www-form-urlencoded")
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'users/profile.html')
            self.assertIsInstance(response.context['p_form'], ProfileUpdateForm)
            self.assertNotEqual(self.user.profile.first_name, 'Jon')
            self.client.logout()




        