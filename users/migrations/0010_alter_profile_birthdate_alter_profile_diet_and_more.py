# Generated by Django 4.1.7 on 2023-04-18 11:18

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthdate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='diet',
            field=models.CharField(blank=True, choices=[('Carnivore', 'Carnivore'), ('Pescetarian', 'Pescetarian'), ('Vegan', 'Vegan'), ('Vegetarian', 'Vegetarian'), ('Raw Veganism', 'Raw Veganism')], max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='expense_management',
            field=models.CharField(blank=True, choices=[('Y', 'Prefer'), ('N', 'Prefer not')], max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('N', 'Not Defined')], max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='hospitality',
            field=models.CharField(blank=True, choices=[('L', 'Love'), ('N', 'Prefer not')], default='empty', max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='kosher',
            field=models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='occupation',
            field=models.CharField(blank=True, choices=[('F', 'Full-time jobe'), ('S', 'Student'), ('P', 'Part-time job'), ('D', "Doesn't matter"), ('empty', '---')], max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='profile',
            name='smoker',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('Occasionally', 'Occasionally'), ('Socially', 'Socially')], max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(blank=True, choices=[('Single', 'Single'), ('Married', 'Married'), ('In a relationship', 'In a relationship'), ('D', "Doesn't matter")], default='empty', max_length=20),
        ),
    ]