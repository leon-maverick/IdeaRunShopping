from django.conf.urls import url
from Shopping import views

urlpatterns = [
    #//todo don't use camel case for urls. we normally use dash (e.g. my-orders)
    # also it's important for the urls to be readable (e.g. product-list instead of p-list)
    url(r'^product-lists/', views.ProductList.as_view(), ),
    url(r'^my-orders/', views.MyOrderList.as_view(), ),
    url(r'^signup/', views.SignUpView.as_view(), ),
    url(r'^category-lists/', views.CategoryList.as_view(), ),
    url(r'^category-product/', views.CatProductList.as_view(), ),
    url(r'^search-product/', views.SearchProduct, ),
]
