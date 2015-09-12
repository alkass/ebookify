from django.forms import ModelForm
from .models import Author, Contributor, Language, Category

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ["full_name", "brief", "deprecated"]

class ContributorForm(ModelForm):
    class Meta:
        model = Contributor
        fields = ["full_name", "deprecated"]

class LanguageForm(ModelForm):
    class Meta:
        model = Language
        fields = ["name", "deprecated"]

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["name", "brief", "deprecated"]
