from rest_framework import serializers

from .models import DepartmentMember

class DepartmentMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = DepartmentMember
        fields = '__all__'