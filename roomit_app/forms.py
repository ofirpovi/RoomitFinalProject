from django import forms
from .models import Info, RequirementsP, RequirementsR
from django.forms import TextInput, RadioSelect, CheckboxInput, DateInput


class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['First_Name', 'Last_Name', 'Birthdate', 'Phone_Number', 'Gender', 'Occupation',
                  'Smoker', 'Diet', 'Status', 'Hospitality', 'Kosher', 'Expense_Management']
        widgets = {'First_Name': TextInput(),
                   'Last_Name': TextInput(),
                   'Birthdate': DateInput(),
                   'Phone_Number': TextInput(),
                   'Gender': RadioSelect(choices=[('F', 'Female'),
                                                  ('M', 'Male'),
                                                  ('N', 'Not Defined')
                                                  ]),
                   'Occupation': RadioSelect(choices=[('F', 'Full-time jobe'),
                                                      ('S', 'Student'),
                                                      ('P', 'Part-time job'),
                                                      ('D', "Doesn't matter")]),
                   'Smoker': RadioSelect(choices=[('Yes', 'Yes'),
                                                  ('No', 'No'),
                                                  ('Occasionally',
                                                  'Occasionally'),
                                                  ('Socially', 'Socially')
                                                  ]),
                   'Diet': RadioSelect(choices=[('Carnivore', 'Carnivore'),
                                                ('Pescetarian', 'Pescetarian'),
                                                ('Vegan', 'Vegan'),
                                                ('Vegetarian', 'Vegetarian'),
                                                ('Raw Veganism',
                                                'Raw Veganism')
                                                ]),
                   'Status': RadioSelect(choices=[('Single', 'Single'),
                                                  ('Married', 'Married'),
                                                  ('In a relationship',
                                                  'In a relationship')
                                                  ]),
                   'Hospitality': CheckboxInput(),
                   'Kosher': CheckboxInput(),
                   'Expense_Management': RadioSelect(choices=[('L', 'Love'),
                                                              ('P', 'Prefer not')]), }


class UpdateRequirementsRForm(forms.ModelForm):
    class Meta:
        model = RequirementsR
        fields = ['Occupation', 'MinAge', 'MaxAge', 'Gender', 'Smoker', 'Diet', 'Kosher', 'Status', 'Expense_Management']
        exclude = ['Requirement_ID', 'Roommates_ID']
        labels = {
                     'Occupation': 'Occupation',
                     'MinAge': 'Min Age',
                     'MaxAge': 'Max Age',
                     'Gender': 'Gender',
                     'Status': 'Relationship Status',
                     'Expense_Management': 'Shared Expenses'

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
            'Shelter_Nearby': 'Shelter_Nearby',
            'Furnished': 'Furnished',
            'Shared_Living_Room': 'Shared Living Room'
        }
