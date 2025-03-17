from django.db import models

# Create your models here.

from django.db import models

class course(models.Model):
    Department = models.CharField(max_length=150)
    CourseTitle = models.CharField(max_length=150)
    Instructor = models.CharField(max_length=150)
