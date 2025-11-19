from django.contrib import admin
from .models import Book, Author, Librarian,Library

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Library)
admin.site.register(Librarian)