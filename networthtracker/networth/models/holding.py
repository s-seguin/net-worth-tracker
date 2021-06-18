import uuid

from django.db import models
from django.utils import timezone
from users.models import User


class Holding(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(null=True, max_length=100)
    description = models.CharField(null=True, max_length=500)
    updated_on = models.DateTimeField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.updated_on = timezone.now()

        super(Holding, self).save(*args, **kwargs)
