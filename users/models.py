from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    profile_status = models.CharField(max_length=15, default=' ', help_text='What are you looking for', choices=[('StatusInsert', 'Roomate'),
                                                                            ('StatusEnter', 'Appartment'),])
    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')
    birthdate = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=30, default='')
    gender = models.CharField(max_length=10, default='empty', choices=[('F', 'Female'),
                                                                       ('M', 'Male'),
                                                                       ('N', 'Not Defined'),
                                                                       ('empty',
                                                                        '---'),
                                                                       ])
    occupation = models.CharField(max_length=30, choices=[('F', 'Full-time jobe'),
                                                          ('S', 'Student'),
                                                          ('P', 'Part-time job'),
                                                          ('D', "Doesn't matter"),
                                                          ('empty', '---'),
                                                          ], default='empty')
    smoker = models.CharField(max_length=15, choices=[('Yes', 'Yes'),
                                                      ('No', 'No'),
                                                      ('Occasionally',
                                                       'Occasionally'),
                                                      ('Socially', 'Socially'),
                                                      ('empty', '---'),
                                                      ], default='empty')
    diet = models.CharField(max_length=15, choices=[('Carnivore', 'Carnivore'),
                                                    ('Pescetarian', 'Pescetarian'),
                                                    ('Vegan', 'Vegan'),
                                                    ('Vegetarian', 'Vegetarian'),
                                                    ('Raw Veganism',
                                                     'Raw Veganism'),
                                                    ('empty', '---'),
                                                    ], default='empty')
    status = models.CharField(max_length=20, choices=[('Single', 'Single'),
                                                      ('Married', 'Married'),
                                                      ('In a relationship',
                                                       'In a relationship'),
                                                      ('D', "Doesn't matter"),
                                                      ('empty', '---'),
                                                      ], default='empty'
                              )
    hospitality = models.CharField(max_length=15, default='empty', choices=[('L', 'Love'),
                                                                            ('N', 'Prefer not'),
                                                                            ('empty', '---'),])
    kosher = models.CharField(max_length=15, default='empty', choices=[('Y', 'Yes'),
                                                                       ('N', 'No'),
                                                                       ('empty', '---'),])
    expense_management = models.CharField(max_length=15, default='empty', choices=[('Y', 'Prefer'),
                                                                                   ('N', 'Prefer not'), ('empty', '---'),])

    def __str__(self):
        return "{} Profile".format(self.user.username)

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
