from django.urls import path
# from .views import list_books, LibraryDetailView, register
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('library/<int:pk>/',views.LibraryDetailView.as_view(),name='library_detail'),
    path('books/', views.list_books, name='list_books'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin_view/', views.admin_view, name='admin_view'),
    path('librarian_view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
    path('books/<int:pk>/edit_book/', views.BookUpdateView.as_view(), name="edit_book"),
    path('books/<int:pk>/delete_book/', views.BookDeleteView.as_view(), name="delete_book"),
    path('books/add_book/', views.BookCreateView.as_view(), name='add_book'),

]