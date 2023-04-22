# Generated by Django 4.2 on 2023-04-18 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomit_app', '0011_alter_requirementsp_minshowers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirementsp',
            name='City',
            field=models.CharField(blank=True, default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='requirementsp',
            name='Country',
            field=models.CharField(blank=True, default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='requirementsp',
            name='MaxRent',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='requirementsp',
            name='MaxRoommates',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='requirementsp',
            name='MaxRooms',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='requirementsp',
            name='MinRent',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='requirementsp',
            name='MinRoommates',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='requirementsp',
            name='MinRooms',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='requirementsp',
            name='MinToilets',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='requirementsp',
            name='Neighborhood',
            field=models.CharField(blank=True, default='', max_length=25),
        ),
    ]
