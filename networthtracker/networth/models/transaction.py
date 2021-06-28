import uuid

from django.db import models
from django.utils import timezone

from .mixins.validate_owns_object import ValidateOwnsObjectMixin

INC = "increase"
DEC = "decrease"

BUY = "buy"
SELL = "sell"
DEPOSIT = "deposit"
WITHDRAW = "withdraw"
CREDIT = "credit"
DEBIT = "debit"

ACTIONS = {
    BUY: INC,
    SELL: DEC,
    DEPOSIT: INC,
    WITHDRAW: DEC,
    CREDIT: INC,
    DEBIT: DEC,
}

# the full name of the value field, used to sum all transactions for a holding
# todo should this be a property of the model?
VALUE_FIELD_NAME = "transaction__net_amount"


class Transaction(ValidateOwnsObjectMixin, models.Model):
    ACTION_CHOICES = (
        (BUY, "Buy"),
        (SELL, "Sell"),
        (DEPOSIT, "Deposit"),
        (WITHDRAW, "Withdraw"),
        (CREDIT, "Credit"),
        (DEBIT, "Debit"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    holding = models.ForeignKey("networth.Holding", on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    transaction_date = models.DateTimeField()
    settlement_date = models.DateTimeField()
    action = models.CharField(max_length=8, choices=ACTION_CHOICES)
    description = models.CharField(max_length=300, null=True)
    quantity = models.FloatField(null=True)
    gross_amount = models.FloatField()
    net_amount = models.FloatField()  # gross_amount - commission
    commission = models.FloatField(null=True)
    updated_on = models.DateTimeField()

    def __str__(self):
        return self.description

    def save(self, *args, **kwargs):
        self.validate_owns(instance=self.holding)
        self.updated_on = timezone.now()

        self.quantity = abs(self.quantity)
        self.gross_amount = abs(self.gross_amount)
        self.commission = abs(self.commission)

        self.net_amount = self.gross_amount - self.commission

        if ACTIONS[self.action] == DEC:
            self.gross_amount = -self.gross_amount
            self.net_amount = -self.net_amount
            if self.quantity is not None:
                self.quantity = -self.quantity

        super(Transaction, self).save(*args, **kwargs)
