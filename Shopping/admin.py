from django.contrib import admin
from .models import Product, Order, Category

class ProductAdmin (admin.ModelAdmin):
    list_display = ('title', 'cat', 'price')
    list_filter = ('cat',)


class OrderAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.person = request.user
        super(OrderAdmin,self).save_model(request,obj,form,change)


admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(Category)


