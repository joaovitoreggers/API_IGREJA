from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TaxDocumentModelViewSet, DocumentTypeModelViewSet

router = DefaultRouter()
router.register('tax_document', TaxDocumentModelViewSet, basename='tax_document'),
router.register('document_type', DocumentTypeModelViewSet, basename='document_type'),

urlpatterns = [
    path('', include(router.urls))
]