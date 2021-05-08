from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import UpdateView

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


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    fields = ['username', 'email']

    def form_valid(self, form):
        form.instance.user.id = self.request.user
        return super().form_valid(form)

    def test_func(self):
        username = self.get_object()
        if self.request.user == username:
            return True
        return False

