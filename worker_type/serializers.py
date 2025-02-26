from rest_framework import serializers

from .models import WorkerType

class WorkerTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkerType
        fields = '__all__'
        