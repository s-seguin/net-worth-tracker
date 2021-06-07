from rest_framework import serializers

from .models import Asset, Cash, Liability, Property, Security, Transaction
from .models.holding import Holding


class HoldingForeignKey(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        return Holding.objects.filter(user=self.context["request"].user)


# Serializers


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = "__all__"
        read_only_fields = ["updated_on", "type", "id", "user"]


class CashSerializer(AssetSerializer):
    class Meta:
        model = Cash
        fields = "__all__"
        read_only_fields = ["updated_on", "type", "id", "user"]


class LiabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Liability
        fields = "__all__"
        read_only_fields = [
            "updated_on",
            "id",
            "user",
        ]  # todo if mortgage model etc. made, make type readonly


class PropertySerializer(AssetSerializer):
    class Meta:
        model = Property
        fields = "__all__"
        read_only_fields = ["updated_on", "type", "id", "user"]


class SecuritySerializer(AssetSerializer):
    class Meta:
        model = Security
        fields = "__all__"
        read_only_fields = ["updated_on", "type", "id", "user"]


class TransactionSerializer(serializers.ModelSerializer):
    holding = HoldingForeignKey()

    class Meta:
        model = Transaction
        fields = "__all__"
        read_only_fields = ["updated_on", "id", "user", "net_amount"]
