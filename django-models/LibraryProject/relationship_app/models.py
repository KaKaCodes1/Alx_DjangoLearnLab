from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author,on_delete=models.PROTECT)

    def __str__(self):
        book_title = f"{self.title} by {self.author}"
        return book_title

    class Meta:
        permissions = [
            # ('codename', 'human-readable description')
            ('can_add_book', 'Permission to add a book'), 
            ('can_change_book', 'Permission to change a book'), 
            ('can_delete_book', 'Permission to delete a book'),
        ]

class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name='books')

class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

class UserProfile(models.Model):
    roles_choices = [
        ('Admin','Admin'), 
        ('Librarian','Librarian'), 
        ('Member','Member'),
    ] 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=roles_choices, default='Member')

#Use Django signals to automatically create a UserProfile when a new user is registered.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


