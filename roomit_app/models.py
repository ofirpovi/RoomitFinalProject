from django.db import models
from django.db.models import JSONField


class Users(models.Model):
    ID = models.FloatField(primary_key=True)
    Email = models.CharField(max_length=100, unique=True)
    Password = models.CharField(max_length=30)


class Roommates(models.Model):
    Roommate_ID = models.FloatField(primary_key=True)
    Status = models.CharField(max_length=50, choices=[(
        'StatusInsert', 'StatusInsert'), ('StatusEnter', 'StatusEnter')])
    Picture = models.BinaryField(null=True, blank=True)
    User_ID = models.ForeignKey(Users, on_delete=models.CASCADE)


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
    Info_ID = models.FloatField(primary_key=True)
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    Birthday = models.DateField(null=True, blank=True)
    Phone_Number = models.CharField(max_length=30)
    Gender = models.CharField(max_length=10)
    Employment = models.CharField(max_length=30)
    Smoker = models.CharField(max_length=15, choices=[(
        'Yes', 'Yes'), ('No', 'No'), ('Occasionally', 'Occasionally'), ('Socially', 'Socially')])
    Diet = models.CharField(max_length=15, choices=[('Carnivore', 'Carnivore'), ('Pescetarian', 'Pescetarian'), (
        'Vegan', 'Vegan'), ('Vegetarian', 'Vegetarian'), ('Raw Veganism', 'Raw Veganism')])
    Status = models.CharField(max_length=20, choices=[('Single', 'Single'), (
        'Married', 'Married'), ('Widow', 'Widow'), ('In a relationship', 'In a relationship')])
    Hospitality = models.CharField(max_length=15)
    Expense_Management = models.CharField(max_length=15)
    Roommate_ID = models.OneToOneField(Roommates, on_delete=models.CASCADE)


class Requirements(models.Model):
    Requirement_ID = models.FloatField(primary_key=True)
    Roommates_ID = models.FloatField()
    Type = models.CharField(max_length=1, choices=[('P', 'P'), ('R', 'R')])
    Content = models.CharField(max_length=50)
    Category = models.CharField(max_length=10, choices=[(
        'yn', 'yn'), ('list', 'list'), ('range', 'range')])
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
