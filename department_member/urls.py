from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import DepartmentMemberModelViewSet

router = DefaultRouter()
router.register('department_member', DepartmentMemberModelViewSet, basename='department_member')

urlpatterns = [
    path('', include(router.urls))
]