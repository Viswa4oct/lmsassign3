from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    dob = models.DateField()
    password = models.CharField(max_length=100)