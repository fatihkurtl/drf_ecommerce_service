from django.shortcuts import render

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from .models import Products, Customers, ShoppingCart
from .serializers import ProductsSerializer, CustomersSerializer, ShoppingCartSerializer

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = [
        DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter
    ]
    filterset_fields = ('name', 'admin', 'category')
    search_fields = ('name')
    ordering_fields = ('stock', 'create_at', 'update_at')


class CustomersViewSet(viewsets.ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer
    filter_backends = [
        DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter
    ]
    filterset_fields = ('name', 'gender', 'birth_date')
    search_fields = ('name')
    ordering_fields = ('phone', 'register_date', 'update_at')


class ShoppingCartViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer
    filter_backends = [
        DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter
    ]
    filterset_fields = ('customer', 'products')
    search_fields = ('customer')
    ordering_fields = ('added_date', 'update_at')