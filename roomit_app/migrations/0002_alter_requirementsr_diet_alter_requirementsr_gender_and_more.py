# Generated by Django 4.1.7 on 2023-05-23 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomit_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirementsr',
            name='Diet',
            field=models.CharField(blank=True, choices=[('Carnivore', 'Carnivore'), ('Pescetarian', 'Pescetarian'), ('Vegan', 'Vegan'), ('Vegetarian', 'Vegetarian'), ('Raw Veganism', 'Raw Veganism'), ('D', "Doesn't matter")], default=None, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='requirementsr',
            name='Gender',
            field=models.CharField(blank=True, choices=[('F', 'Female'), ('M', 'Male'), ('N', 'Not Defined'), ('D', "Doesn't matter")], default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='requirementsr',
            name='Occupation',
            field=models.CharField(blank=True, choices=[('F', 'Full-time job'), ('S', 'Student'), ('P', 'Part-time job'), ('D', "Doesn't matter")], default=None, max_length=30, null=True),
        ),
    ]
