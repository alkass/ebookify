from django.contrib.admin import site
from django.contrib.admin import ModelAdmin
from .models import Author, Contributor, Language, Category
from .forms import AuthorForm, ContributorForm, LanguageForm, CategoryForm

class AuthorAdmin(ModelAdmin):
    form = AuthorForm
    list_display = ["full_name", "deprecated"]

class ContributorAdmin(ModelAdmin):
    form = ContributorForm
    list_display = ["full_name", "deprecated"]

class LanguageAdmin(ModelAdmin):
    form = LanguageForm
    list_display = ["name", "deprecated"]

class CategoryAdmin(ModelAdmin):
    form = CategoryForm
    list_display = ["name", "deprecated"]


site.register(Author, AuthorAdmin)
site.register(Contributor, ContributorAdmin)
site.register(Language, LanguageAdmin)
site.register(Category, CategoryAdmin)
