from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import WorkerTypeModelViewSet

router = DefaultRouter()
router.register('worker_type', WorkerTypeModelViewSet, basename='worker_type')

urlpatterns = [
    path('', include(router.urls))
]