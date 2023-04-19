from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from phonenumber_field.modelfields import PhoneNumberField
from djmoney.models.fields import MoneyField
import os
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

class PropertyForOffer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rent = MoneyField(max_digits=14, decimal_places=2, default_currency='Israeli New Shekel')
    square_meters = models.FloatField(blank= True)
    description = models.TextField()
    renovated = models.BooleanField(blank= True, default=False)
    shelter_inside = models.BooleanField(blank= True, default=False)
    shelter_nerbay = models.BooleanField(blank= True, default=False)
    furnished = models.BooleanField(blank= True, default=False)
    shared_livingroom = models.BooleanField(blank= True, default=False)
    
    rooms_number = models.FloatField(max_length=3, choices=[(1.0, '1'),
                                                            (1.5, '1.5'),
                                                            (2.0, '2'),
                                                            (2.5, '2.5'),
                                                            (3.0, '3'),
                                                            (3.5, '3.5'),
                                                            (4.0, '4'),
                                                            (4.5, '4.5'),
                                                            (5.0, '5'),], blank=False, default='1')
    roomates_number = models.IntegerField( choices=[(1, '1'),                                                                        
                                                    (2, '2'),
                                                    (3, '3'),
                                                    (4, '4'),
                                                    (5, '5'),], blank=False, default='1')
    showers_number = models.IntegerField(  choices=[(1, '1'),                                                                        
                                                    (2, '2'),
                                                    (3, '3'),
                                                    (4, '4'),
                                                    (5, '5'),], blank=False, default='1')
    toilets_number = models.IntegerField(  choices=[(1, '1'),                                                                        
                                                    (2, '2'),
                                                    (3, '3'),
                                                    (4, '4'),
                                                    (5, '5'),], blank=False, default='1')

    # nearby_choices = [('Supermarket','Supermarket'), ('Bakery','Bakery'), ('Synagogue','Synagogue'), ('Clinic','Clinic'), ('Bars','Bars'), ('Restaurants','Restaurants'), ('University','University'), ('School','School'),('Kindergarten','Kindergarten'), ('Shopping center','Shopping center')]
    # available_nearby = ArrayField(models.CharField(max_length=100, choices = nearby_choices, blank=True, null=True), blank=True, null= True)
    def __str__(self):
        return "{} Property".format(self.user.username)

    def save(self, *args, **kwargs):
        super(PropertyForOffer, self).save(*args, **kwargs)



def get_upload_path(instance, filename):
    # Get the name of the file without the extension
    name, ext = os.path.splitext(filename)
    # Use the name of the file as the directory name
    directory = name
    # Return the path to the file
    return f'property_pics/{directory}/{filename}'

class PropertyImage(models.Model):
    property = models.ForeignKey(PropertyForOffer, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to= 'property_pics')
    #default = models.BooleanField(default=False)

    def __str__(self):
        return "{} Property imges".format(self.user.username)

    def save(self, *args, **kwargs):
        super(PropertyImage, self).save(*args, **kwargs)

        img = Image.open(self.image.path)