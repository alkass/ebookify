from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Author, Contributor, Category, Language, Book, Uploads, Comment
from .forms import AuthorForm, ContributorForm, CategoryForm, LanguageForm, BookForm, UploadsForm, CommentForm

class AuthorAdmin(ModelAdmin):
    form = AuthorForm
    actions = ["hide", "unhide"]
    list_display = ["full_name", "brief", "hidden"]

    def hide(modeladmin, request, queryset):
        queryset.update(hidden=True)
    hide.short_description = "Hide selected Authors"

    def unhide(modeladmin, request, queryset):
        queryset.update(hidden=False)
    unhide.short_description = "Unhide selected Authors"

class ContributorAdmin(ModelAdmin):
    form = ContributorForm
    actions = ["hide", "unhide"]
    list_display = ["full_name", "hidden"]

    def hide(modeladmin, request, queryset):
        queryset.update(hidden=True)
    hide.short_description = "Hide selected Contributors"

    def unhide(modeladmin, request, queryset):
        queryset.update(hidden=False)
    unhide.short_description = "Unhide selected Contributors"

class CategoryAdmin(ModelAdmin):
    form = CategoryForm
    actions = ["hide", "unhide"]
    list_display = ["category_name", "hidden"]

    def hide(modeladmin, request, queryset):
        queryset.update(hidden=True)
    hide.short_description = "Hide selected Categories"

    def unhide(modeladmin, request, queryset):
        queryset.update(hidden=False)
    unhide.short_description = "Unhide selected Categories"

class LanguageAdmin(ModelAdmin):
    form = LanguageForm
    actions = ["hide", "unhide"]
    list_display = ["language_name", "hidden"]

    def hide(modeladmin, request, queryset):
        queryset.update(hidden=True)
    hide.short_description = "Hide selected Languages"

    def unhide(modeladmin, request, queryset):
        queryset.update(hidden=False)
    unhide.short_description = "Unhide selected Languages"

class BookAdmin(ModelAdmin):
    form = BookForm
    actions = ["hide", "unhide"]
    list_display = ["title", "author", "category", "hidden"]
    readonly_fields = ["book_id"]

    def hide(modeladmin, request, queryset):
        queryset.update(hidden=True)
    hide.short_description = "Hide selected Books"

    def unhide(modeladmin, request, queryset):
        queryset.update(hidden=False)
    unhide.short_description = "Unhide selected Books"

class UploadsAdmin(ModelAdmin):
    form = UploadsForm
    actions = ["hide", "unhide"]
    list_display = ["title", "author", "category", "hidden"]
    readonly_fields = ["book_id"]

    def hide(modeladmin, request, queryset):
        queryset.update(hidden=True)
    hide.short_description = "Hide selected Books"

    def unhide(modeladmin, request, queryset):
        queryset.update(hidden=False)
    unhide.short_description = "Unhide selected Books"

class CommentAdmin(ModelAdmin):
    form = CommentForm
    list_display = ["book_title", "comment", "hidden"]


admin.site.register(Author, AuthorAdmin)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Uploads, UploadsAdmin)
admin.site.register(Comment, CommentAdmin)
