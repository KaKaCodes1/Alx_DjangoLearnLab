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
    


class CustomUserManager(BaseUserManager):
    """
    A custom user manager for the CustomUser model.
    It provides methods for creating standard users and superusers.
    """
    def create_user(self, username, email, password=None,**extra_fields):
        # 1. Ensure a username is provided (required for AbstractUser by default)
        if not username:
            raise ValueError('The username field must be set')
        if not email:
            raise ValueError('The email field must be set')
        
        # Normalize the email for consistency ie lowercase the domain name 
        email = self.normalize_email(email)

        #create a user instance
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # This method is specifically called when running commands like python manage.py createsuperuser
    def create_superuser(self, username, email, password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(username, email, password, **extra_fields)

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True)
    profile_photo = models.ImageField(null=True, blank=True)
    email = models.EmailField(unique=True)

    # Link the CustomUserManager to the model
    objects = CustomUserManager()

