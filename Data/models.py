from django.db.models import Model, CharField, ForeignKey, TextField, BooleanField
from Attributes.models import Author, Contributor, Language, Category

# Create your models here.
class Book(Model):
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
    title = CharField(max_length=256, blank=False, null=True)
    author1 = ForeignKey(Author)
    contributor = ForeignKey(Contributor, blank=True, null=True)
    language = ForeignKey(Language, blank=True, null=True)
    category = ForeignKey(Category, blank=True, null=True)
    description = TextField(max_length=2000, blank=True, null=True)
    deprecated = BooleanField(help_text="Hide this book", default=False)

    def __unicode__(self):
        return self.title
