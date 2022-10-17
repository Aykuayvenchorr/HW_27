from django.db import models


# Create your models here.

class Ad(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=300)
    address = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)


class Category(models.Model):
    name = models.CharField(max_length=200)
