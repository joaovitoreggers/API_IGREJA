from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Tenancy

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'tenancy', 'phone_number', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('tenancy', 'phone_number')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('tenancy', 'phone_number')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
