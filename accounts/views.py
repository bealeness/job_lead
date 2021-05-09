from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Job



@login_required
def profile(request):
    context = {
        'jobs': Job.objects.filter(fresh=True),
    }
    return render(request, 'accounts/profile.html', context)



@login_required
def applied(request):
    context = {
        'jobs': Job.objects.filter(applied=True)
    }
    return render(request, 'accounts/applied.html', context)


@login_required
def response(request):
    context = {
        'jobs': Job.objects.filter(response=True)
    }
    return render(request, 'accounts/response.html', context)


@login_required
def replied(request):
    context = {
        'jobs': Job.objects.filter(replied=True)
    }
    return render(request, 'accounts/replied.html', context)


@login_required
def interview(request):
    context = {
        'jobs': Job.objects.filter(interview=True)
    }
    return render(request, 'accounts/interview.html', context)


@login_required
def help(request):
    return render(request, 'accounts/help.html')


class JobDetailView(DetailView):
    model = Job


class JobCreateView(LoginRequiredMixin, CreateView):
    model = Job
    fields = ['company', 'role', 'contact', 'deadline', 'location', 'skills']
    
    def form_valid(self, form):
        form.instance.applicant = self.request.user
        return super().form_valid(form)


class JobUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Job
    fields = ['fresh', 'applied', 'response', 'replied', 'interview', 'applied_date', 'response_act', 'reply_act',
                'interview_date', 'interview_method', 'notes']

    def form_valid(self, form):
        form.instance.applicant = self.request.user
        return super().form_valid(form)

    def test_func(self):
        job = self.get_object()
        if self.request.user == job.applicant:
            return True
        return False


class JobDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Job
    success_url = 'accounts/profile/'

    def test_func(self):
        job = self.get_object()
        if self.request.user == job.applicant:
            return True
        return False
    





