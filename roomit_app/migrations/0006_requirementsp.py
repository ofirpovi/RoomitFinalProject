# Generated by Django 4.2 on 2023-04-18 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomit_app', '0005_alter_info_user_id_alter_roommates_user_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequirementsP',
            fields=[
                ('Requirement_ID', models.FloatField(primary_key=True, serialize=False)),
                ('Roommates_ID', models.FloatField()),
                ('Type', models.CharField(choices=[('P', 'Property'), ('R', 'Roommate')], max_length=1)),
                ('Country', models.CharField(max_length=25)),
                ('Neighborhood', models.CharField(max_length=25)),
                ('MinRent', models.IntegerField()),
                ('MaxRent', models.IntegerField()),
                ('MinRooms', models.IntegerField()),
                ('MaxRooms', models.IntegerField()),
                ('MaxRoommates', models.IntegerField()),
                ('MinRoommates', models.IntegerField()),
                ('MinToilets', models.IntegerField()),
                ('MinShowers', models.IntegerField()),
            ],
        ),
    ]
