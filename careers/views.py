from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import JobOpening, Application
from home.views import index
from .forms import ApplicationForm
from django.utils import timezone


# Create your views here.
"""Displays the current job openings"""
def current_jobs(request):
    current_jobs = JobOpening.objects.all()
    return render(request, 'careers.html', {'current_jobs':current_jobs})

"""
apply for the job
"""
def apply(request):
    if request.method=="POST":
        application_form = ApplicationForm(request.POST, request.FILES)

        if application_form.is_valid():
            application = application_form.save(commit=False)
            application.date = timezone.now()
            application.save()
            messages.error(request, "Thanks for applying!")
            return redirect(reverse(index))
    else:
        application_form = ApplicationForm()
    return render(request, 'application.html', {'application_form':application_form})
    