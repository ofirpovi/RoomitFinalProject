from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import DateInput
from .models import Profile, PropertyForOffer, Image  # , PropertyImage


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'first_name', 'last_name', 'birthdate', 'phone_number', 'gender','about_me', 'image',
                  'occupation', 'smoker', 'diet', 'status', 'hospitality', 'kosher', 'expense_management']
        exclude = ['profile_status']
        widgets = {
            'birthdate': DateInput(attrs={'type': 'date'})
        }

        about_me = forms.CharField()
       

class OfferPropertyForm(forms.ModelForm):
    class Meta:
        model = PropertyForOffer
        fields = '__all__'
        exclude = ['user']

        description = forms.TextInput(attrs={'size': '10'})
        renovated = forms.BooleanField(label='Is the property renovated?')
        shelter_inside = forms.BooleanField(label='Is there a shelter inside?')
        shelter_nearby = forms.BooleanField(label='Is there a shelter nearby?')
        furnished = forms.BooleanField(label='Is the property furnished?')
        shared_livingroom = forms.BooleanField(
            label='Is there a shared living room?')
        rooms_number = forms.ChoiceField(choices=[(1.0, '1'),
                                                  (1.5, '1.5'),
                                                  (2.0, '2'),
                                                  (2.5, '2.5'),
                                                  (3.0, '3'),
                                                  (3.5, '3.5'),
                                                  (4.0, '4'),
                                                  (4.5, '4.5'),
                                                  (5.0, '5'),], label='Number of rooms:')
        roomates_number = forms.ChoiceField(choices=[(1, '1'),
                                                     (2, '2'),
                                                     (3, '3'),
                                                     (4, '4'),
                                                     (5, '5'),], label='Number of roomates:')
        showers_number = forms.ChoiceField(choices=[(1, '1'),
                                                    (2, '2'),
                                                    (3, '3'),
                                                    (4, '4'),
                                                    (5, '5'),], label='Number of showers:')
        toilets_number = forms.ChoiceField(choices=[(1, '1'),
                                                    (2, '2'),
                                                    (3, '3'),
                                                    (4, '4'),
                                                    (5, '5'),], label='Number of toilets:')


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']


class DisplayOfferPropertyForm(ImageForm, OfferPropertyForm):
    pass
