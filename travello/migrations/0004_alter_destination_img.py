# Generated by Django 5.0.6 on 2024-06-25 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0003_destination_orient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='img',
            field=models.ImageField(upload_to='media/'),
        ),
    ]