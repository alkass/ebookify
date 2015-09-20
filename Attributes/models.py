from django.db.models import Model, CharField, TextField, BooleanField, UUIDField, ForeignKey
from uuid import uuid4

class Author(Model):
    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
    full_name = CharField(max_length=256, unique=True, blank=False, null=True)
    brief = TextField(max_length=2000, blank=True, null=True)
    deprecated = BooleanField(help_text="If checked off, all books associated with this author will NOT be discoverable to clients", default=False)
    def __unicode__(self):
        return self.full_name

class Contributor(Model):
    class Meta:
        verbose_name = "Contributor"
        verbose_name_plural = "Contributors"
    full_name = CharField(max_length=256, unique=True, blank=False, null=True)
    deprecated = BooleanField(help_text="If checked off, all books associated with this contributor will NOT be discoverable to clients", default=False)
    def __unicode__(self):
        return self.full_name

class Language(Model):
    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"
    name = CharField(max_length=256, unique=True, blank=False, null=True)
    deprecated = BooleanField(help_text="If checked off, all books associated with this language will NOT be discoverable to clients", default=False)
    def __unicode__(self):
        return self.name

class Category(Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    name = CharField(max_length=256, unique=True, blank=False, null=True)
    brief = TextField(max_length=2000, blank=True, null=True)
    deprecated = BooleanField(help_text="If checked off, all books associated with this category will NOT be discoverable to clients", default=False)
    def __unicode__(self):
        return self.name

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

class BookFeedback(Model):
    class Meta:
        verbose_name = "Book Feedback"
        verbose_name_plural = "Book Feedbacks"
    book = ForeignKey(Book)
    feedback = TextField(max_length=1000, blank=False, null=True)
    deprecated = BooleanField(help_text="If checked off, this comment will be hidden from the book list of reviews", default=False)
    def __unicode__(self):
        return str(self.book)
