from django.db import models

from ..holding import Holding
from ..mixins.validate_owns_object import ValidateOwnsObjectMixin


class Liability(ValidateOwnsObjectMixin, Holding):
    CREDIT_CARD = "credit_card"
    MORTGAGE = "mortgage"
    LOAN = "loan"
    TYPE_CHOICES = (
        (CREDIT_CARD, "Credit Card"),
        (MORTGAGE, "Mortgage"),
        (LOAN, "Loan"),
    )

    amount_owing = models.FloatField()
    type = models.CharField(max_length=11, null=True, choices=TYPE_CHOICES)
