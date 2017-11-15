from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Product, Order, Category
from rest_framework.validators import UniqueValidator


class ProductListingField(serializers.RelatedField):
    def to_representation(self, value):
        return 'Product %s: %d (%s)' % (value.title, value.price, value.cat)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        extra_kwargs = {
            'title': {'read_only': True},
        }


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'cat', 'price', 'available', 'description', 'available')


class OrderSerializer(serializers.ModelSerializer):
    queryset = Product.objects.all()

    # products = ProductListingField(many=True,queryset=queryset )
    class Meta:
        model = Order
        fields = ('date', 'products', 'status', )
        extra_kwargs = {
            'date': {'read_only': True},
        }


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
                                        validated_data['password'],)
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
