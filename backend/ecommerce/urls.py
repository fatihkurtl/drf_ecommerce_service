from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('api/ecommerce', views.ProductsViewSet, basename='ecommerce')
router.register('api/ecommerce/customers', views.CustomersViewSet, basename='ecommerce')

# router.register('api/ecommerce/customers/{pk}/shopping-cart', views.CustomersViewSet, basename='shopping-cart')

urlpatterns = router.urls
