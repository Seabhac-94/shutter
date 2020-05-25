from django.shortcuts import render

# Create your views here.

def index(request):
    """Renders index.html"""
    return render(request, 'index.html')