from django.urls import path
from .views import list_books, LibraryDetailView, RegisterView
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('library/<int:pk>/',LibraryDetailView.as_view(),name='library_detail'),
    path('books/', list_books, name='list_books'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/',RegisterView.as_view(template_name='relationship_app/register.html')),
]