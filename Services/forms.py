from django.forms import ModelForm
from .models import BookRequest

class BookRequestForm(ModelForm):
    class Meta:
        model = BookRequest
        fields = ["title"]
