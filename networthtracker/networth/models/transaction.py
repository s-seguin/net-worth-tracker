import uuid

from django.db import models
from users.models import User


class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # todo finish references
    # not sure if this is the relationship or account
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

    def __str__(self):
        return self.description
