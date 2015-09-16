from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Book
from .forms import BookForm

def deprecate_selected(modeladmin, request, queryset):
    queryset.update(deprecated=True)

def undeprecate_selected(modeladmin, request, queryset):
    queryset.update(deprecated=False)

class BookAdmin(ModelAdmin):
    form = BookForm
    list_display = ["title", "author1", "author2", "author5", "language", "category1", "category2", "deprecated"]
    readonly_fields = ["identification"]
    actions = [deprecate_selected, undeprecate_selected]

admin.site.register(Book, BookAdmin)
