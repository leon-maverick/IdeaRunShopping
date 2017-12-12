from django.contrib.auth.models import User
from .models import Order, Product
from django import forms
from django.utils.translation import gettext_lazy as _

class UserForm ( forms.ModelForm ):
    password = forms.CharField(widget=forms.PasswordInput, label=_('password'))
    class Meta:#information about the class
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

class UserFormIn ( forms.Form ):
    username = forms.CharField(label =_('username'))
    password = forms.CharField(widget=forms.PasswordInput, label =_('password'))

class OrderForm (forms.ModelForm):
    # TODO multi choose from available products
    # products = forms.CharField(label=_('products'))
    products = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset= Product.objects.filter(available__gt=0))

    class Meta:
        model = Order
        fields=['products', ]

    def save(self, commit=True):
        order = super(OrderForm, self).save(commit=False)
        for p in (order.products.all()):
            order.total_price = order.total_price + p.price
        print("hereeee")
        print(order.total_price)
        order.save()

        return order


class SearchForm (forms.Form):
    category_title = forms.CharField(required=False,label=_('Category'))
    product_title = forms.CharField(required=False, label=_('Product'))
