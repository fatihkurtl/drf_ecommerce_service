from django.db import models
from django.conf import settings

class Products(models.Model):
    name = models.CharField(max_length=60, null=False)
    brand = models.CharField(max_length=60, null=False)
    image = models.ImageField(null=False)
    price = models.FloatField(null=False)
    category = models.CharField(max_length=100, null=False)
    stock = models.IntegerField(null=False)
    description = models.TextField()
    admin = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='products',
        null=True,
        blank=True,
    )
    create_at = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.admin} - {self.name}'
    

class ShoppingCart(models.Model):
    customer = models.OneToOneField('Customers', on_delete=models.CASCADE, related_name='cart')
    products = models.ManyToManyField('Products', related_name='shopping_carts', through='CartItem')
    added_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Shopping Cart for {self.customer}'

class CartItem(models.Model):
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    product = models.ForeignKey('Products', on_delete=models.CASCADE)
    customer = models.ForeignKey('Customers', on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f'{self.quantity} x {self.product}'

class Customers(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    name = models.CharField(max_length=50, null=False)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=250, null=False)
    
    shopping_cart = models.OneToOneField(ShoppingCart, on_delete=models.SET_NULL, null=True, blank=True)
    
    register_date = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.name}'

    