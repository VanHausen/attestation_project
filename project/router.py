from rest_framework.routers import DefaultRouter

from sales_hierarchy.views import SupplierAPIView

router = DefaultRouter()
router.register('suppliers', SupplierAPIView, basename='suppliers')
