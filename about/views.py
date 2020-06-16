from django.shortcuts import render

# Create your views here.

def about(request):
    """
    renders about.html
    """
    return render(request, 'about.html')