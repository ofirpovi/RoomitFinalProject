# Generated by Django 4.1.7 on 2023-05-01 17:18

from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('roomit_app', '0023_remove_requirementsr_furnished_and_more'),
        ('users', '0005_alter_image_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisplayOfferReqsForm',
            fields=[
                ('requirementsp_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='roomit_app.requirementsp')),
            ],
            bases=('roomit_app.requirementsp',),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default='default_for_property.jpg', upload_to=users.models.property_image_upload_path),
        ),
        migrations.AlterField(
            model_name='image',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='users.propertyforoffer'),
        ),
    ]
