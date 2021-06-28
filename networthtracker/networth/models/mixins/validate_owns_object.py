import logging

from django.core.exceptions import ValidationError


# todo: rename class?
class ValidateOwnsObjectMixin:
    def validate_owns(self, instance):
        model = type(instance)
        if instance is None:
            logging.debug(f"Validating {model.__name__}: instance is None")
            return

        logging.debug(
            f'Validating {model.__name__}: "{instance.id}" belongs to user: "{self.user.id}"'
        )
        o = model.objects.get(id=instance.id)

        if o.user.id != self.user.id:
            raise ValidationError(
                f'{model.__name__}: "{instance.id}" does not belong to user: "{self.user.id}"'
            )
