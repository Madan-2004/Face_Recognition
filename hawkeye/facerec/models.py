# models.py

from django.db import models

class ImageFile(models.Model):
    image = models.ImageField(upload_to='images/')

class Image(models.Model):
    images = models.ManyToManyField(ImageFile, related_name='related_images')
