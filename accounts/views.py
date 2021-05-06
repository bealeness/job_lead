from django.shortcuts import render
from django.contrib.auth.decorators import login_required

jobs = [
    {
        'company': 'Google',
        'role': 'Python Developer',
        'contact': 'google@gmail.com',
        'deadline': 'June 2 2021'
    },
    {
        'company': 'Microsoft',
        'role': 'Python Developer',
        'contact': 'microsoft@hotmail.com',
        'deadline': 'June 12 2021'
    }
]

@login_required
def profile(request):
    context = {
        'jobs': jobs
    }
    return render(request, 'accounts/profile.html', context)
