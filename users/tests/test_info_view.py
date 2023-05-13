import datetime
from django.http import HttpRequest
from django.test import RequestFactory, TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from users.models import Profile
from users.forms import ProfileUpdateForm
from users.views import info


class InfoViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.user = User.objects.create_user(
            'testusername', 'testemail@test.com', 'testpassword')

    def tearDown(self):
        self.user.delete()

    def test_info_get_user_logged(self):
        self.client.login(username='testusername', password='testpassword')
        url = reverse('fill_info', args=['testusername'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/fill_info.html')
        self.assertIsInstance(response.context['p_form'], ProfileUpdateForm)
        self.client.logout()
        
    def test_info_get_user_unlogged(self):
        url = reverse('fill_info', args=['testusername'])
        response = self.client.get(url, follow=True)
        self.assertRedirects(response, '/user/login/?next=' + url, status_code=302,
                             target_status_code=200, fetch_redirect_response=True)

    def test_info_post_valid_form(self):
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
        response = info(request, self.user.username)

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
        url = reverse('fill_info', args=['testusername'])
        response = self.client.post(url, data={'first_name': 'Jon'}, content_type= "application/x-www-form-urlencoded")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/fill_info.html')
        self.assertIsInstance(response.context['p_form'], ProfileUpdateForm)
        self.assertNotEqual(self.user.profile.first_name, 'Jon')
        self.client.logout()

        


