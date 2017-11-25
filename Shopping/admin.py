from django.contrib import admin
from .models import Product, Order, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'cat', 'price')
    list_filter = ('cat',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(Category)
