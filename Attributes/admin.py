from django.contrib.admin import site
from django.contrib.admin import ModelAdmin
from .models import Author, Contributor, Language, Category, Book, BookFeedback
from .forms import AuthorForm, ContributorForm, LanguageForm, CategoryForm, BookForm, BookFeedbackForm

class AuthorAdmin(ModelAdmin):
    def deprecate_selected(modeladmin, request, queryset):
        queryset.update(deprecated=True)
        for author in queryset:
            Book.objects.filter(author1=author).update(deprecated=True)
            Book.objects.filter(author2=author).update(deprecated=True)
            Book.objects.filter(author3=author).update(deprecated=True)
            Book.objects.filter(author4=author).update(deprecated=True)
            Book.objects.filter(author5=author).update(deprecated=True)
    def undeprecate_selected(modeladmin, request, queryset):
        queryset.update(deprecated=False)
        for author in queryset:
            Book.objects.filter(author1=author).update(deprecated=False)
            Book.objects.filter(author2=author).update(deprecated=False)
            Book.objects.filter(author3=author).update(deprecated=False)
            Book.objects.filter(author4=author).update(deprecated=False)
            Book.objects.filter(author5=author).update(deprecated=False)
    form = AuthorForm
    list_display = ["full_name", "brief", "deprecated"]
    actions = [deprecate_selected, undeprecate_selected]

class ContributorAdmin(ModelAdmin):
    def deprecate_selected(modeladmin, request, queryset):
        queryset.update(deprecated=True)
        for contributor in queryset:
            Book.objects.filter(contributor1=contributor).update(deprecated=True)
            Book.objects.filter(contributor2=contributor).update(deprecated=True)
            Book.objects.filter(contributor3=contributor).update(deprecated=True)
            Book.objects.filter(contributor4=contributor).update(deprecated=True)
            Book.objects.filter(contributor5=contributor).update(deprecated=True)
    def undeprecate_selected(modeladmin, request, queryset):
        queryset.update(deprecated=False)
        for contributor in queryset:
            Book.objects.filter(contributor1=contributor).update(deprecated=False)
            Book.objects.filter(contributor2=contributor).update(deprecated=False)
            Book.objects.filter(contributor3=contributor).update(deprecated=False)
            Book.objects.filter(contributor4=contributor).update(deprecated=False)
            Book.objects.filter(contributor5=contributor).update(deprecated=False)
    form = ContributorForm
    list_display = ["full_name", "deprecated"]
    actions = [deprecate_selected, undeprecate_selected]

class LanguageAdmin(ModelAdmin):
    def deprecate_selected(modeladmin, request, queryset):
        queryset.update(deprecated=True)
        for language in queryset:
            Book.objects.filter(language=language).update(deprecated=True)
    def undeprecate_selected(modeladmin, request, queryset):
        queryset.update(deprecated=False)
        for language in queryset:
            Book.objects.filter(language=language).update(deprecated=False)
    form = LanguageForm
    list_display = ["name", "deprecated"]
    actions = [deprecate_selected, undeprecate_selected]

class CategoryAdmin(ModelAdmin):
    def deprecate_selected(modeladmin, request, queryset):
        queryset.update(deprecated=True)
        for category in queryset:
            Book.objects.filter(category1=category).update(deprecated=True)
            Book.objects.filter(category2=category).update(deprecated=True)
            Book.objects.filter(category3=category).update(deprecated=True)
            Book.objects.filter(category4=category).update(deprecated=True)
            Book.objects.filter(category5=category).update(deprecated=True)
    def undeprecate_selected(modeladmin, request, queryset):
        queryset.update(deprecated=False)
        for category in queryset:
            Book.objects.filter(category1=category).update(deprecated=False)
            Book.objects.filter(category2=category).update(deprecated=False)
            Book.objects.filter(category3=category).update(deprecated=False)
            Book.objects.filter(category4=category).update(deprecated=False)
            Book.objects.filter(category5=category).update(deprecated=False)
    form = CategoryForm
    list_display = ["name", "deprecated"]
    actions = [deprecate_selected, undeprecate_selected]

class BookAdmin(ModelAdmin):
    def deprecate_selected(modeladmin, request, queryset):
        queryset.update(deprecated=True)
    def undeprecate_selected(modeladmin, request, queryset):
        queryset.update(deprecated=False)
    form = BookForm
    list_display = ["title", "author1", "author2", "author5", "language", "category1", "category2", "deprecated"]
    readonly_fields = ["identification"]
    actions = [deprecate_selected, undeprecate_selected]

class BookFeedbackAdmin(ModelAdmin):
    def deprecate_selected(modeladmin, request, queryset):
        queryset.update(deprecated=True)
    def undeprecate_selected(modeladmin, request, queryset):
        queryset.update(deprecated=False)
    form = BookFeedbackForm
    list_display = ["book", "feedback", "deprecated"]
    actions = [deprecate_selected, undeprecate_selected]

site.register(Author, AuthorAdmin)
site.register(Contributor, ContributorAdmin)
site.register(Language, LanguageAdmin)
site.register(Category, CategoryAdmin)
site.register(Book, BookAdmin)
site.register(BookFeedback, BookFeedbackAdmin)
