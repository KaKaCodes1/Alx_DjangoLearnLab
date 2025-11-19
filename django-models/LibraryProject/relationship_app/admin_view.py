from django.contrib.auth.decorators import user_passes_test
# from django.contrib.auth.models import User
from django.shortcuts import render
from .models import UserProfile
from .views import is_admin

# def is_admin(user):
#     return UserProfile.objects.filter(user=user, role='Admin').exists()
# @user_passes_test(is_admin)
# def Admin(request):
#     # context = {'message':'Welcome Admin!'}
#     return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_admin)
def Admin(request):
    return render(request, 'relationship_app/admin_view.html', {})