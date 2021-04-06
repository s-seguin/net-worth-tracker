from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"assets/cash", views.CashViewSet, basename="cash")
router.register(
    r"assets/properties", views.PropertyViewSet, basename="property"
)
router.register(
    r"assets/securities", views.SecurityViewSet, basename="security"
)
router.register(r"assets", views.AssetViewSet, basename="asset")
router.register(r"accounts", views.AccountViewSet, basename="account")
router.register(
    r"transactions", views.TransactionViewSet, basename="transaction"
)

urlpatterns = [path("", include(router.urls))]
