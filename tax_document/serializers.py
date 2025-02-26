from rest_framework import serializers

from .models import TaxDocument

class TaxDocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaxDocument
        fields = '__all__'