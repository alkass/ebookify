from django.db.models import Model
from django.db.models import CharField, TextField, IntegerField, BooleanField
from django.db.models import UUIDField
from django.db.models import ForeignKey
from django.db.models import FileField, ImageField
from django.db.models import DateTimeField
from django.db.models import ManyToManyField
from django.conf import settings
from uuid import uuid4
from os.path import join

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
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
    identification = UUIDField("Book ID", default=uuid4, null=True)
    title = CharField(max_length=256, blank=False, null=True)
    subtitle = CharField(max_length=256, blank=True, null=True)
    authors = ManyToManyField(Author)
    contributors = ManyToManyField(Contributor)
    language = ForeignKey(Language, blank=False, null=True)
    categories = ManyToManyField(Category)
    pdf_file = FileField("PDF File", upload_to=join(settings.DATABASE_BOOK_DIR), blank=True, null=True)
    epub_file = FileField("EPUB File", upload_to=join(settings.DATABASE_BOOK_DIR), blank=True, null=True)
    mobi_file = FileField("MOBI File", upload_to=join(settings.DATABASE_BOOK_DIR), blank=True, null=True)
    cover = ImageField(upload_to=join(settings.DATABASE_COVER_DIR), blank=True, null=True)
    description = TextField(max_length=5000, blank=True, null=True)
    num_pages = IntegerField("number of Pages", help_text="Leave at 0 if you don't want the number of pages to be shown", default=0)
    num_views = IntegerField("Views", default=0)
    num_downloads = IntegerField("Downloads", default=0)
    discoverable = BooleanField(help_text="Make this book discoverable to view and download", default=True)
    recommended = BooleanField(help_text="Recommend this book to your library visitors", default=False)
    def pdf(self):
        if len(str(self.pdf_file)) > 0:
            return "Yes"
        else:
            return "No"
    def epub(self):
        if len(str(self.epub_file)) > 0:
            return "Yes"
        else:
            return "No"
    def mobi(self):
        if len(str(self.mobi_file)) > 0:
            return "Yes"
        else:
            return "No"
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
        return str(self.book.identification)
