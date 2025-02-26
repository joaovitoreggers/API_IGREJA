from django.contrib import admin
from .models import Tenancy  

@admin.register(Tenancy)
class TenancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', )
    search_fields = ('name',)
    ordering = ('id',)