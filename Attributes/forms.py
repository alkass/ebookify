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
        "authors",
        "contributors",
        "language",
        "categories",
        "pdf_file", "epub_file", "mobi_file",
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
            raise ValidationError("Books can't contain less than zero pages.")
        return self.cleaned_data["num_pages"]
    def clean_file1(self):
        file_path = self.cleaned_data["file1"]
        file_name = str(file_path).split("/")[-1]
        file_name_tokens = file_name.split(".")
        if len(file_name_tokens) == 1:
            raise ValidationError("Couldn't detect ebook file format.")
        else:
            file_extention = file_name_tokens[-1].strip().lower()
            if file_extention != "pdf":
                raise ValidationError("Expected a PDF file.")
        return file_path
    def clean_file2(self):
        file_path = self.cleaned_data["file2"]
        file_name = str(file_path).split("/")[-1]
        file_name_tokens = file_name.split(".")
        if len(file_name_tokens) == 1:
            raise ValidationError("Couldn't detect ebook file format.")
        else:
            file_extention = file_name_tokens[-1].strip().lower()
            if file_extention != "epub":
                raise ValidationError("Expected an EPUB file.")
        return file_path
