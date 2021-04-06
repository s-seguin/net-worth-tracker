import uuid

from django.db import models
from django.utils import timezone
from users.models import User


class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=300, null=True)
    # todo look into this package: https://github.com/django-money/django-money
    balance = models.FloatField()
    updated_on = models.DateTimeField()

    # todo finish references

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.updated_on = timezone.now()
        super(Account, self).save(*args, **kwargs)
