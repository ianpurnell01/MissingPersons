from django.db import models
from datetime import datetime

# Create your models here.
class Person(models.Model) :
    date_at_missing = models.DateField(default=datetime.today, blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    missing_age = models.IntegerField()
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    gender = models.CharField(max_length=1)
    race = models.CharField(max_length=1)
    
    def __str__(self) :
    return(self.first_name + " " + self.last_name)
