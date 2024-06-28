from django.db import models

# Create your models here.
class Register(models.Model):
    user = models.CharField(max_length=100)
    email = models.EmailField()
    pswd = models.IntegerField()
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)