from django.shortcuts import render, redirect
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from .models import UserProfile
from django.contrib.auth.decorators import user_passes_test


# List all books
def list_books(request):
    books = Book.objects.all()
    context = {'books':books}
    return render(request, 'relationship_app/list_books.html',context)

#Get library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

#create a new user
# class RegisterView(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'relationship_app/register.html'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = UserCreationForm()
        return render(request, 'relationship_app/register.html', {'form':form})

# def is_admin(user):
#     return UserProfile.objects.filter(user=user, role='Admin').exists()
# @user_passes_test(is_admin)
# def Admin(request):
#     # context = {'message':'Welcome Admin!'}
#     return render(request, 'relationship_app/admin_view.html')

# --- Access Check Helper Functions ---

# def is_admin(user):
#     if user.is_authenticated: 
#         try:
#             return user.userprofile.role == 'Admin'
#         except UserProfile.DoesNotExist:
#             return False
#     return False

# def is_librarian(user):
#     if user.is_authenticated: 
#         try:
#             return user.userprofile.role == 'Librarian'
#         except UserProfile.DoesNotExist:
#             return False
#     return False

# def is_member(user):
#     if user.is_authenticated: 
#         try:
#             return user.userprofile.role == 'Member'
#         except UserProfile.DoesNotExist:
#             return False
#     return False