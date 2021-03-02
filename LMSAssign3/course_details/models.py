from django.db import models

# Create your models here.

from django.db import models


class Course(models.Model):
    courseId = models.AutoField(primary_key=True, editable=False)
    courseName = models.CharField(max_length=100)
    courseDescription = models.CharField(max_length=100)
    lecturerName = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    startDate = models.DateField()
    seatsAvailable = models.CharField(max_length=100)
    credits = models.CharField(max_length=100)
    enrolled = models.CharField(max_length=100)
