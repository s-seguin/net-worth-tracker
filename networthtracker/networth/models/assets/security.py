from django.db import models

from ..ticker_symbol import TickerSymbol
from .asset import Asset


class Security(Asset):
    ticker_symbol = models.ForeignKey(
        TickerSymbol, null=True, on_delete=models.SET_NULL
    )
    exchange = models.CharField(max_length=50, null=True)
    price_per_unit = models.FloatField()

    def save(self, *args, **kwargs):
        self.type = Asset.SECURITY
        super(Security, self).save(*args, **kwargs)
