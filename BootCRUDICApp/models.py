from django.db import models

# Create your models here.
class GymMemberModel(models.Model):
    name = models.CharField(max_length=200, default="")
    address = models.CharField(max_length=200, default="")
    age = models.IntegerField(default=0)
    imageURL = models.CharField(max_length=800, default="")
