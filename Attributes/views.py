from django.shortcuts import render

from .models import Author

def home(request):
    return render(request, "home.html", {})
