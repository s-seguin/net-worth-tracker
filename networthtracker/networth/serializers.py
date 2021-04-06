from rest_framework import serializers

from .models import Account, Asset, Cash, Property, Security, Transaction


class AssetForeignKey(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        return Asset.objects.filter(user=self.context["request"].user)


class AccountForeignKey(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        return Account.objects.filter(user=self.context["request"].user)


class AssetSerializer(serializers.ModelSerializer):
    account = AccountForeignKey()

    class Meta:
        model = Asset
        fields = "__all__"
        read_only_fields = ["updated_on", "type", "id", "user"]


class CashSerializer(AssetSerializer):
    class Meta:
        model = Cash
        fields = "__all__"
        read_only_fields = ["updated_on", "type", "id", "user"]


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


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"
        read_only_fields = ["updated_on", "id", "user"]


class TransactionSerializer(serializers.ModelSerializer):
    asset = AssetForeignKey()
    account = AccountForeignKey()

    class Meta:
        model = Transaction
        fields = "__all__"
        read_only_fields = ["updated_on", "id", "user"]
