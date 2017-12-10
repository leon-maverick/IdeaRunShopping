from django.contrib import admin
from .models import Product, Order, Category, NotAvPro
from django.utils.translation import ugettext_lazy as _



def make_done(modelAdmin, request, queryset):
    queryset.update(status="D")
make_done.short_description = "Change Status to done"

def make_cancel(modelAdmin, request, queryset):
    queryset.update(status="C")
make_cancel.short_description = "Change Status to Cancel"

class PriceRangeFilter(admin.SimpleListFilter):
    title = _('price range')
    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'price'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('L20', _('Less than 20000')),
            ('20N50', _('Btween 20000 and 50000')),
            ('G50', _('More than 50000')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == 'L20':
            return queryset.filter(price__lte=20000)
        if self.value() == '20N50':
            return queryset.filter(price__gte=20000,
                                   price__lte=50000)
        if self.value() == 'G50':
            return queryset.filter(price__gte=50000)


class TotalPriceRangeFilter(admin.SimpleListFilter):
    title = _('total price range')
    parameter_name = 'total_price'

    def lookups(self, request, model_admin):
        return (
            ('L20', _('Less than 20000')),
            ('20N50', _('Btween 20000 and 50000')),
            ('G50', _('More than 50000')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'L20':
            return queryset.filter(total_price__lte=20000)
        if self.value() == '20N50':
            return queryset.filter(total_price__gte=20000,
                                   total_price__lte=50000)
        if self.value() == 'G50':
            return queryset.filter(total_price__gte=50000)


class RelationInlineAdmin(admin.TabularInline):
    model = Order.products.through


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'cat', 'price', 'sold_price')
    list_filter = ('cat',PriceRangeFilter)
    inlines = [
        RelationInlineAdmin
    ]


class OrderAdmin (admin.ModelAdmin):

    inlines = [
        RelationInlineAdmin
    ]
    exclude = ('products',)
    list_display = ('person', 'status','total_price' )
    list_filter = (TotalPriceRangeFilter, )
    actions = [make_done, make_cancel]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'sold_price')

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(NotAvPro)


# TODO when I use action to done the order it doesnt affect sold price but when I change it indivdualy it's ok