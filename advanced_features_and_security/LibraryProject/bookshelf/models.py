from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        object_string = f"{self.title} by {self.author} published in {self.publication_year}"
        return object_string
    
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True)
    profile_photo = models.ImageField(null=True, blank=True)

# class CustomUserManager(BaseUserManager):
#     def create_user(self, username, password):
#         user = self.model()
