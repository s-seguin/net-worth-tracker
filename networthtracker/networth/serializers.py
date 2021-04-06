from rest_framework import serializers

from .models import Account, Asset, Cash, Property, Security, Transaction


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = "__all__"
        read_only_fields = ["updated_on", "type", "id", "user"]


class CashSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cash
        fields = "__all__"
        read_only_fields = ["updated_on", "type", "id", "user"]


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = "__all__"
        read_only_fields = ["updated_on", "type", "id", "user"]


class SecuritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Security
        fields = "__all__"
        read_only_fields = ["updated_on", "type", "id", "user"]


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"
        read_only_fields = ["updated_on", "id", "user"]


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"
        read_only_fields = ["updated_on", "id", "user"]
