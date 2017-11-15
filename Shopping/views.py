from .models import Product, Order, Category
from .serializers import ProductSerializer, OrderSerializer, CategorySerializer
from rest_framework.views import APIView
from rest_framework import generics
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .serializers import UserSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views import generic

@api_view(['GET'])
def SearchProduct(request):
    query = request.data
    queryset = Product.objects.filter(title__contains=query['title'])
    serializer_class = ProductSerializer(queryset, many=True)
    permission_classes = []  # (permissions.IsAuthenticatedOrReadOnly)
    return Response(serializer_class.data)


@api_view(['GET'])
def CatProductList(request):
    query = request.data
    queryset = Product.objects.filter(cat__title__contains=query['cat'])
    serializer_class = ProductSerializer(queryset, many=True)
    permission_classes = []
    return Response(serializer_class.data)


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = []


class SignUpView(APIView):
    permission_classes = []
    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.get_or_create(user=user)
                json = serializer.data
                json['token'] = token.key
                print(json['token'])
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MyOrdersUpdate(generic.UpdateView):
    pass

class MyOrderList(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def get_queryset(self):
        return Order.objects.filter(person=self.request.user)

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.person = self.request.user
        serializer.status = "P"
        # serializer.save(person=self.request.user, status="P")
        super().perform_create(serializer)

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.filter(available__gt=0)
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
