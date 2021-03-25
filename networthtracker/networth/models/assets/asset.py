from django.db import models

from users.models import User


class Asset(models.Model):
    id = models.UUIDField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(null=True, max_length=100)
    description = models.CharField(null=True, max_length=500)
    market_value = models.FloatField()
    book_value = models.FloatField()
    book_value_is_average = models.BooleanField(default=True)
    updated_on = models.DateTimeField()

    def __str__(self):
        return self.id
