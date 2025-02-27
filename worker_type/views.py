from rest_framework.viewsets import ModelViewSet
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
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


class WorkerTypeListView(ListView):
    model = WorkerType
    template_name = 'worker_type_list.html'
    context_object_name = 'worker_type'