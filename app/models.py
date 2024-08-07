from django.db import models

from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    origin = models.CharField(max_length=64)
    residence = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    born = models.IntegerField()
    photo = models.ImageField(upload_to='media/', blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='people')

    def __str__(self):
        return self.name

