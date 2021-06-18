from django.db import models

from ..holding import Holding


class Asset(Holding):
    CASH = "cash"
    PROPERTY = "property"
    SECURITY = "security"
    TYPE_CHOICES = (
        (CASH, "Cash"),
        (PROPERTY, "Property"),
        (SECURITY, "Security"),
    )

    market_value = models.FloatField()
    book_value = models.FloatField()
    book_value_is_average = models.BooleanField(default=True)
    type = models.CharField(max_length=8, null=True, choices=TYPE_CHOICES)
    quantity = models.FloatField(default=1)
