from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import *


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'link_supplier']
    list_filter = ['city']

    def link_supplier(self, obj):
        link = reverse("admin:sales_hierarchy_networknode_change", args=[obj.supplier_id])
        if obj.supplier:
            return format_html('<a href="{}">{}</a>', link, obj.supplier.name)
        else:
            return format_html('<p>-</p>')

    link_supplier.allow_tags = True

    def clear_debt(self, request, queryset):
        updated_debt = queryset.update(debt=0.00)
        self.message_user(request, f'{updated_debt} объектов списана задолженность.')

    clear_debt.short_description = 'Очистить задолженность по выбранным объектам'
    actions = [clear_debt]

    change_list_template = 'admin/networknode_change_list.html'

@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    pass


@admin.register(RetailNetwork)
class RetailNetworkAdmin(admin.ModelAdmin):
    pass


@admin.register(IndividualEntrepreneur)
class IndividualEntrepreneurAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class Product(admin.ModelAdmin):
    pass
