from rest_framework.viewsets import ModelViewSet
from tenancy.models import Tenancy
from .serializers import WorkerTypeSerializer
from .models import WorkerType

class WorkerTypeModelViewSet(ModelViewSet):
    serializer_class = WorkerTypeSerializer

    def get_queryset(self):
        user_tenancy = self.request.user.tenancy
        return WorkerType.objects.filter(tenancy = user_tenancy)