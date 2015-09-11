from django.forms import ModelForm
from .models import Author, Contributor, Category, Language, Book, Uploads, Comment
from re import sub


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ["full_name", "brief", "hidden"]
    def clean_full_name(self):
        return sub("[ \t]+", " ", self.cleaned_data["full_name"]).strip().title()
    def clean_brief(self):
        return sub("[ \t]+", " ", self.cleaned_data["brief"]).strip().capitalize()

class ContributorForm(ModelForm):
    class Meta:
        model = Contributor
        fields = ["full_name", "hidden"]
    def clean_full_name(self):
        return sub("[ \t]+", " ", self.cleaned_data["full_name"]).strip().title()

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["category_name", "hidden"]
    def clean_category_name(self):
        return sub("[ \t]+", " ", self.cleaned_data["category_name"]).strip().title()

class LanguageForm(ModelForm):
    class Meta:
        model = Language
        fields = ["language_name", "hidden"]
    def clean_language_name(self):
        return sub("[ \t]+", " ", self.cleaned_data["language_name"]).strip().title()

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "category", "hidden"]
    def clean_title(self):
        return sub("[ \t]+", " ", self.cleaned_data["title"]).strip().title()

class UploadsForm(ModelForm):
    class Meta:
        model = Uploads
        fields = ["title", "author", "category", "hidden"]
    def clean_title(self):
        return sub("[ \t]+", " ", self.cleaned_data["title"]).strip().title()

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["book_title", "comment", "hidden"]
