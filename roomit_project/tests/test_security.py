import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'roomit_project.settings'
django.setup()

from django.test import TestCase, Client
from django.urls import reverse


class SecurityTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # self.user = User.objects.create_user(username='eylon', password='sade12345')
        # self.admin_user = User.objects.create_superuser(username='admin', password='admin12345')

    # no user is logged in, tries to go to admin page, instead gets redirected to login page
    def test_unauthorized_access(self):
        response = self.client.get(reverse('admin:index'))
        self.assertEqual(response.status_code, 302)  # redirect to login page

    # admin tries to login with wrong password
    def test_invalid_credentials(self):
        response = self.client.post(reverse('login'), {'username': 'admin', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please enter a correct username and password.')

    # user tries to reset password
    def test_password_reset(self):
        response = self.client.post(reverse('password_reset'), {'email': 'eylon@gamil.com'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('password_reset_done'))

    # when regular user is logged-in and tries to go to admin page the systemm redirects him to the login page
    # when the admin is logged-in the system will allow him to proceed to the admin page
    def test_role_permissions(self):
        self.client.login(username='eylon', password='sade12345')
        response = self.client.get(reverse('admin:index'))
        self.assertEqual(response.status_code, 302)  # redirect to login page

        self.client.login(username='admin', password='admin12345')
        response = self.client.get(reverse('admin:index'))
        self.assertEqual(response.status_code, 200)  # admin page access granted

    def test_input_sanitization(self):
        # Create a user with a malicious input
        malicious_input = '<script>alert("Hello world!")</script>'
        response = self.client.post(reverse('login'), {'username': malicious_input, 'password': 'password'}, follow=True)
        # Check that the response does not contain the malicious input
        self.assertNotContains(response, malicious_input)

    # def test_sql_injection(self):
    #     # Attempt a SQL injection attack by submitting malicious input
    #     malicious_input = "'; DROP TABLE Users; --"
    #     response = self.client.get('user/register/')
    #     csrftoken = response.cookies['csrftoken']
    #     response = self.client.post('user/register/', {'username': malicious_input,"password1": malicious_input, "password2": malicious_input, "email": malicious_input}, headers={'X-CSRFToken': csrftoken})
    #     self.assertNotEqual(response.status_code, 500)
    #
    # def test_xss(self):
    #     # Attempt a XSS attack by submitting malicious input
    #     malicious_input = "<script>alert('XSS');</script>"
    #     response = self.client.get('user/register/')
    #     csrftoken = response.cookies['csrftoken']
    #     response = self.client.post('user/register/', {'username': malicious_input,"password1": malicious_input, "password2": malicious_input, "email": malicious_input}, headers={'X-CSRFToken': csrftoken})
    #     self.assertNotEqual(response.status_code, 500)
