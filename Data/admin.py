from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Book
from .forms import BookForm

class BookAdmin(ModelAdmin):
    form = BookForm
    list_display = ["title", "author1", "author2", "author3", "author4", "author5", "language", "category", "deprecated"]
    readonly_fields = ["identification"]

admin.site.register(Book, BookAdmin)
