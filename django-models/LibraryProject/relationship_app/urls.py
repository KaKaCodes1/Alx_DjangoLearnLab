from django.urls import path
from .views import books_in_library
from .views import book_list

urlpatterns = [
    path('library/<int:pk>/',books_in_library.as_view(),name='library_deatail'),
    path('books/', book_list, name='list_books'),
]