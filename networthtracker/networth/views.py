from rest_framework import viewsets
from rest_framework import permissions

from .permissions import IsOwner
from .models import Asset, Cash
from .serializers import AssetSerializer, CashSerializer

import logging


class AssetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows assets to be viewed or edited.
    """

    logging.debug("test test")
    serializer_class = AssetSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Asset.objects.filter(user=self.request.user).order_by(
            "-updated_on"
        )


class CashViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cash assets to be viewed or edited.
    """

    serializer_class = CashSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Cash.objects.filter(user=self.request.user).order_by(
            "-updated_on"
        )
