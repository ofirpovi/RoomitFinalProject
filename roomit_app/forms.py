from django import forms
from . import models
from django.forms import TextInput, RadioSelect, CheckboxInput, DateInput


class InfoForm(forms.ModelForm):
    class Meta:
        model = models.Info
        fields = ['First_Name', 'Last_Name', 'Birthdate', 'Phone_Number', 'Gender', 'Occupation',
                  'Smoker', 'Diet', 'Status', 'Hospitality', 'Kosher', 'Expense_Management',]
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
# class CharField(forms.Field):
#     ...

#     def compress(self, value):
#         """
#         Return the cleaned data, or raise a validation error
#         """
#         if value is None:
#             return ''
#         return str(value).strip()

# class MultiValueField(forms.Field):
#     ...

#     def compress(self, value):
#         """
#         Return the cleaned data, or raise a validation error
#         """
#         if value is None:
#             return ''
#         return str(value).strip()



# class InfoForm(forms.Form):

#     first_name = forms.CharField(
#         label='First Name', help_text='Enter your first name')
#     last_name = forms.CharField(
#         label='Last Name', help_text='Enter your last name')

#     phone_number = forms.MultiValueField(
#         label='Phone Number',
#         widget=forms.MultiWidget(
#             widgets=[
#                 forms.TextInput(),
#                 forms.TextInput()
#             ]
#         ),
#         fields=(forms.CharField(), forms.CharField())
#     )
#     birthdate = forms.DateField(label='Date of birth', help_text='MM-DD-YYY')

#     GENDER_CHOICES = [
#         ('F', 'Female'),
#         ('M', 'Male'),
#         ('N', 'Not Defined'),
#     ]
#     gender = forms.ChoiceField(
#         label='Gender',
#         choices=GENDER_CHOICES,
#         widget=forms.RadioSelect,
#     )

#     OCCUPATION_CHOICES = [
#         ('F', 'Full-time jobe'),
#         ('S', 'Student'),
#         ('P', 'Part-time job'),
#         ('D', "Doesn't matter"),
#     ]
#     occupation = forms.ChoiceField(
#         label='Occupation',
#         choices=OCCUPATION_CHOICES,
#         widget=forms.RadioSelect,
#     )

#     smoking = forms.ChoiceField(
#         label='Smoking',
#         choices=[('Yes', 'Yes'),
#                  ('No', 'No'),
#                  ('Occasionally', 'Occasionally'),
#                  ('Socially', 'Socially')],
#         widget=forms.RadioSelect,
#         initial=False
#     )
#     DIET_CHOICES = [('Carnivore', 'Carnivore'),
#                     ('Pescetarian', 'Pescetarian'),
#                     ('Vegan', 'Vegan'),
#                     ('Vegetarian', 'Vegetarian'),
#                     ('Raw Veganism',
#                      'Raw Veganism')
#                     ]
#     diet = forms.ChoiceField(
#         label='Vegetarian/Veganism',
#         choices=DIET_CHOICES,
#         widget=forms.RadioSelect
#     )

#     kosher = forms.ChoiceField(
#         label='Kosher',
#         choices=[(True, 'Yes'), (False, 'No')],
#         widget=forms.RadioSelect,
#         initial=False
#     )

#     status = forms.ChoiceField(
#         label='status',
#         choices=[('Single', 'Single'),
#                  ('Married', 'Married'),
#                  ('In a relationship',
#                   'In a relationship')],
#         widget=forms.RadioSelect,
#         initial=False
#     )

#     HOSPITALITY_CHOICES = [
#         ('L', 'Love'),
#         ('P', 'Prefer not'),
#     ]
#     hospitality = forms.ChoiceField(
#         label='Vegetarian/Veganism',
#         choices=HOSPITALITY_CHOICES,
#         widget=forms.RadioSelect
#     )

#     BUY_CHOICES = [
#         ('L', 'Love'),
#         ('P', 'Prefer not'),
#     ]
#     shopping = forms.ChoiceField(
#         label='Buying groceries together',
#         choices=BUY_CHOICES,
#         widget=forms.RadioSelect
#     )
