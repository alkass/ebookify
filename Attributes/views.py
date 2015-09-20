from django.shortcuts import render
from .models import Author, Category
from .models import Book

def homepage(request):
    authors = Author.objects.all().exclude(deprecated=True)
    categories = Category.objects.all().exclude(deprecated=True)
    books = Book.objects.all().exclude(deprecated=True)
    return render(request, "home.html", locals())
