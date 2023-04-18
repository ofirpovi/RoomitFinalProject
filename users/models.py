from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    profile_status = models.CharField(max_length=15, default=' ', help_text='What are you looking for', choices=[('StatusInsert', 'Roomate'),
                                                                                                                 ('StatusEnter', 'Appartment'),])
    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')
    birthdate = models.DateField(null=True, blank=False)
    phone_number = PhoneNumberField()
    gender = models.CharField(max_length=10, blank=False, choices=[('F', 'Female'),
                                                                   ('M', 'Male'),
                                                                   ('N', 'Not Defined'),
                                                                   ])
    occupation = models.CharField(max_length=30,  blank=True, choices=[('F', 'Full-time jobe'),
                                                                       ('S', 'Student'),
                                                                       ('P', 'Part-time job'),
                                                                       ('D', "Doesn't matter"),
                                                                       ('empty',
                                                                        '---'),
                                                                       ])
    smoker = models.CharField(max_length=15, blank=True, choices=[('Yes', 'Yes'),
                                                                  ('No', 'No'),
                                                                  ('Occasionally',
                                                                   'Occasionally'),
                                                                  ('Socially',
                                                                   'Socially'),
                                                                  ])
    diet = models.CharField(max_length=15, blank=True, choices=[('Carnivore', 'Carnivore'),
                                                                ('Pescetarian',
                                                                 'Pescetarian'),
                                                                ('Vegan', 'Vegan'),
                                                                ('Vegetarian',
                                                                 'Vegetarian'),
                                                                ('Raw Veganism',
                                                                 'Raw Veganism'),
                                                                ])
    status = models.CharField(max_length=20, blank=True, choices=[('Single', 'Single'),
                                                                  ('Married',
                                                                   'Married'),
                                                                  ('In a relationship',
                                                                   'In a relationship'),
                                                                  ('D', "Doesn't matter"),
                                                                  ], default='empty'
                              )
    hospitality = models.CharField(max_length=15, blank=True, default='empty', choices=[('L', 'Love'),
                                                                                        ('N', 'Prefer not'),])
    kosher = models.CharField(max_length=15, blank=True, choices=[('Y', 'Yes'),
                                                                  ('N', 'No'),])
    expense_management = models.CharField(max_length=15, blank=True, choices=[('Y', 'Prefer'),
                                                                              ('N', 'Prefer not'),])

    def __str__(self):
        return "{} Profile".format(self.user.username)

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
