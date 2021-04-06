from django.db import models

from .asset import Asset


class Property(Asset):
    address = models.CharField(max_length=350)
    special_notes = models.CharField(max_length=500)
    purchased_on = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        self.type = Asset.PROPERTY
        super(Property, self).save(*args, **kwargs)
