from django.shortcuts import render, get_object_or_404
from Shopping.forms import UserForm, UserFormIn, OrderForm, SearchForm
from .models import Product, Order, Category
from .serializers import ProductSerializer, OrderSerializer, CategorySerializer
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View


class ApiSearchProduct(generics.ListAPIView): #search on title of the products
    permission_classes = []
    def get(self, request):
        query = request.data
        if not 'title' in query:
            return Response('No Data entry')
        else:
            queryset = Product.objects.filter(title__contains=query['title'])
            serializer_class = ProductSerializer(queryset, many=True)
            return Response(serializer_class.data)


class ApiCatProductList(generics.ListAPIView):# returns the products of searched category
    permission_classes = []
    def get(self, request):
        query = request.data
        if not 'cat' in query:
            return Response('No Data entry')
        else:
            queryset = Product.objects.filter(cat__title__contains=query['cat'],)
            serializer_class = ProductSerializer(queryset, many=True)
            return Response(serializer_class.data)


class ApiCategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = []


class ApiSignUpView(APIView):
    permission_classes = []

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token, created = Token.objects.get_or_create(user=user)
                json = serializer.data
                # todo bug in here. read about get_or_create to fix it
                json['token'] = token.key

                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApiMyOrderList(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def get_queryset(self):
        return Order.objects.filter(person=self.request.user)

    def perform_create(self, serializer):

        serializer.person = self.request.user
        serializer.status = "P"
        super().perform_create(serializer,)


class ApiProductList(generics.ListCreateAPIView):
    """
    get:
    list of available products
    """
    queryset = Product.objects.filter(available__gt=0)
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


def Index (request):
    return render(request, 'shopping/Index.html')


class ProductList(View):

    def get(self, request, pk):
        if pk == '0':
            all_products = Product.objects.all()
            return render (request, 'shopping/product.html', {'products': all_products})

        elif pk!=0:
            all_products = Product.objects.filter(cat_id = pk)
            cat = get_object_or_404(Category, pk=pk)
            return render(request, 'shopping/product.html', {'products': all_products, 'catcat':cat.title})


def ProductListDetail(request, pk):
    product = get_object_or_404( Product,pk = pk)
    return render(request, 'shopping/productdetail.html', {'product':product})


def CategoryDetail(request, pk):
    cat = get_object_or_404(Category, pk = pk)
    print(cat)
    print (cat.title)
    product = Product.objects.filter(cat__title__contains = cat.title)
    print(product)
    return render(request, 'shopping/categorydetail.html',{'product':product})


class SignUp (View): # TODO password check
    form_class = UserForm
    template_name = 'shopping/signup.html'

    # dispaly new form for register
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # just store it normally
            # clean and normalize data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user.set_password(password)

            user.save()

            # return user objects if credentials are correct
            user = authenticate(username=username, password=password,
                                first_name=first_name, last_name=last_name, email=email)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('shop:homepage')
        return render(request, self.template_name, {'form': form})


class SignIn (View):
    form_class = UserFormIn
    template_name = 'shopping/signin.html'

    # dispaly new form for register
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            # clean and normalize data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # return user objects if credentials are correct
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('shop:homepage')
        return render(request, self.template_name, {'form': form})


class search (View):
    form_class = SearchForm
    template_name = 'shopping/search.html'

    def get (self, request):
        products = []
        form = self.form_class(None)
        return render (request, self.template_name, { 'form' : form, 'products':products })

    def post (self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            category_title = form.cleaned_data['category_title']
            product_title = form.cleaned_data['product_title']
            if product_title:
                products = Product.objects.filter(title__contains=product_title)
            elif category_title:
                products = Product.objects.filter(cat__title__contains= category_title)
            elif category_title and product_title:
                pass
        return render (request, self.template_name, {'form':form, 'products':products})


def LogOut(request):
    logout(request)
    return render(request, 'shopping/Index.html')


def Categories (request):
    cats = Category.objects.all()
    return render (request, 'shopping/Categories.html', {'cats':cats})


class Orders(View):
    form_class = OrderForm
    template_name = 'shopping/myorders.html'
    def get(self, request):
        form = self.form_class(None)
        orders = Order.objects.filter(person=request.user)
        return render (request, self.template_name, {'orders':orders, 'form':form})

    def post (self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            # clean and normalize data
            products = form.cleaned_data['products']
            order = Order.objects.create(person = request.user)
            order.total_price = 0
            print(products)
            for p in products:
                order.products.add(p)
                order.total_price = order.total_price + p.price
            order.save()
            orders = Order.objects.filter(person=request.user)

        return render(request, self.template_name, {'orders':orders ,'form': form})

