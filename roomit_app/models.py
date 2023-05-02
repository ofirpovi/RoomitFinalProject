from django.db import models
from django.db.models import JSONField
from django.contrib.auth.models import User
from django.db import models
# from django.contrib.postgres.fields import ArrayField


class Roommates(models.Model):
    Roommate_ID = models.FloatField(primary_key=True)
    Status = models.CharField(max_length=50, choices=[(
        'StatusInsert', 'StatusInsert'), ('StatusEnter', 'StatusEnter')])
    # Picture = models.ImageField(null=True, blank=True)
    User_ID = models.ForeignKey(User, on_delete=models.CASCADE)


class StatusInsert(models.Model):
    Status_ID = models.FloatField(primary_key=True)
    Target = models.CharField(max_length=1, choices=[('P', 'P'), ('R', 'R')])
    Content = models.CharField(max_length=150)
    Roommate_ID = models.ForeignKey(Roommates, on_delete=models.CASCADE)


class StatusEnter(models.Model):
    Status_ID = models.FloatField(primary_key=True)
    Target = models.CharField(max_length=1, choices=[('P', 'P'), ('R', 'R')])
    Content = models.CharField(max_length=150)
    Roommate_ID = models.ForeignKey(Roommates, on_delete=models.CASCADE)


class Info(models.Model):
    User_ID = models.OneToOneField(
        User, primary_key=True, on_delete=models.CASCADE)
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    Birthdate = models.DateField(null=True, blank=True)
    Phone_Number = models.CharField(max_length=30)
    Gender = models.CharField(max_length=10, choices=[('F', 'Female'),
                                                      ('M', 'Male'),
                                                      ('N', 'Not Defined')
                                                      ])
    Occupation = models.CharField(max_length=30, choices=[('F', 'Full-time jobe'),
                                                          ('S', 'Student'),
                                                          ('P', 'Part-time job'),
                                                          ('D', "Doesn't matter"),
                                                          ], default='D')
    Smoker = models.CharField(max_length=15, choices=[('Yes', 'Yes'),
                                                      ('No', 'No'),
                                                      ('Occasionally',
                                                       'Occasionally'),
                                                      ('Socially', 'Socially')
                                                      ])
    Diet = models.CharField(max_length=15, choices=[('Carnivore', 'Carnivore'),
                                                    ('Pescetarian', 'Pescetarian'),
                                                    ('Vegan', 'Vegan'),
                                                    ('Vegetarian', 'Vegetarian'),
                                                    ('Raw Veganism',
                                                     'Raw Veganism')
                                                    ])
    Status = models.CharField(max_length=20, choices=[('Single', 'Single'),
                                                      ('Married', 'Married'),
                                                      ('In a relationship', 'In a relationship'),
                                                      ])

    Hospitality = models.BooleanField(max_length=15, default=True)
    Kosher = models.BooleanField(default=False)
    Expense_Management = models.CharField(max_length=15, default='P', choices=[('L', 'Love'),
                                                                               ('P', 'Prefer not')])
    # Roommate_ID = models.OneToOneField(Roommates, on_delete=models.CASCADE


class Scores(models.Model):
    Username_enter = models.ForeignKey(User, related_name='scores_entered', on_delete=models.CASCADE)
    Username_insert = models.ForeignKey(User, related_name='scores_inserted', on_delete=models.CASCADE)
    Enter_score = models.FloatField()
    Insert_score = models.FloatField()

    def save(self, *args, **kwargs):
        super(Scores, self).save(*args, **kwargs)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['Username_enter', 'Username_insert'], name='unique_scores')
        ]


