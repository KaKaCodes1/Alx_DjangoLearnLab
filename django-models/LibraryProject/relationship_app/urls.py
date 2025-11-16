from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('library/<int:pk>/',LibraryDetailView.as_view(),name='library_deatail'),
    path('books/', list_books, name='list_books'),
]