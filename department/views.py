from rest_framework.viewsets import ModelViewSet

from tenancy.models import Tenancy
from .models import Department
from .serializers import DepartmentSerializer

class DepartmentModelViewSet(ModelViewSet):
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        user_tenant = self.request.user.tenancy
        return Department.objects.filter(tenancy = user_tenant)
    
    def perform_create(self, serializer):
        user = self.request.user
        tenant = Tenancy.objects.get(id=user.tenancy.id)
        serializer.save(tenancy=tenant)