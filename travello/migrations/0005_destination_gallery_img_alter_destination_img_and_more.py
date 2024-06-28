# Generated by Django 5.0.6 on 2024-06-25 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0004_alter_destination_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='gallery_img',
            field=models.ImageField(default='static/images/pic01.jpg', upload_to='gallery/'),
        ),
        migrations.AlterField(
            model_name='destination',
            name='img',
            field=models.ImageField(upload_to='pics/'),
        ),
        migrations.AlterField(
            model_name='destination',
            name='orient',
            field=models.CharField(default='orient-left', max_length=20),
        ),
    ]