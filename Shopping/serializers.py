from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Product, Order, Category
from rest_framework.validators import UniqueValidator


#todo unused class
class ProductListingField(serializers.RelatedField):
    def to_representation(self, value):
        return 'Product %s: %d (%s) [description: %s]' % (value.title,
                                                          value.price, value.cat, value.description)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        extra_kwargs = {
            'title': {'read_only': True},
        }


class ProductSerializer(serializers.ModelSerializer):
    # todo when sending product data, send the category (cat) as a json, not just id.
    # i would want to see the category name alongside the product data
    class Meta:
        model = Product
        fields = ('title', 'cat', 'price', 'available', 'description', 'available', 'pic')


class OrderSerializer(serializers.ModelSerializer):
    # queryset = Product.objects.filter(available__gt=0)


    # todo it's minor thing, but always put the class Meta before all the methods, then validators, then other methods
    def validate(self, attr):
        for p in attr['products']:
            if p.available <= 0:
                raise serializers.ValidationError(p.title + " is not available")
        return attr

    class Meta:
        model = Order
        fields = ('date', 'products', 'status',)
        extra_kwargs = {
            'date': {'read_only': True},
        }

    def create(self, validated_data):
        validated_data['person'] = self.person
        validated_data['status'] = self.status
        print(validated_data)
        return super().create(validated_data)


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
                                        validated_data['password'], )
        print(validated_data)
        print(validated_data['first_name'])

        user.first_name = validated_data['first_name']
        user.last_name = validated_data['last_name']
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
