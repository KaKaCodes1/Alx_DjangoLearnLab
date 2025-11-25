from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.
def hello_view(request):
    return HttpResponse("Hellooo World")
def book_list(request):
    books = Book.objects.all()
    context = {'book_list':books}
    return render(request, 'books/book_list.html', context)