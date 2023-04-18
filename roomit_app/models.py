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
    # Roommate_ID = models.OneToOneField(Roommates, on_delete=models.CASCADE)


class Requirements(models.Model):
    Requirement_ID = models.FloatField(primary_key=True)
    Roommates_ID = models.FloatField()
    Type = models.CharField(max_length=1, choices=[('P', 'P'), ('R', 'R')])
    Content = models.CharField(max_length=50)
    Category = models.CharField(max_length=10, choices=[('yn', 'yn'),
                                                        ('list', 'list'),
                                                        ('range', 'range')
                                                        ])
    Min_Value = models.IntegerField()
    Max_Value = models.IntegerField()
    Disqualifier = models.BooleanField()
    Weight = models.FloatField()
    Roommate = models.ForeignKey('Roommates', on_delete=models.CASCADE)


class Offers(models.Model):
    Offer_ID = models.FloatField(primary_key=True)
    Roommates_ID = models.FloatField()
    Content = JSONField()
    Roommate = models.ForeignKey('Roommates', on_delete=models.CASCADE)


class Scores(models.Model):
    Roommate1_ID = models.ForeignKey(
        Roommates, on_delete=models.CASCADE, related_name='roommate1_scores')
    Roommate2_ID = models.ForeignKey(
        Roommates, on_delete=models.CASCADE, related_name='roommate2_scores')
    Roommate1_score = models.FloatField()
    Roommate2_score = models.FloatField()
    Total_Score = models.FloatField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['Roommate1_ID', 'Roommate2_ID'], name='unique_scores'),
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

    def save(self, *args, **kwargs):
        super(RequirementsP, self).save(*args, **kwargs)

    # # Define the predefined list of choices
    # CHOICES_LIST = (
    #     ('choice1', 'Choice 1'),
    #     ('choice2', 'Choice 2'),
    #     ('choice3', 'Choice 3'),
    # )

    # # Define the field that holds the restricted list of strings
    # restricted_list = ArrayField(
    #     models.CharField(choices=CHOICES_LIST, max_length=10),
    #     default=list,
    # )