class RequirementsP(models.Model):
    Requirement_ID = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Type = models.CharField(max_length=1, choices=[('P', 'Property'), ('R', 'Roommate')])
    Country = models.CharField(max_length=25, default='', blank=True)
    City = models.CharField(max_length=25, default='', blank=True)
    Neighborhood = models.CharField(max_length=25, default='', blank=True)
    MinRent = models.IntegerField(null=True, default=None, blank=True)
    MaxRent = models.IntegerField(null=True, default=None, blank=True)
    MinRooms = models.IntegerField(null=True, default=None, blank=True)
    MaxRooms = models.IntegerField(null=True, default=None, blank=True)
    MaxRoommates = models.IntegerField(null=True, default=None, blank=True)
    MinRoommates = models.IntegerField(null=True, default=None, blank=True)
    MinToilets = models.IntegerField(null=True, default=None, blank=True)
    MinShowers = models.IntegerField(null=True, default=None, blank=True)
    Weight = models.FloatField(null=True, default=100/5, blank=True)
    Renovated = models.BooleanField(blank= True, default=False)
    Shelter_Inside = models.BooleanField(blank= True, default=False)
    Shelter_Nearby = models.BooleanField(blank= True, default=False)
    Furnished = models.BooleanField(blank= True, default=False)
    Shared_Living_Room = models.BooleanField(blank= True, default=False)

    def save(self, *args, **kwargs):
        super(RequirementsP, self).save(*args, **kwargs)


class RequirementsR(models.Model):
    Requirement_ID = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Occupation = models.CharField(max_length=30,  blank=True, null=True, default=None, choices=[('F', 'Full-time job'),
                                                                      ('S', 'Student'),
                                                                       ('P', 'Part-time job'),
                                                                       ('D', "Doesn't matter"),
                                                                       ('empty',
                                                                        '---'),
                                                                       ])
    MinAge = models.IntegerField(null=True, default=None, blank=True)
    MaxAge = models.IntegerField(null=True, default=None, blank=True)
    Gender = models.CharField(max_length=10, null=True, default=None, blank=True, choices=[('F', 'Female'),
                                                                   ('M', 'Male'),
                                                                   ('N', 'Not Defined'),
                                                                   ])
    Smoker = models.CharField(max_length=15, null=True, default=None, blank=True, choices=[('Yes', 'Yes'),
                                                                  ('No', 'No'),
                                                                  ('Occasionally',
                                                                   'Occasionally'),
                                                                  ('Socially',
                                                                   'Socially'),
                                                                  ])
    Diet = models.CharField(max_length=15, null=True, default=None, blank=True, choices=[('Carnivore', 'Carnivore'),
                                                                ('Pescetarian',
                                                                 'Pescetarian'),
                                                                ('Vegan', 'Vegan'),
                                                                ('Vegetarian',
                                                                 'Vegetarian'),
                                                                ('Raw Veganism',
                                                                 'Raw Veganism'),
                                                                ])
    Kosher = models.CharField(max_length=15, null=True, default=None, blank=True, choices=[('Y', 'Yes'),
                                                                  ('N', 'No'),])
    Status = models.CharField(max_length=20, null=True, default=None, blank=True, choices=[('Single', 'Single'),
                                                                  ('Married',
                                                                   'Married'),
                                                                  ('In a relationship',
                                                                   'In a relationship'),
                                                                  ('D', "Doesn't matter"),])
    Weight = Weight = models.FloatField(null=True, default=100/7, blank=True)
    Expense_Management = models.CharField(max_length=15, default='P', choices=[('L', 'Love'),
                                                                           ('P', 'Prefer not')])


    def save(self, *args, **kwargs):
        super(RequirementsR, self).save(*args, **kwargs)


class Likes(models.Model):
    User_insert = models.ForeignKey(User, related_name='enter_likes_insert', on_delete=models.CASCADE)
    User_enter = models.ForeignKey(User, related_name='insert_likes_enter', on_delete=models.CASCADE)
    enter_likes_insert = models.BooleanField(blank= False, default=False)
    insert_likes_enter = models.BooleanField(blank= False, default=False)

    def save(self, *args, **kwargs):
        super(Likes, self).save(*args, **kwargs)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['User_insert', 'User_enter'], name='unique_likes')
        ]

