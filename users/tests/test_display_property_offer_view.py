from django.http import HttpRequest
from django.test import Client, TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from users.models import PropertyForOffer, Image
from users.views import display_property_offer
from django.contrib.messages import get_messages


class DisplayPropertyOfferViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.user = User.objects.create_user(username='testusername', email='testemail@test.com', password='testpassword')
      
    def tearDown(self):
        self.user.delete()

    def test_display_property_offer_get(self):
        url = reverse('property-offer-display', args=[self.user.username])
        request = self.factory.get(url)
        request.user = self.user

        response = display_property_offer(request, self.user.username)

        self.assertEqual(response.status_code, 200)

    def test_display_property_offer_post_valid_form(self):
        self.client.login(username='testusername', password='testpassword')
        request = HttpRequest()
        request.user = self.user
        request.method = 'POST'
        image = SimpleUploadedFile(
            "test_image.jpg", content=b'', content_type="image/jpeg")
        
        form_data = {
            'country': 'Israel', 
            'city': 'Beer-Sheva',
            'neighborhood': 'Ramot',
            'rent': '2500',
        }

        request.POST = form_data
        request.META['HTTP_HOST'] = 'localhost'
        response = display_property_offer(request, self.user.username)
        self.assertEqual(response.status_code, 200)
        self.client.logout()

    def test_display_property_offer_post_invalid_form(self):
        self.client.login(username='testusername', password='testpassword')
        request = HttpRequest()
        request.user = self.user
        request.method = 'POST'
        image = SimpleUploadedFile(
            "test_image.jpg", content=b'', content_type="image/jpeg")
        
        form_data = {}

        request.POST = form_data
        request.META['HTTP_HOST'] = 'localhost'
        response = display_property_offer(request, self.user.username)

        self.assertEqual(response.status_code, 200)