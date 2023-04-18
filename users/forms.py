from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import DateInput
from .models import Profile


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
        fields = ['image', 'first_name', 'last_name', 'birthdate', 'phone_number', 'gender',
                  'occupation', 'smoker', 'diet', 'status', 'hospitality', 'kosher', 'expense_management']
        exclude = ['profile_status']
        widgets = {
        'birthdate': DateInput(attrs={'type': 'date'})
    }