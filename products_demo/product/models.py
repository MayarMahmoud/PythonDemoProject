from django.db import models
from django import forms
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class product(models.Model):
    Name=models.CharField(max_length=200)
    description = models.CharField(max_length=50)
    Image= models.ImageField(upload_to='static/product/images/', height_field=None, width_field=None, max_length=100)


class user(models.Model):
    Name=models.CharField(max_length=200)
    Email = models.EmailField(max_length=254,unique=True)
    Password = models.CharField(_('password'),max_length=32,)
