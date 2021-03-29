from rest_framework import serializers

from .models import Asset, Cash


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = "__all__"
        read_only_fields = ["updated_on", "type", "id"]


class CashSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cash
        fields = "__all__"
        read_only_fields = ["updated_on", "type", "id"]
