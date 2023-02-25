from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Inventory(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    department = models.CharField(max_length=100)
    image = CloudinaryField('image',blank=True, null=True)
    details = models.CharField(max_length=250)
    location = models.CharField(max_length=20)
    
