

from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from django.contrib.auth.models import User
from users.views import display_property_reqs


class DisplayPropertyReqsViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testusername', email='testemail@test.com', password='testpassword')

    def tearDown(self):
            self.user.delete()

    def test_display_property_offer_get(self):
        url = reverse('property-offer-display', args=[self.user.username])
        request = self.client.get(url)
        request.user = self.user

        self.assertEqual(request.status_code, 302)
    
    def test_display_property_reqs_post_invalid_form(self):
            url = reverse('property-reqs-display', args=[self.user.username])
            form_data = {}
            request = self.client.post(url, data=form_data)
            request.user = self.user
            self.assertEqual(request.status_code, 302)