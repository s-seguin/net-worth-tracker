import logging

from django.core.exceptions import ValidationError


class ValidateOwnsObjectMixin:
    def validate_owns(self, model, instance):
        logging.debug(
            f'Validating {model.__name__}: "{instance.id}" belongs to user: "{self.user.id}"'
        )
        o = model.objects.get(id=instance.id)

        if o.user.id != self.user.id:
            raise ValidationError(
                f'{model.__name__}: "{instance.id}" does not belong to user: "{self.user.id}"'
            )
