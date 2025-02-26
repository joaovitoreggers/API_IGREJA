from rest_framework import serializers

from .models import Tenancy

class TenancySerializar(serializers.ModelSerializer):

    class Meta:
        model = Tenancy
        fields = '__all__'