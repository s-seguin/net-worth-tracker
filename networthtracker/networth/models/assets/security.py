from django.db import models

from .asset import Asset
from ..ticker_symbol import TickerSymbol


class Security(Asset):
    special_notes = models.CharField(max_length=500)
    purchased_on = models.DateTimeField(null=True)
    settlement_date = models.DateTimeField()
    ticker_symbol = models.ForeignKey(TickerSymbol, null=True, on_delete=models.SET_NULL)
    # todo add account reference
    # todo add symbol references
