# Generated by Django 5.0.6 on 2024-06-27 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0006_gallery_remove_destination_gallery_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
