from django.forms import ModelForm
from .models import Author, Contributor, Language, Category
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
