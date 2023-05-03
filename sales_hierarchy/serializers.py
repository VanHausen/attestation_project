from rest_framework import serializers

from sales_hierarchy.models import NetworkNode


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkNode
        fields = '__all__'
        read_only_fields = ('debt',)
