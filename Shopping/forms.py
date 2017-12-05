from django.contrib.auth.models import User
from django import forms

class UserForm ( forms.ModelForm ):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:#information about the class
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

class UserFormIn ( forms.Form ):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class OrderForm (forms.Form):
    # TODO multi choose from available products
    products = forms.CharField()

class SearchForm (forms.Form):
    category_title = forms.CharField(required=False)
    product_title = forms.CharField(required=False)
