from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages

def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. You are now able to sign in.')
            return redirect('sign_in')
    else:
        form = RegistrationForm()
    return render(request, 'users/sign_up.html', { 'form': form })
