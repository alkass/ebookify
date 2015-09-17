from django.db.models import Model, CharField, UUIDField
from uuid import uuid4

class BookRequest(Model):
    class Meta:
        verbose_name = "Book Request"
        verbose_name_plural = "Book Requests"
    title = CharField(max_length=256, blank=False, null=True)
    request_id = UUIDField(default=uuid4, null=True)
    def __unicode__(self):
        return self.title
