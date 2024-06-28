from django.db import models

# Create your models here.
class Destination(models.Model):
    title = models.CharField(max_length=200)
    desc = models.CharField()
    img = models.ImageField(upload_to='pics/')
    orient = models.CharField(max_length=20,default="orient-left")

class Gallery(models.Model):
    gallery_img = models.ImageField(upload_to='gallery/',default='static/images/pic01.jpg')

class CustomTags(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"
