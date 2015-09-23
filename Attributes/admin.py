from django.contrib.admin import site
from django.contrib.admin import ModelAdmin
from .models import Author, Contributor, Language, Category, Book, BookFeedback
from .forms import AuthorForm, ContributorForm, LanguageForm, CategoryForm, BookForm, BookFeedbackForm

class AuthorAdmin(ModelAdmin):
    def make_selected_discoverable(modeladmin, request, queryset):
        queryset.update(discoverable=True)
        for author in queryset:
            Book.objects.filter(author1=author).update(discoverable=True)
            Book.objects.filter(author2=author).update(discoverable=True)
            Book.objects.filter(author3=author).update(discoverable=True)
            Book.objects.filter(author4=author).update(discoverable=True)
            Book.objects.filter(author5=author).update(discoverable=True)
    def make_selected_undiscoverable(modeladmin, request, queryset):
        queryset.update(discoverable=False)
        for author in queryset:
            Book.objects.filter(author1=author).update(discoverable=False)
            Book.objects.filter(author2=author).update(discoverable=False)
            Book.objects.filter(author3=author).update(discoverable=False)
            Book.objects.filter(author4=author).update(discoverable=False)
            Book.objects.filter(author5=author).update(discoverable=False)
    form = AuthorForm
    list_display = ["full_name", "discoverable"]
    actions = [make_selected_discoverable, make_selected_undiscoverable]

class ContributorAdmin(ModelAdmin):
    def make_selected_discoverable(modeladmin, request, queryset):
        queryset.update(discoverable=True)
        for contributor in queryset:
            Book.objects.filter(contributor1=contributor).update(discoverable=True)
            Book.objects.filter(contributor2=contributor).update(discoverable=True)
            Book.objects.filter(contributor3=contributor).update(discoverable=True)
            Book.objects.filter(contributor4=contributor).update(discoverable=True)
            Book.objects.filter(contributor5=contributor).update(discoverable=True)
    def make_selected_undiscoverable(modeladmin, request, queryset):
        queryset.update(discoverable=False)
        for contributor in queryset:
            Book.objects.filter(contributor1=contributor).update(discoverable=False)
            Book.objects.filter(contributor2=contributor).update(discoverable=False)
            Book.objects.filter(contributor3=contributor).update(discoverable=False)
            Book.objects.filter(contributor4=contributor).update(discoverable=False)
            Book.objects.filter(contributor5=contributor).update(discoverable=False)
    form = ContributorForm
    list_display = ["full_name", "discoverable"]
    actions = [make_selected_discoverable, make_selected_undiscoverable]

class LanguageAdmin(ModelAdmin):
    def make_selected_discoverable(modeladmin, request, queryset):
        queryset.update(discoverable=True)
        for language in queryset:
            Book.objects.filter(language=language).update(discoverable=True)
    def make_selected_undiscoverable(modeladmin, request, queryset):
        queryset.update(discoverable=False)
        for language in queryset:
            Book.objects.filter(language=language).update(discoverable=False)
    form = LanguageForm
    list_display = ["name", "discoverable"]
    actions = [make_selected_discoverable, make_selected_undiscoverable]

class CategoryAdmin(ModelAdmin):
    def make_selected_discoverable(modeladmin, request, queryset):
        queryset.update(discoverable=True)
        for category in queryset:
            Book.objects.filter(category1=category).update(discoverable=True)
            Book.objects.filter(category2=category).update(discoverable=True)
            Book.objects.filter(category3=category).update(discoverable=True)
            Book.objects.filter(category4=category).update(discoverable=True)
            Book.objects.filter(category5=category).update(discoverable=True)
    def make_selected_undiscoverable(modeladmin, request, queryset):
        queryset.update(discoverable=False)
        for category in queryset:
            Book.objects.filter(category1=category).update(discoverable=False)
            Book.objects.filter(category2=category).update(discoverable=False)
            Book.objects.filter(category3=category).update(discoverable=False)
            Book.objects.filter(category4=category).update(discoverable=False)
            Book.objects.filter(category5=category).update(discoverable=False)
    form = CategoryForm
    list_display = ["name", "discoverable"]
    actions = [make_selected_discoverable, make_selected_undiscoverable]

class BookAdmin(ModelAdmin):
    def make_selected_discoverable(modeladmin, request, queryset):
        queryset.update(discoverable=True)
    def make_selected_undiscoverable(modeladmin, request, queryset):
        queryset.update(discoverable=False)
    form = BookForm
    list_display = [
        "title",
        "author1", "author2",
        "language",
        "category1", "category2",
        "num_views",
        "num_downloads",
        "discoverable"
        ]
    readonly_fields = ["identification", "num_views", "num_downloads"]
    actions = [make_selected_discoverable, make_selected_undiscoverable]

class BookFeedbackAdmin(ModelAdmin):
    def make_selected_discoverable(modeladmin, request, queryset):
        queryset.update(discoverable=True)
    def make_selected_undiscoverable(modeladmin, request, queryset):
        queryset.update(discoverable=False)
    form = BookFeedbackForm
    list_display = ["book", "feedback_date", "feedback", "discoverable"]
    actions = [make_selected_discoverable, make_selected_undiscoverable]

site.register(Author, AuthorAdmin)
site.register(Contributor, ContributorAdmin)
site.register(Language, LanguageAdmin)
site.register(Category, CategoryAdmin)
site.register(Book, BookAdmin)
site.register(BookFeedback, BookFeedbackAdmin)
