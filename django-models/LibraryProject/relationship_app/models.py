from django.db import models

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

class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name='books')

class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

# #Create new user
# from django.contrib.auth.models import User
# user = User.objects.create_user(username="", password="")

# #Authenticate
# from django.contrib.auth import authenticate,login
# def
