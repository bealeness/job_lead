from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Job



@login_required
def profile(request, self):
    context = {
        'jobs': Job.objects.filter(applicant=self.request.user),
        'user': User.objects.filter(user=self.request.user)
    }
    return render(request, 'accounts/profile.html', context)


class JobListView(ListView):
    model = Job
    template_name = 'accounts/profile.html'
    context_object_name = 'jobs'
    ordering = ['deadline']
    
    
class JobDetailView(DetailView):
    model = Job


class JobCreateView(LoginRequiredMixin, CreateView):
    model = Job
    fields = ['company', 'role', 'contact', 'deadline', 'location', 'skills']
    
    def form_valid(self, form):
        form.instance.applicant = self.request.user
        return super().form_valid(form)


class JobDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Job
    success_url = 'accounts/profile/'

    def test_func(self):
        job = self.get_object()
        if self.request.user == job.applicant:
            return True
        return False
    





