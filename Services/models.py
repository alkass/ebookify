from django.db.models import Model, CharField, UUIDField

class PlaceBookRequest(Model):
    title = CharField(max_length=256, blank=False, null=True)
    def __unicode__(self):
        return self.title

class CheckBookRequestStatus(Model):
    request_id = UUIDField(blank=False, null=True)
    def __unicode__(self):
        return str(self.request_id)
