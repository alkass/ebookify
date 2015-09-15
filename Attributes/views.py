from django.shortcuts import render
from .models import Author
from Data.models import Book

def home(request):
    data = {}
    data["books"] = Book.objects.all()
    return render(request, "home.html", data)
