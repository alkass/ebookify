from django.forms import ModelForm, ValidationError
from re import sub

from .models import Author
class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ["full_name", "brief", "discoverable"]
    def clean_full_name(self):
        return sub("[ \t]+", " ", self.cleaned_data["full_name"]).strip().title()

from .models import Contributor
class ContributorForm(ModelForm):
    class Meta:
        model = Contributor
        fields = ["full_name", "discoverable"]
    def clean_full_name(self):
        return sub("[ \t]+", " ", self.cleaned_data["full_name"]).strip().title()

from .models import Language
class LanguageForm(ModelForm):
    class Meta:
        model = Language
        fields = ["name", "discoverable"]
    def clean_name(self):
        return sub("[ \t]+", " ", self.cleaned_data["name"]).strip().title()

from .models import Category
class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["name", "brief", "discoverable"]
    def clean_name(self):
        return sub("[ \t]+", " ", self.cleaned_data["name"]).strip().title()

from .models import Book
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
        "title", "subtitle",
        "author1", "author2", "author3", "author4", "author5",
        "contributor1", "contributor2", "contributor3",
        "language",
        "category1", "category2", "category3", "category4", "category5",
        "category6", "category7", "category8", "category9", "category10",
        "file1", "file2", "file3",
        "cover",
        "description",
        "num_pages",
        "discoverable",
        "recommended",
        ]
    def clean_title(self):
        return sub("[ \t]+", " ", self.cleaned_data["title"]).strip().title()
    def clean_subtitle(self):
        return sub("[ \t]+", " ", self.cleaned_data["subtitle"]).strip().title()
    def clean_num_pages(self):
        if self.cleaned_data["num_pages"] < 0:
            raise ValidationError("Books can't contain less than zero pages")
        return self.cleaned_data["num_pages"]

from .models import BookFeedback
class BookFeedbackForm(ModelForm):
    class Meta:
        model = BookFeedback
        fields = ["book", "feedback", "discoverable"]
