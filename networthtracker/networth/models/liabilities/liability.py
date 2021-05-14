import uuid

from django.db import models
from django.utils import timezone
from users.models import User

from ..mixins.validate_owns_object import ValidateOwnsObjectMixin


class Liability(ValidateOwnsObjectMixin, models.Model):
    CREDIT_CARD = "credit_card"
    MORTGAGE = "mortgage"
    LOAN = "loan"
    TYPE_CHOICES = (
        (CREDIT_CARD, "Credit Card"),
        (MORTGAGE, "Mortgage"),
        (LOAN, "Loan"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(null=True, max_length=100)
    description = models.CharField(null=True, max_length=500)
    # market_value = models.FloatField()
    # book_value = models.FloatField()
    # book_value_is_average = models.BooleanField(default=True)
    amount_owing = (
        models.FloatField()
    )  # todo should we use the market value etc here?
    type = models.CharField(max_length=11, null=True, choices=TYPE_CHOICES)
    updated_on = models.DateTimeField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.updated_on = timezone.now()
        super(Liability, self).save(*args, **kwargs)
