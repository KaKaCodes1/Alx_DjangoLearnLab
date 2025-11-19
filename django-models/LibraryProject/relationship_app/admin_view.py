from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .models import UserProfile

def is_admin(user):
    """Return True if the user is authenticated and has role 'Admin'."""
    return user.is_authenticated and UserProfile.objects.filter(user=user, role='Admin').exists()

@user_passes_test(is_admin)
def admin_view(request):
    """View only accessible to Admin users."""
    return render(request, 'relationship_app/admin_view.html')
