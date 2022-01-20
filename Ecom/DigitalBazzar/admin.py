from django.contrib import admin

from .models import Cart, Customer, Order, Products,Shipping

admin.site.register(Products)
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Shipping)

