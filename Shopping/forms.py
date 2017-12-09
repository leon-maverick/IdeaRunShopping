from django.contrib.auth.models import User
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

class OrderForm (forms.Form):
    # TODO multi choose from available products
    products = forms.CharField(label=_('products'))

class SearchForm (forms.Form):
    category_title = forms.CharField(required=False,label=_('Category'))
    product_title = forms.CharField(required=False, label=_('Product'))
