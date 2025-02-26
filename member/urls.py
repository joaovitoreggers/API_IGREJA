from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import MemberModelViewSet

router = DefaultRouter()
router.register('member', MemberModelViewSet, basename='member')

urlpatterns = [
    path('', include(router.urls))
]