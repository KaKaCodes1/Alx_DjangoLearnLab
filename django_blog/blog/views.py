from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages #show success/error messages
from .forms import SignUpForm, UserUpdateForm

#Registration View
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account for {username} has been created. You can now log in.')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'blog/register.html', {'form':form})
    
#Profile View
@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'blog/profile.html', {'form':form})


def home(request):
    return render(request, 'blog/home.html')

