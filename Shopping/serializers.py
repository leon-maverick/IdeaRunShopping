from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Product, Order, Category
from rest_framework.validators import UniqueValidator


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        extra_kwargs = {
            'title': {'read_only': True},
        }


class ProductSerializer(serializers.ModelSerializer):
    cat = serializers.CharField(source='cat.title', read_only=True)

    class Meta:
        model = Product
        fields = ('title', 'cat', 'price', 'available', 'description', 'available', 'pic')


class OrderSerializer(serializers.ModelSerializer):
    # products_names = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    products = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)
    # status = serializers.CharField(source='get_status_display')

    class Meta:
        model = Order
        fields = ('date', 'products', 'status','total_price')
        extra_kwargs = {
            'date': {'read_only': True},
        }

    def validate(self, attr):
        for p in attr['products']:
            if p.available <= 0:
                raise serializers.ValidationError(p.title + " is not available")
        return attr

    def create(self, validated_data, ):
        validated_data['person'] = self.person
        validated_data['status'] = self.status

        price = 0
        for p in validated_data.get('products') :
            price = price + p.price
        validated_data['total_price'] = price
        order = super().create(validated_data)

        return order


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

        user.first_name = validated_data['first_name']
        user.last_name = validated_data['last_name']
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
