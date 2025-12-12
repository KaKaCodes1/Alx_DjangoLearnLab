from django.db import models

# Create your models here.
class Book:
    title = models.CharField(max_length=400)
    author = models.CharField(max_length=100)
    published_date = models.DateField()