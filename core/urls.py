
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('worker_type.urls')),
    path('api/v1/', include('department.urls')),
    path('api/v1/', include('tax_document.urls')),
    path('api/v1/', include('suppliers.urls')),
    path('api/v1/', include('member.urls')),
    path('api/v1/', include('department_member.urls')),
]
