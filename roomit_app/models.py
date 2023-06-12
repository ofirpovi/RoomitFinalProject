from django.contrib.auth.models import User
from django.db import models
# from django.contrib.postgres.fields import ArrayField
from djmoney.models.fields import MoneyField


class Scores(models.Model):
    Username_enter = models.ForeignKey(
        User, related_name='scores_entered', on_delete=models.CASCADE)
    Username_insert = models.ForeignKey(
        User, related_name='scores_inserted', on_delete=models.CASCADE)
    Enter_score = models.FloatField()
    Insert_score = models.FloatField()

    def save(self, *args, **kwargs):
        super(Scores, self).save(*args, **kwargs)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['Username_enter', 'Username_insert'], name='unique_scores')
        ]


class RequirementsP(models.Model):
    Requirement_ID = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Country = models.CharField(max_length=25, default='', blank=True)
    # City = models.CharField(max_length=25, default='', blank=True)
    # Neighborhood = models.CharField(max_length=25, default='', blank=True)
    # MinRent = MoneyField(max_digits=14, decimal_places=2, default_currency='ILS',null=True, default=None, blank=True)
    # MaxRent = MoneyField(max_digits=14, decimal_places=2, default_currency='ILS',null=True, default=None, blank=True)
    MinRent = models.IntegerField(null=True, default=None, blank=True)
    MaxRent = models.IntegerField(null=True, default=None, blank=True)
    MinRooms = models.IntegerField(null=True, default=None, blank=True)
    MaxRooms = models.IntegerField(null=True, default=None, blank=True)
    MaxRoommates = models.IntegerField(null=True, default=None, blank=True)
    MinRoommates = models.IntegerField(null=True, default=None, blank=True)
    MinToilets = models.IntegerField(null=True, default=None, blank=True)
    MinShowers = models.IntegerField(null=True, default=None, blank=True)
    Weight = models.FloatField(null=True, default=100, blank=True)
    Renovated = models.BooleanField(blank=False, default=False)
    ShelterInside = models.BooleanField(blank=False, default=False)
    ShelterNearby = models.BooleanField(blank=False, default=False)
    Furnished = models.BooleanField(blank=False, default=False)
    SharedLivingRoom = models.BooleanField(blank=False, default=False)
    Location = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        super(RequirementsP, self).save(*args, **kwargs)


class RequirementsR(models.Model):
    Requirement_ID = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Occupation = models.CharField(max_length=30, null=True, default='D', choices=[('F', 'Full-time job'),
                                                                                                ('S', 'Student'),
                                                                                                ('P', 'Part-time job'),
                                                                                                ('D', "Doesn't matter"),
                                                                                                ])
    MinAge = models.IntegerField(null=True, default=None, blank=True)
    MaxAge = models.IntegerField(null=True, default=None, blank=True)
    Gender = models.CharField(max_length=10, null=True, default='D', choices=[('F', 'Female'),
                                                                                           ('M', 'Male'),
                                                                                           ('T', 'Transgender'),
                                                                                           ('NB', 'Non-binary'),
                                                                                           ('GN', 'Gender neutral'),
                                                                                           ('D', "Doesn't matter"),
                                                                                           ])
    Smoker = models.CharField(max_length=15, null=True, default='D', choices=[('Yes', 'Yes'),
                                                                                           ('No','No'),
                                                                                           ('Occasionally','Occasionally'),
                                                                                           ('Socially','Socially'),
                                                                                           ("D", "Doesn't matter"),
                                                                                           ])
    Diet = models.CharField(max_length=15, null=True, default='D', choices=[('Carnivore', 'Carnivore'),
                                                                                         ('Pescetarian','Pescetarian'),
                                                                                         ('Vegan','Vegan'),
                                                                                         ('Vegetarian','Vegetarian'),
                                                                                         ('Raw Veganism','Raw Veganism'),
                                                                                         ('D', "Doesn't matter"),
                                                                                         ])
    Kosher = models.CharField(max_length=15, null=True, default='D', choices=[('Y', 'Yes'),
                                                                                           ('N', 'No'),
                                                                                            ('D', "Doesn't matter"),])
    Status = models.CharField(max_length=20, null=True, default='D', choices=[('Single', 'Single'),
                                                                                           ('Married',
                                                                                            'Married'),
                                                                                           ('In a relationship',
                                                                                            'In a relationship'),
                                                                                           ('D', "Doesn't matter"),])
    Weight = Weight = models.FloatField(null=True, default=100, blank=True)
    Expense_Management = models.CharField(max_length=15, default='D', choices=[('S', 'Shared'),
                                                                               ('I', 'Individual'),
                                                                                ('D', "Doesn't matter")])
    Hospitality = models.CharField(max_length=15, default='D', choices=[('L', 'Love'),
                                                                                        ('N', 'Prefer not'), ('D', "Doesn't matter")])

    def save(self, *args, **kwargs):
        super(RequirementsR, self).save(*args, **kwargs)


class Likes(models.Model):
    User_insert = models.ForeignKey(
        User, related_name='enter_likes_insert', on_delete=models.CASCADE)
    User_enter = models.ForeignKey(
        User, related_name='insert_likes_enter', on_delete=models.CASCADE)
    enter_likes_insert = models.BooleanField(blank=False, default=False)
    insert_likes_enter = models.BooleanField(blank=False, default=False)

    def save(self, *args, **kwargs):
        super(Likes, self).save(*args, **kwargs)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['User_insert', 'User_enter'], name='unique_likes')
        ]
