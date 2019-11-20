from django.db import models

# Create your models here.
class Data(models.Model):
    uname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    pwd = models.CharField(max_length=100)
    img = models.ImageField(upload_to = 'pics')