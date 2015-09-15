from django.db.models import Model, CharField, ForeignKey, TextField, BooleanField, UUIDField
from Attributes.models import Author, Contributor, Language, Category
from uuid import uuid4

class Book(Model):
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
    title = CharField(max_length=256, blank=False, null=True)
    author1 = ForeignKey(Author, related_name="author1", null=True)
    author2 = ForeignKey(Author, related_name="author2", blank=True, null=True)
    author3 = ForeignKey(Author, related_name="author3", blank=True, null=True)
    author4 = ForeignKey(Author, related_name="author4", blank=True, null=True)
    author5 = ForeignKey(Author, related_name="author5", blank=True, null=True)
    contributor1 = ForeignKey(Contributor, related_name="contributor1", blank=True, null=True)
    contributor2 = ForeignKey(Contributor, related_name="contributor2", blank=True, null=True)
    contributor3 = ForeignKey(Contributor, related_name="contributor3", blank=True, null=True)
    language = ForeignKey(Language, blank=True, null=True)
    category = ForeignKey(Category, blank=True, null=True)
    description = TextField(max_length=2000, blank=True, null=True)
    deprecated = BooleanField(help_text="Hide this book", default=False)
    identification = UUIDField(default=uuid4, null=True)

    def __unicode__(self):
        return self.title
