import logging
import uuid

from django.db import models
from django.utils import timezone
from users.models import User

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
    description = models.CharField(null=True, max_length=500)
    market_value = models.FloatField()
    book_value = models.FloatField()
    book_value_is_average = models.BooleanField(default=True)
    type = models.CharField(max_length=8, null=True, choices=TYPE_CHOICES)
    quantity = models.FloatField(default=1)
    updated_on = models.DateTimeField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.updated_on = timezone.now()
        super(Asset, self).save(*args, **kwargs)

    def increase_book_value(self, amount):
        logging.debug("increasing book value")
        # todo account for quantity?
        self.book_value += amount
        self.save()

    def decrease_book_value(self, amount):
        logging.debug("decreasing book value")
        self.book_value -= amount
        self.save()

    def increase_quantity(self, amount):
        if amount is None:
            return

        logging.debug("increasing quantity")
        self.quantity += amount
        self.save()

    def decrease_quantity(self, amount):
        if amount is None:
            return

        logging.debug("increasing quantity")
        self.quantity -= amount
        self.save()
