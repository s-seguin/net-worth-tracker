from django.db import models

from ..ticker_symbol import TickerSymbol
from .asset import Asset


class Security(Asset):
    special_notes = models.CharField(max_length=500)
    purchased_on = models.DateTimeField(null=True)
    settlement_date = models.DateTimeField()
    ticker_symbol = models.ForeignKey(
        TickerSymbol, null=True, on_delete=models.SET_NULL
    )

    def save(self, *args, **kwargs):
        self.type = Asset.SECURITY
        super(Security, self).save(*args, **kwargs)
