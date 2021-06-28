from django.db import models
from django.db.models.functions import Coalesce

from .transaction import VALUE_FIELD_NAME as TRANSACTION_VALUE_FIELD_NAME


class HoldingManager(models.Manager):
    def get_queryset(self):
        """Include transaction sums when returning Holdings"""
        return (
            super()
            .get_queryset()
            .annotate(
                transaction_sum=Coalesce(
                    models.Sum(TRANSACTION_VALUE_FIELD_NAME), models.Value(0)
                )
            )
        )
