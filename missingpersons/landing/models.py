from django.db import models

# Create your models here.
class Person(models.Model) :
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    missing_age = models.IntegerField()
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    gender = models.CharField(max_length=1)
    race = models.CharField(max_length=1)