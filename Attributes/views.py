from django.shortcuts import render
from .models import Author, Category

def home(request):
    data = {}
    data["authors"] = Author.objects.all()
    data["Categories"] = Category.objects.all()
    return render(request, "home.html", data)
