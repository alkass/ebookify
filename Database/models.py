from django.db.models import Model, CharField, TextField, BooleanField, ForeignKey, UUIDField, FileField
from uuid import uuid4

class Author(Model):
    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
    full_name = CharField(max_length=128, unique=True, blank=False, null=True)
    brief = TextField(max_length=2000, blank=True, null=True)
    hidden = BooleanField(help_text="Hide all books associated with this author", default=False)
    def __unicode__(self):
        return self.full_name

class Contributor(Model):
    class Meta:
        verbose_name = "Contributor"
        verbose_name_plural = "Contributors"
    full_name = CharField(max_length=128, unique=True, blank=False, null=True)
    hidden = BooleanField(help_text="Hide all books associated with this contributor", default=False)
    def __unicode__(self):
        return self.full_name

class Category(Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    category_name = CharField(max_length=128, unique=True, blank=False, null=True)
    hidden = BooleanField(help_text="Hide all books associated with this category", default=False)
    def __unicode__(self):
        return self.category_name

class Language(Model):
    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"
    language_name = CharField(max_length=32, unique=True, blank=False, null=True)
    hidden = BooleanField(help_text="Hide all books associated with this language", default=False)
    def __unicode__(self):
        return self.language_name

class Book(Model):
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
    book_id = UUIDField(default=uuid4, blank=False, null=True)
    title = CharField(max_length=256, blank=False, null=True)
    author = ForeignKey(Author)
    category = ForeignKey(Category)
    hidden = BooleanField(help_text="Hide this book", default=False)

    def __unicode__(self):
        return self.title

class Uploads(Model):
    class Meta:
        verbose_name = "Upload"
        verbose_name_plural = "Uploads"
    book_id = UUIDField(default=uuid4, blank=False, null=True)
    title = CharField(max_length=256, blank=False, null=True)
    author = ForeignKey(Author)
    category = ForeignKey(Category)
    hidden = BooleanField(help_text="Hide this book", default=False)

    def __unicode__(self):
        return self.title

class Comment(Model):
    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
    book_title = ForeignKey(Book)
    comment = TextField(max_length=2000, blank=False, null=True)
    hidden = BooleanField(help_text="Hide all books associated with this author", default=False)
    def __unicode__(self):
        return self.book_title.__str__()
