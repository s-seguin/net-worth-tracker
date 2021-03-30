from django.db import models

from .asset import Asset


class Cash(Asset):
    CURRENCY_CHOICES = [("cad", "CAD"), ("usd", "USD")]
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)

    # todo add account reference

    def save(self, *args, **kwargs):
        self.type = Asset.CASH
        super(Cash, self).save(*args, **kwargs)
