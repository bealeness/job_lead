from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Job(models.Model):
    company = models.CharField(max_length=50)
    role = models.CharField(max_length=30)
    contact = models.CharField(max_length=30)
    deadline = models.DateField(auto_now=False)
    location = models.CharField(max_length=30)
    skills = models.TextField()
    fresh = models.BooleanField(default=True)
    applied = models.BooleanField(default=False)
    response = models.BooleanField(default=False)
    replied = models.BooleanField(default=False)
    interview = models.BooleanField(default=False)
    applied_date = models.DateField(auto_now=False, null=True)
    response_act = models.CharField(max_length=100, null=True)
    reply_act = models.CharField(max_length=100, null=True)
    interview_date = models.DateField(auto_now=False, null=True)
    interview_method = models.CharField(max_length=30, null=True)
    notes = models.TextField(null=True)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('job-detail', kwargs={'pk': self.pk})
    
    
    
