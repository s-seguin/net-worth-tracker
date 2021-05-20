import logging
import uuid

from django.db import models
from django.utils import timezone
from networth.models.assets.asset import Asset
from networth.models.liabilities.liability import Liability
from networth.models.mixins.validate_owns_object import ValidateOwnsObjectMixin
from users.models import User


class Transaction(ValidateOwnsObjectMixin, models.Model):
    BUY = "buy"
    SELL = "sell"
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"
    ACTIONS = (
        (BUY, "Buy"),
        (SELL, "Sell"),
        (DEPOSIT, "Deposit"),
        (WITHDRAW, "Withdraw"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # todo look into this for these relationships
    #  https://docs.djangoproject.com/en/3.2/ref/contrib/contenttypes/#generic-relations
    asset = models.ForeignKey(Asset, null=True, on_delete=models.CASCADE)
    liability = models.ForeignKey(
        Liability, null=True, on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_date = models.DateTimeField()
    settlement_date = models.DateTimeField()
    action = models.CharField(max_length=8, choices=ACTIONS)
    description = models.CharField(max_length=300, null=True)
    quantity = models.FloatField(null=True)
    gross_amount = models.FloatField()
    net_amount = models.FloatField()  # gross_amount - commission
    commission = models.FloatField(null=True)
    updated_on = models.DateTimeField()

    def __str__(self):
        return self.description

    def save(self, *args, **kwargs):
        self.updated_on = timezone.now()
        self.validate_owns(model=Asset, instance=self.asset)
        self.validate_owns(model=Liability, instance=self.liability)

        self.net_amount = self.gross_amount - self.commission

        if self.asset is not None:
            self.update_asset()
        if self.liability is not None:
            self.update_liability()
        super(Transaction, self).save(*args, **kwargs)

    def update_asset(self):
        logging.debug("Update asset")
        if self.action == self.BUY or self.action == self.DEPOSIT:
            self.asset.increase_book_value(
                self.net_amount
            )  # todo improve accessor funcs here
            self.asset.increase_quantity(self.quantity)
        elif self.action == self.SELL or self.action == self.WITHDRAW:
            self.asset.decrease_book_value(self.net_amount)
            self.asset.decrease_quantity(self.quantity)

    def update_liability(self):
        pass
