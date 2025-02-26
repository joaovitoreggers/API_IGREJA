from rest_framework.viewsets import ModelViewSet
import tenancy
from tenancy.models import Tenancy
from .serializers import WorkerTypeSerializer
from .models import WorkerType

class WorkerTypeModelViewSet(ModelViewSet):
    serializer_class = WorkerTypeSerializer

    def get_queryset(self):
        user_tenancy = self.request.user.tenancy
        return WorkerType.objects.filter(tenancy = user_tenancy)
    
    def perform_create(self, serializer):
        user = self.request.user
        tenant = Tenancy.objects.get(id=user.tenancy.id)
        serializer.save(tenancy = tenant)