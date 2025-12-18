from django.urls import path
from .views import (
    BookCreateView,
    BookDeleteView,
    BookDetailView,
    BookListView,
    BookUpdateView
    
)

urlpatterns = [
    path('books/',BookListView.as_view(), name='books-list'),
    path('books/<int:pk>/',BookDetailView.as_view(), name='books-detail'),
    path('books/<int:pk>/update/',BookUpdateView.as_view(), name='books-update'),
    path('books/create/',BookCreateView.as_view(), name='books-create'),
    path('books<int:pk>/delete/',BookDeleteView.as_view(), name='books-delete'),

]