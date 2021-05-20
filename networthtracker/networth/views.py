from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

from .models import Asset, Cash, Liability, Property, Security, Transaction
from .permissions import IsOwner
from .serializers import (
    AssetSerializer,
    CashSerializer,
    LiabilitySerializer,
    PropertySerializer,
    SecuritySerializer,
    TransactionSerializer,
)
from .services.transaction import TransactionService


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


class LiabilityViewSet(SetUserMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows liabilities to be viewed or edited.
    """

    serializer_class = LiabilitySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Liability.objects.filter(user=self.request.user).order_by(
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


class TransactionViewSet(viewsets.ViewSet):
    """
    API endpoint that allows transactions to be viewed or edited.
    """

    serializer_class = TransactionSerializer  # needed for browsable api
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    @staticmethod
    def list(request):
        transactions = TransactionService.get_transactions(user=request.user)
        data = TransactionSerializer(transactions, many=True).data

        return Response(data)

    @staticmethod
    def create(request):
        serializer = TransactionSerializer(
            data=request.data, context={"request": request}
        )
        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        transaction = TransactionService.create_transaction(
            user=request.user, **serializer.validated_data
        )
        data = TransactionSerializer(
            transaction, context={"request": request}
        ).data
        return Response(data, status=status.HTTP_201_CREATED)
