from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Book
from .forms import BookForm

class BookAdmin(ModelAdmin):
    form = BookForm
    list_display = ["title", "author1", "language", "category", "deprecated"]

admin.site.register(Book, BookAdmin)
