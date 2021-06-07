import uuid

from django.db import models
from django.utils import timezone
from networth.models.mixins.validate_owns_object import ValidateOwnsObjectMixin
from users.models import User

from ..models.holding import Holding


class Transaction(ValidateOwnsObjectMixin, models.Model):
    BUY = "buy"
    SELL = "sell"
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"
    CREDIT = "credit"
    DEBIT = "debit"
    ACTIONS = (
        (BUY, "Buy"),
        (SELL, "Sell"),
        (DEPOSIT, "Deposit"),
        (WITHDRAW, "Withdraw"),
        (CREDIT, "Credit"),
        (DEBIT, "Debit"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    holding = models.ForeignKey(Holding, on_delete=models.CASCADE)
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
        self.validate_owns(model=Holding, instance=self.holding)
        self.net_amount = self.gross_amount - self.commission

        super(Transaction, self).save(*args, **kwargs)
