from django.db import models

from users.models import User


class Account(models.Model):
    id = models.UUIDField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    account_number = models.CharField(max_length=150)
    type = models.CharField(max_length=150)
    # todo look into this package: https://github.com/django-money/django-money
    balance = models.FloatField()

    # todo finish references

    def __str__(self):
        return self.name
