from django.shortcuts import render
from .models import Author, Category
from Data.models import Book

def homepage(request):
    authors = Author.objects.all()
    categories = Category.objects.all()
    books = Book.objects.all()
    return render(request, "home.html", locals())
