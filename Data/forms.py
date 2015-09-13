from django.forms import ModelForm
from .models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author1", "contributor", "language", "category", "description", "deprecated"]
