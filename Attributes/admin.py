from django.contrib.admin import site
from django.contrib.admin import ModelAdmin
from .models import Author, Contributor, Language, Category
from .forms import AuthorForm, ContributorForm, LanguageForm, CategoryForm

def deprecate_selected(modeladmin, request, queryset):
    queryset.update(deprecated=True)

def undeprecate_selected(modeladmin, request, queryset):
    queryset.update(deprecated=False)

class AuthorAdmin(ModelAdmin):
    form = AuthorForm
    list_display = ["full_name", "brief", "deprecated"]
    actions = [deprecate_selected, undeprecate_selected]

class ContributorAdmin(ModelAdmin):
    form = ContributorForm
    list_display = ["full_name", "deprecated"]
    actions = [deprecate_selected, undeprecate_selected]

class LanguageAdmin(ModelAdmin):
    form = LanguageForm
    list_display = ["name", "deprecated"]
    actions = [deprecate_selected, undeprecate_selected]

class CategoryAdmin(ModelAdmin):
    form = CategoryForm
    list_display = ["name", "deprecated"]
    actions = [deprecate_selected, undeprecate_selected]


site.register(Author, AuthorAdmin)
site.register(Contributor, ContributorAdmin)
site.register(Language, LanguageAdmin)
site.register(Category, CategoryAdmin)
