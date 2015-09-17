from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import BookRequest
from .forms import BookRequestForm

class BookRequestAdmin(ModelAdmin):
    form = BookRequestForm
    readonly_fields = ["request_id"]
    list_display = ["request_id", "title"]

admin.site.register(BookRequest, BookRequestAdmin)
