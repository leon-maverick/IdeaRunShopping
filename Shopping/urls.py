from django.conf.urls import url
from Shopping import views

urlpatterns = [
    #todo don't use camel case for urls. we normally use dash (e.g. my-orders)
    # also it's important for the urls to be readable (e.g. product-list instead of p-list)
    url(r'^PLists/', views.ProductList.as_view(), ),
    url(r'^MyOrders/', views.MyOrderList.as_view(), ),
    url(r'^SignUp/', views.SignUpView.as_view(), ),
    url(r'^CatLists/', views.CategoryList.as_view(), ),
    url(r'^CatProduct/', views.CatProductList, ),
    url(r'^SearchProduct/', views.SearchProduct, ),
]
