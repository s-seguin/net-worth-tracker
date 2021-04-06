import uuid

from django.db import models
from django.utils import timezone
from users.models import User

from .account import Account
from .assets.asset import Asset
from .mixins.validate_owns_object import ValidateOwnsObjectMixin


class Transaction(ValidateOwnsObjectMixin, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account = models.ForeignKey(Account, null=True, on_delete=models.SET_NULL)
    # should asset and liability be grouped under holding?
    asset = models.ForeignKey(Asset, null=True, on_delete=models.CASCADE)
    # liability = models.ForeignKey(Liability, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_date = models.DateTimeField()
    settlement_date = models.DateTimeField()
    activity_type = models.CharField(max_length=100)
    action = models.CharField(max_length=10, null=True)
    description = models.CharField(max_length=300, null=True)
    quantity = models.FloatField()
    price = models.FloatField()
    gross_amount = models.FloatField()
    net_amount = models.FloatField()
    commission = models.FloatField()
    updated_on = models.DateTimeField()

    def __str__(self):
        return self.description

    def save(self, *args, **kwargs):
        self.updated_on = timezone.now()
        self.validate_owns(model=Account, instance=self.account)
        self.validate_owns(model=Asset, instance=self.asset)
        # todo self.validate_owns(model=Liability, instance=self.liability)
        super(Transaction, self).save(*args, **kwargs)
