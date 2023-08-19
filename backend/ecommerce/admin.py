from django.contrib import admin
from .models import Products, Customers, ShoppingCart, CartItem

class CustomersRegister(admin.ModelAdmin):
    list_display = ('id', 'name', 'birth_date', 'gender', 'phone', 'email', 'address', 'shopping_cart', 'register_date', 'update_at')
    list_filter = ('gender',)
    
class CartItemInline(admin.TabularInline):
    model = CartItem

class ShoppingCartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]

class CustomersAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]

admin.site.register(Products)
admin.site.register(ShoppingCart, ShoppingCartAdmin)
admin.site.register(Customers, CustomersAdmin)

# admin.site.register(Customers, CustomersRegister)
