from django.db.models import Model
from django.db.models import CharField, TextField, IntegerField, BooleanField
from django.db.models import UUIDField
from django.db.models import ForeignKey
from django.db.models import FileField, ImageField
from django.db.models import DateTimeField
from django.conf import settings
from uuid import uuid4

class Author(Model):
    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
    full_name = CharField(max_length=256, unique=True, blank=False, null=True)
    brief = TextField(max_length=2000, blank=True, null=True)
    discoverable = BooleanField(help_text="If checked off, all books associated with this author will be discoverable to clients", default=True)
    def __unicode__(self):
        return self.full_name

class Contributor(Model):
    class Meta:
        verbose_name = "Contributor"
        verbose_name_plural = "Contributors"
    full_name = CharField(max_length=256, unique=True, blank=False, null=True)
    discoverable = BooleanField(help_text="If checked off, all books associated with this contributor will be discoverable to clients", default=True)
    def __unicode__(self):
        return self.full_name

class Language(Model):
    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"
    name = CharField(max_length=256, unique=True, blank=False, null=True)
    discoverable = BooleanField(help_text="If checked off, all books associated with this language will be discoverable to clients", default=True)
    def __unicode__(self):
        return self.name

class Category(Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    name = CharField(max_length=256, unique=True, blank=False, null=True)
    brief = TextField(max_length=2000, blank=True, null=True)
    discoverable = BooleanField(help_text="If checked off, all books associated with this category will be discoverable to clients", default=True)
    def __unicode__(self):
        return self.name

class Book(Model):
    """hello world"""
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
    title = CharField(max_length=256, blank=False, null=True)
    subtitle = CharField(max_length=256, blank=True, null=True)
    author1 = ForeignKey(Author, related_name="author1", null=True)
    author2 = ForeignKey(Author, related_name="author2", blank=True, null=True)
    author3 = ForeignKey(Author, related_name="author3", blank=True, null=True)
    author4 = ForeignKey(Author, related_name="author4", blank=True, null=True)
    author5 = ForeignKey(Author, related_name="author5", blank=True, null=True)
    contributor1 = ForeignKey(Contributor, related_name="contributor1", blank=True, null=True)
    contributor2 = ForeignKey(Contributor, related_name="contributor2", blank=True, null=True)
    contributor3 = ForeignKey(Contributor, related_name="contributor3", blank=True, null=True)
    language = ForeignKey(Language, blank=False, null=True)
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
    file1 = FileField(upload_to=settings.DATABASE_DIR)
    file2 = FileField(upload_to=settings.DATABASE_DIR, blank=True, null=True)
    file3 = FileField(upload_to=settings.DATABASE_DIR, blank=True, null=True)
    cover = ImageField(upload_to=settings.DATABASE_DIR, blank=True, null=True)
    description = TextField(max_length=2000, blank=True, null=True)
    num_pages = IntegerField("number of Pages", help_text="Leave at 0 if you don't want the number of pages to be shown", default=0)
    num_views = IntegerField("Views", default=0)
    num_downloads = IntegerField("Downloads", default=0)
    discoverable = BooleanField(help_text="Make this book discoverable to view and download", default=True)
    recommended = BooleanField(help_text="Recommend this book to your library visitors", default=True)
    identification = UUIDField("Book ID", default=uuid4, null=True)
    def __unicode__(self):
        return self.title

class BookFeedback(Model):
    class Meta:
        verbose_name = "Book Feedback"
        verbose_name_plural = "Book Feedbacks"
    book = ForeignKey(Book)
    feedback = TextField(max_length=1000, blank=False, null=True)
    feedback_date = DateTimeField(auto_now=False, auto_now_add=True)
    discoverable = BooleanField(help_text="Make this comment visible in the book view page", default=True)
    def __unicode__(self):
        return str(self.book)
