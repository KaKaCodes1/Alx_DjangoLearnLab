from django.urls import path
# from .views import list_books, LibraryDetailView, register
from . import views
from . import admin_view
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('library/<int:pk>/',views.LibraryDetailView.as_view(),name='library_detail'),
    path('books/', views.list_books, name='list_books'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin-view/', admin_view, name='admin_view')
]