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
    category1 = ForeignKey(Category, related_name="category1", null=True)
    category2 = ForeignKey(Category, related_name="category2", blank=True, null=True)
    category3 = ForeignKey(Category, related_name="category3", blank=True, null=True)
    category4 = ForeignKey(Category, related_name="category4", blank=True, null=True)
    category5 = ForeignKey(Category, related_name="category5", blank=True, null=True)
    category6 = ForeignKey(Category, related_name="category6", blank=True, null=True)
    category7 = ForeignKey(Category, related_name="category7", blank=True, null=True)
    category8 = ForeignKey(Category, related_name="category8", blank=True, null=True)
    category9 = ForeignKey(Category, related_name="category9", blank=True, null=True)
    category10 = ForeignKey(Category, related_name="category10", blank=True, null=True)
    description = TextField(max_length=2000, blank=True, null=True)
    deprecated = BooleanField(help_text="If checked off, this book will NOT be discoverable to clients", default=False)
    identification = UUIDField("Book ID", default=uuid4, null=True)

    def __unicode__(self):
        return self.title
