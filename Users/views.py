from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for {username}! You can now Log In with this account!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'Users/register.html', {'form': form})

@login_required
def profile(request):
    if request == 'POST':
        uForm = UserUpdateForm(request.POST, instance=request.user)
        pForm = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if uForm.is_valid() and pForm.is_valid():
            uForm.save()
            pForm.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        uForm = UserUpdateForm(instance=request.user)
        pForm = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'uForm' : uForm,
        'pForm' : pForm
    }
    return render(request, 'Users/profile.html', context)