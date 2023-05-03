from django.contrib import messages
from django.shortcuts import redirect
from rest_framework import permissions
from rest_framework.viewsets import GenericViewSet, mixins
from django_filters.rest_framework import DjangoFilterBackend

from sales_hierarchy.models import NetworkNode
from sales_hierarchy.permissions import IsActive
from sales_hierarchy.serializers import SupplierSerializer


class SupplierAPIView(GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = SupplierSerializer
    queryset = NetworkNode.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country']
    permission_classes = [IsActive]


def clear_all_debt(request):
    NetworkNode.objects.all().update(debt=0.00)
    messages.success(request, 'Задолженность по всем объектам успешно очищена.')
    return redirect('admin:sales_hierarchy_networknode_changelist')
