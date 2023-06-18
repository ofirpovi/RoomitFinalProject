from django.contrib.auth.models import User
from django.db import models
# from djmoney.models.fields import MoneyField
from phonenumber_field.modelfields import PhoneNumberField
from functools import partial

def image_upload_path(instance, filename, flag):
    if flag == 0:
        return f"property_pics/{instance.property.user.username}/{filename}"
    else:
        return f"profile_pics/{instance.user.username}_profile_pic"
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(help_text='Choose your profile-picture', default='default_for_profile', upload_to= partial(image_upload_path, flag=1))
    profile_status = models.CharField(max_length=15, default=' ', help_text='What you are looking for', choices=[('StatusInsert', 'insert in'),                                                                                                   ('StatusEnter', 'enter in'),])
    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')
    birthdate = models.DateField(null=True, blank=False)
    phone_number = PhoneNumberField(
        help_text='Enter a valid phone number (e.g. +972521111111)')
    gender = models.CharField(max_length=10, blank=False, choices=[('F', 'Female'),
                                                                   ('M', 'Male'),
                                                                   ('T', 'Transgender'),
                                                                   ('NB', 'Non-binary'),
                                                                   ('GN', 'Gender neutral'),
                                                                   ('D', "Don't wish to answer"),
                                                                   ])
    occupation = models.CharField(max_length=30,  blank=True, choices=[('F', 'Full-time job'),
                                                                       ('S', 'Student'),
                                                                       ('P', 'Part-time job'),
                                                                       ('D', "Don't wish to answer"),
                                                                       ])
    smoker = models.CharField(max_length=15, blank=True, choices=[('Yes', 'Yes'),
                                                                  ('No', 'No'),
                                                                  ('Occasionally',
                                                                   'Occasionally'),
                                                                  ('Socially',
                                                                   'Socially'),
                                                                  ('D', "Don't wish to answer"),
                                                                  ])
    diet = models.CharField(max_length=15, blank=True, choices=[('Carnivore', 'Carnivore'),
                                                                ('Pescetarian',
                                                                 'Pescetarian'),
                                                                ('Vegan', 'Vegan'),
                                                                ('Vegetarian',
                                                                 'Vegetarian'),
                                                                ('Raw Veganism',
                                                                 'Raw Veganism'),
                                                                ('D', "Don't wish to answer"),
                                                                ])
    status = models.CharField(max_length=20, blank=True, choices=[('Single', 'Single'),
                                                                  ('Married',
                                                                   'Married'),
                                                                  ('In a relationship',
                                                                   'In a relationship'),
                                                                  ('D', "Don't wish to answer"),
                                                                  ])

    hospitality = models.CharField(max_length=15, blank=True, default='', choices=[('L', 'Love'),
                                                                                        ('N', 'Prefer not'),
                                                                                   ('D', "Don't wish to answer"),])
    kosher = models.CharField(max_length=15, blank=True, choices=[('Y', 'Yes'),
                                                                  ('N', 'No'),
                                                                  ('D', "Doesn't matter"),])
    expense_management = models.CharField(max_length=15, blank=True, choices=[('S', 'Shared'),
                                                                               ('I', 'Individual'),
                                                                                ('D', "Doesn't matter"),])
    about_me = models.TextField(max_length=80, default='', blank= True)

    def __str__(self):
        return "{} Profile".format(self.user.username)

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)


class PropertyForOffer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='property')
    rent = models.IntegerField(blank=True, default=None, null=True)
    square_meters = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, default='')
    renovated = models.BooleanField(blank=True, default=False)
    shelter_inside = models.BooleanField(blank=True, default=False)
    shelter_nearby = models.BooleanField(blank=True, default=False)
    furnished = models.BooleanField(blank=True, default=False)
    shared_livingroom = models.BooleanField(blank=True, default=False)
    rooms_number = models.FloatField(max_length=3, blank=False, default=None)
    roomates_number = models.IntegerField(blank=False, default=None)
    showers_number = models.IntegerField(blank=False, default=None)
    toilets_number = models.IntegerField(blank=False, default=None)
    Location = models.TextField(blank=True)
    # nearby_choices = [('Supermarket','Supermarket'), ('Bakery','Bakery'), ('Synagogue','Synagogue'), ('Clinic','Clinic'), ('Bars','Bars'), ('Restaurants','Restaurants'), ('University','University'), ('School','School'),('Kindergarten','Kindergarten'), ('Shopping center','Shopping center')]
    # available_nearby = ArrayField(models.CharField(max_length=100, choices = nearby_choices, blank=True, null=True), blank=True, null= True)
    def __str__(self):
        return "{} Property".format(self.user.username)

    def save(self, *args, **kwargs):
        super(PropertyForOffer, self).save(*args, **kwargs)


class Image(models.Model):
    property = models.ForeignKey(PropertyForOffer, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(default='default_for_property', upload_to= partial(image_upload_path, flag=0))

    def save(self, *args, **kwargs):
        super(Image, self).save(*args, **kwargs)
