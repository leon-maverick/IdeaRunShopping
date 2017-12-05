from django.contrib import admin
from .models import Product, Order, Category


class RelationInlineAdmin(admin.TabularInline):
    model = Order.products.through


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'cat', 'price')
    list_filter = ('cat',)
    inlines = [
        RelationInlineAdmin
    ]


class OrderAdmin (admin.ModelAdmin):

    inlines = [
        RelationInlineAdmin
    ]
    exclude = ('products',)
    list_display = ('person', 'status','total_price' )

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Category)
