import uuid

from django.db import models
from django.utils import timezone
from users.models import User

from ..account import Account
from ..mixins.validate_owns_object import ValidateOwnsObjectMixin


class Asset(ValidateOwnsObjectMixin, models.Model):
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
    account = models.ForeignKey(Account, null=True, on_delete=models.SET_NULL)
    description = models.CharField(null=True, max_length=500)
    market_value = models.FloatField()
    book_value = models.FloatField()
    book_value_is_average = models.BooleanField(default=True)
    type = models.CharField(max_length=8, null=True, choices=TYPE_CHOICES)
    updated_on = models.DateTimeField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.updated_on = timezone.now()
        self.validate_owns(model=Account, instance=self.account)
        super(Asset, self).save(*args, **kwargs)
