from rest_framework import permissions, viewsets

from .models import Account, Asset, Cash, Property, Security, Transaction
from .permissions import IsOwner
from .serializers import (
    AccountSerializer,
    AssetSerializer,
    CashSerializer,
    PropertySerializer,
    SecuritySerializer,
    TransactionSerializer,
)


class SetUserMixin(viewsets.ModelViewSet):
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AssetViewSet(SetUserMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows assets to be viewed or edited.
    """

    serializer_class = AssetSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Asset.objects.filter(user=self.request.user).order_by(
            "-updated_on"
        )


class CashViewSet(SetUserMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows cash assets to be viewed or edited.
    """

    serializer_class = CashSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Cash.objects.filter(user=self.request.user).order_by(
            "-updated_on"
        )


class PropertyViewSet(SetUserMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows property assets to be viewed or edited.
    """

    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Property.objects.filter(user=self.request.user).order_by(
            "-updated_on"
        )


class SecurityViewSet(SetUserMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows security assets to be viewed or edited.
    """

    serializer_class = SecuritySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Security.objects.filter(user=self.request.user).order_by(
            "-updated_on"
        )


class AccountViewSet(SetUserMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows accounts to be viewed or edited.
    """

    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user).order_by(
            "-updated_on"
        )


class TransactionViewSet(SetUserMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows accounts to be viewed or edited.
    """

    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user).order_by(
            "-updated_on"
        )
