from django.forms import ModelForm
from .models import Author, Contributor, Language, Category, Book, BookFeedback
from re import sub

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ["full_name", "brief", "deprecated"]
    def clean_full_name(self):
        return sub("[ \t]+", " ", self.cleaned_data["full_name"]).strip().title()

class ContributorForm(ModelForm):
    class Meta:
        model = Contributor
        fields = ["full_name", "deprecated"]
    def clean_full_name(self):
        return sub("[ \t]+", " ", self.cleaned_data["full_name"]).strip().title()

class LanguageForm(ModelForm):
    class Meta:
        model = Language
        fields = ["name", "deprecated"]
    def clean_name(self):
        return sub("[ \t]+", " ", self.cleaned_data["name"]).strip().title()

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["name", "brief", "deprecated"]
    def clean_name(self):
        return sub("[ \t]+", " ", self.cleaned_data["name"]).strip().title()

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

class BookFeedbackForm(ModelForm):
    class Meta:
        model = BookFeedback
        fields = ["book", "feedback", "deprecated"]
