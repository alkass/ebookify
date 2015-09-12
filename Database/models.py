from django.db.models import Model, CharField, TextField, BooleanField

class Author(Model):
    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
    full_name = CharField(max_length=256, unique=True, blank=False, null=True)
    brief = TextField(max_length=2000, blank=True, null=True)
    deprecated = BooleanField(default=False)

    def __unicode__(self):
        return self.full_name

class Contributor(Model):
    class Meta:
        verbose_name = "Contributor"
        verbose_name_plural = "Contributors"
    full_name = CharField(max_length=256, unique=True, blank=False, null=True)
    deprecated = BooleanField(default=False)

    def __unicode__(self):
        return self.full_name

class Language(Model):
    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"
    name = CharField(max_length=256, unique=True, blank=False, null=True)
    deprecated = BooleanField(default=False)

    def __unicode__(self):
        return self.name

class Category(Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    name = CharField(max_length=256, unique=True, blank=False, null=True)
    brief = TextField(max_length=2000, blank=True, null=True)
    deprecated = BooleanField(default=False)

    def __unicode__(self):
        return self.name
