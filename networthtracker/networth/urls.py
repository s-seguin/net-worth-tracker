from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"assets/cash", views.CashViewSet, basename="cash")
router.register(r"assets", views.AssetViewSet, basename="asset")

urlpatterns = [
    path("", include(router.urls)),
]
