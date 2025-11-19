from django.shortcuts import render, redirect
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from .models import UserProfile
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required


# List all books
def list_books(request):
    books = Book.objects.all()
    context = {'books':books}
    return render(request, 'relationship_app/list_books.html',context)

#adding books
@method_decorator(permission_required('relationship_app.can_add_book'), name='dispatch')
class BookCreateView(CreateView):
    model = Book
    fields = ["title", "author"]
    success_url = reverse_lazy('list_books')

@method_decorator(permission_required('relationship_app.can_change_book'), name='dispatch')
class BookUpdateView(UpdateView):
    model = Book
    fields = ["title", "author"]
    success_url = reverse_lazy('list_books')

@method_decorator(permission_required('relationship_app.can_delete_book'), name='dispatch')
class BookDeleteView(DeleteView):
    model = Book
    # Django requires a template for confirmation before deletion
    template_name = 'relationship_app/book_confirm_delete.html'
    success_url =reverse_lazy('list_books')


#Get library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = UserCreationForm()
        return render(request, 'relationship_app/register.html', {'form':form})

#Checks whether the user is logged in(authenticated successfully) & has a userprofile
def is_admin(user):
    user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# @user_passes_test decorator checks the user’s role before granting access to each view
@user_passes_test(is_admin)
def admin_view(request):
    # context = {'message':'Welcome Admin!'}
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

