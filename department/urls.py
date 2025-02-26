from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import DepartmentModelViewSet

router = DefaultRouter()
router.register('department', DepartmentModelViewSet, basename='department')

urlpatterns = [
    path('', include(router.urls))
]