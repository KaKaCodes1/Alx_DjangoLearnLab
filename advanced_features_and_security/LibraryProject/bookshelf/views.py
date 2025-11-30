from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView


# Create your views here.
def hello_view(request):
    return HttpResponse("Hellooo World")
# Define the success URL for redirects (assuming list_books is the destination)
LIST_BOOKS_URL = reverse_lazy('list_books') 


# --- 1. View List (Secured by bookshelf.can_view) ---
# Requires permission to even see the list of books
@method_decorator(permission_required('bookshelf.can_view', raise_exception=True), name='dispatch')
class BookListView(ListView):
    model = Book
    template_name = 'bookshelf/book_list.html'
    context_object_name = 'books'


# --- 2. Create View (Secured by bookshelf.can_create) ---
@method_decorator(permission_required('bookshelf.can_create', raise_exception=True), name='dispatch')
class BookCreateView(CreateView):
    model = Book
    fields = ["title", "author", "publication_year"]
    template_name = 'bookshelf/book_form.html'
    success_url = LIST_BOOKS_URL


# --- 3. Update View (Secured by bookshelf.can_edit) ---
@method_decorator(permission_required('bookshelf.can_edit', raise_exception=True), name='dispatch')
class BookUpdateView(UpdateView):
    model = Book
    fields = ["title", "author", "publication_year"]
    template_name = 'bookshelf/book_form.html'
    success_url = LIST_BOOKS_URL


# --- 4. Delete View (Secured by bookshelf.can_delete) ---
@method_decorator(permission_required('bookshelf.can_delete', raise_exception=True), name='dispatch')
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'bookshelf/book_confirm_delete.html' 
    success_url = LIST_BOOKS_URL