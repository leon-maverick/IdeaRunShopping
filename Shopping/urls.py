from django.conf.urls import url
from Shopping import views

urlpatterns = [
    url(r'^PLists/', views.ProductList.as_view(), ),
    url(r'^MyOrders/', views.MyOrderList.as_view(), ),
    url(r'^SignUp/', views.SignUpView.as_view(), ),
    url(r'^CatLists/', views.CategoryList.as_view(), ),
    url(r'^CatProduct/', views.CatProductList, ),
    url(r'^SearchProduct/', views.SearchProduct, ),
]
