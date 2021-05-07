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
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('job-detail', kwargs={'pk': self.pk})
    
    
    
