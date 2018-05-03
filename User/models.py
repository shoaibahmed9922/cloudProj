# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField
import cloudinary.uploader
import cloudinary.api
# Create your models here.
class User(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,blank=True)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=20, unique=True)
    image = models.ImageField(upload_to='Pictures')

    def __str__(self):
        return  str(self.id) +'     ' + self.name +'       '+ self.email
