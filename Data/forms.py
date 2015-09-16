from django.forms import ModelForm
from .models import Book
from re import sub

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
        "title",
        "author1", "author2", "author3", "author4", "author5",
        "contributor1", "contributor2", "contributor3",
        "language",
        "category1", "category2", "category3", "category4", "category5",
        "category6", "category7", "category8", "category9", "category10",
        "description",
        "deprecated"
        ]
    def clean_title(self):
        return sub("[ \t]+", " ", self.cleaned_data["title"]).strip().title()
