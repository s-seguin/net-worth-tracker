import datetime
import uuid

from django.db import models
from users.models import User


class Asset(models.Model):
    CASH = "cash"
    PROPERTY = "property"
    SECURITY = "security"
    TYPE_CHOICES = (
        (CASH, "Cash"),
        (PROPERTY, "Property"),
        (SECURITY, "Security"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(null=True, max_length=100)
    description = models.CharField(null=True, max_length=500)
    market_value = models.FloatField()
    book_value = models.FloatField()
    book_value_is_average = models.BooleanField(default=True)
    type = models.CharField(max_length=8, null=True, choices=TYPE_CHOICES)
    updated_on = models.DateTimeField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.updated_on = datetime.datetime.utcnow()
        super(Asset, self).save(*args, **kwargs)
