from django.urls import path
from .views import hello_view
from . import views

urlpatterns = [
    path('hello/',hello_view),
    # List View (READ/VIEW)
    path('books/', views.BookListView.as_view(), name='list_books'),

    # Create View (ADD)
    path('books/add/', views.BookCreateView.as_view(), name='book_add'),
    
    # Update View (EDIT)
    path('books/<int:pk>/change/', views.BookUpdateView.as_view(), name='book_change'),
    
    # Delete View (DELETE)
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),

    path('search/', views.book_search_secure, name='book_search'),
]