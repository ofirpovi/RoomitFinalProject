# Generated by Django 4.2 on 2023-04-21 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomit_app', '0022_requirementsr_expense_management_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requirementsr',
            name='Furnished',
        ),
        migrations.RemoveField(
            model_name='requirementsr',
            name='Renovated',
        ),
        migrations.RemoveField(
            model_name='requirementsr',
            name='Shared_Living_Room',
        ),
        migrations.RemoveField(
            model_name='requirementsr',
            name='Shelter_Inside',
        ),
        migrations.RemoveField(
            model_name='requirementsr',
            name='Shelter_Nearby',
        ),
        migrations.AddField(
            model_name='requirementsp',
            name='Furnished',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='requirementsp',
            name='Renovated',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='requirementsp',
            name='Shared_Living_Room',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='requirementsp',
            name='Shelter_Inside',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='requirementsp',
            name='Shelter_Nearby',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
