from rest_framework.viewsets import ModelViewSet

from tenancy.models import Tenancy
from .models import DocumentType, TaxDocument
from .serializers import DocumentTypeSerializer, TaxDocumentSerializer

class TaxDocumentModelViewSet(ModelViewSet):
    serializer_class = TaxDocumentSerializer

    def get_queryset(self):
        user_tenant = self.request.user.tenancy
        return TaxDocument.objects.filter(tenancy = user_tenant)
    
    def perform_create(self, serializer):
        user = self.request.user
        tenant = Tenancy.objects.get(id=user.tenancy.id)
        serializer.save(tenancy=tenant)


class DocumentTypeModelViewSet(ModelViewSet):
    serializer_class = DocumentTypeSerializer

    def get_queryset(self):
        user_tenant = self.request.user.tenancy
        return DocumentType.objects.filter(tenancy = user_tenant)
    
    def perform_create(self, serializer):
        user = self.request.user
        tenant = Tenancy.objects.get(id=user.tenancy.id)
        serializer.save(tenancy=tenant)