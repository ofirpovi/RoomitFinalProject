from django import forms
from .models import RequirementsP, RequirementsR


class UpdateRequirementsRForm(forms.ModelForm):
    class Meta:
        model = RequirementsR
        fields = ['Occupation', 'MinAge', 'MaxAge', 'Gender', 'Smoker', 'Diet', 'Kosher', 'Status', 'Expense_Management', 'Hospitality']
        exclude = ['Requirement_ID', 'Roommates_ID']
        labels = {
                     'Occupation': 'Occupation',
                     'MinAge': 'Min Age',
                     'MaxAge': 'Max Age',
                     'Gender': 'Gender',
                     'Status': 'Relationship Status',
                     'Expense_Management': 'Shared Expenses',
                     'Hospitality': 'Hospitality'

        }


class UpdateRequirementsPForm(forms.ModelForm):
    class Meta:
        model = RequirementsP
        fields = ['Country', 'City', 'Neighborhood', 'MinRent', 'MaxRent', 'MinRooms', 'MaxRooms',
                  'MaxRoommates', 'MinRoommates', 'MinToilets', 'MinShowers', 'Renovated',
                  'Shelter_Inside', 'Shelter_Nearby', 'Furnished', 'Shared_Living_Room']
        exclude = ['Requirement_ID', 'Roommates_ID', 'Type']
        labels = {
            'Country': 'Country',
            'City': 'City',
            'Neighborhood': 'Neighborhood',
            'MinRent': 'Min Rent',
            'MaxRent': 'Max Rent',
            'MinRooms': 'Min Rooms',
            'MaxRooms': 'Max Rooms',
            'MaxRoommates': 'Max Roommates',
            'MinRoommates': 'Min Roommates',
            'MinToilets': 'Min Toilets',
            'MinShowers': 'Min Showers',
            'Renovated': 'Renovated',
            'Shelter_Inside': 'Shelter Inside',
            'Shelter_Nearby': 'Shelter Nearby',
            'Furnished': 'Furnished',
            'Shared_Living_Room': 'Shared Living Room'
        }
