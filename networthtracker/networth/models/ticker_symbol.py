from django.db import models


class TickerSymbol(models.Model):
    CURRENCY_CHOICES = [
        ('cad', 'CAD'),
        ('usd', 'USD'),
    ]
    TYPE_CHOICES = [
        ('equity', 'Equity Security'),
        ('debt', 'Debt Security'),
        ('hybrid', 'Hybrid Security'),
    ]
    EXCHANGE_CHOICES = [
        ('xtse', 'Toronto Stock Exchange'),
        ('xnys', 'New York Stock Exchange'),
        ('xnas', 'Nasdaq'),
        ('xlon', 'London Stock Exchange')
    ]

    id = models.UUIDField(primary_key=True)
    # todo look into this package: https://github.com/django-money/django-money
    price_per_unit = models.FloatField()
    price_updated_on = models.DateTimeField()
    symbol = models.CharField(max_length=20)
    exchange = models.CharField(max_length=4, choices=EXCHANGE_CHOICES)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=6, choices=TYPE_CHOICES)

    def __str__(self):
        return self.name
