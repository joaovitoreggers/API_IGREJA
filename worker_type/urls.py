from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import WorkerTypeModelViewSet, WorkerTypeListView

router = DefaultRouter()
router.register('worker_type', WorkerTypeModelViewSet, basename='worker_type')

urlpatterns = [
    path('api/v1/', include(router.urls)),

    path('worker_type/list/', WorkerTypeListView.as_view(), name='worker_type_list_view')
]