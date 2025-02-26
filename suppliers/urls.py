from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import SupplierModelViewSet

router = DefaultRouter()
router.register('supplier', SupplierModelViewSet, basename='supplier')

urlpatterns = [
    path('', include(router.urls))
]