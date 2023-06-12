from django import forms
from .models import RequirementsP, RequirementsR


class UpdateRequirementsRForm(forms.ModelForm):
    class Meta:
        model = RequirementsR
        fields = ['Occupation', 'MinAge', 'MaxAge', 'Gender', 'Smoker',
                  'Diet', 'Kosher', 'Status', 'Expense_Management']
        exclude = ['Requirement_ID', 'Roommates_ID']
        labels = {
            'Occupation': 'Occupation',
            'MinAge': 'Min Age',
            'MaxAge': 'Max Age',
            'Gender': 'Gender',
            'Status': 'Relationship Status',
            'Expense_Management': 'Shared Expenses',
        }


class UpdateRequirementsPForm(forms.ModelForm):
    class Meta:
        model = RequirementsP
        fields = ['MinRent', 'MaxRent', 'MinRooms', 'MaxRooms',
                  'MinRoommates', 'MaxRoommates', 'MinToilets', 'MinShowers', 'Renovated',
                  'ShelterInside', 'ShelterNearby', 'Furnished', 'SharedLivingRoom']
        exclude = ['Requirement_ID', 'Roommates_ID', 'Country', 'City', 'Neighborhood', 'Location']
        labels = {
            'MinRent': 'Min Rent',
            'MaxRent': 'Max Rent',
            'MinRooms': 'Min Rooms',
            'MaxRooms': 'Max Rooms',
            'MinRoommates': 'Min Roommates',
            'MaxRoommates': 'Max Roommates',
            'MinToilets': 'Min Toilets',
            'MinShowers': 'Min Showers',
            'Renovated': 'Renovated',
            'ShelterInside': 'Shelter Inside',
            'ShelterNearby': 'Shelter Nearby',
            'Furnished': 'Furnished',
            'SharedLivingRoom': 'Shared Living Room'
        }

