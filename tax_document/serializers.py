from rest_framework import serializers

from .models import TaxDocument, DocumentType

class TaxDocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaxDocument
        fields = '__all__'

class DocumentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = DocumentType
        fields = '__all__'