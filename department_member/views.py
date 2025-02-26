from rest_framework.viewsets import ModelViewSet
from tenancy.models import Tenancy
from .serializers import DepartmentMemberSerializer
from .models import DepartmentMember

class DepartmentMemberModelViewSet(ModelViewSet):
    serializer_class = DepartmentMemberSerializer

    def get_queryset(self):
        user_tenancy = self.request.user.tenancy
        return DepartmentMember.objects.filter(tenancy = user_tenancy)
    
    def perform_create(self, serializer):
        user = self.request.user
        tenant = Tenancy.objects.get(id=user.tenancy.id)
        serializer.save(tenancy = tenant)