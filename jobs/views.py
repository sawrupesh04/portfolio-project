from django.shortcuts import render
from .models import Job

def home(request):
    job = Job.objects
    return render(request, 'jobs/home.html', {'jobs': job})
