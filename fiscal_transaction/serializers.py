from rest_framework import serializers

from .models import FiscalTransaction

class FiscalTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = FiscalTransaction
        fields = '__all__'