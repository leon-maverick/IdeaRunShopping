from django.conf.urls import url
from Shopping import views
app_name = 'shop'

urlpatterns = [

    url(r'^api-product-lists/', views.ApiProductList.as_view(), ),
    url(r'^api-my-orders/', views.ApiMyOrderList.as_view(), ),
    url(r'^api-signup/', views.ApiSignUpView.as_view(), ),
    url(r'^api-category-lists/', views.ApiCategoryList.as_view(), ),
    url(r'^api-category-product/', views.ApiCatProductList.as_view(), ),
    url(r'^api-search-product/', views.ApiSearchProduct.as_view(), ),

    url(r'^home', views.Index, name='homepage'),
    url(r'^product-lists/', views.ProductList, name='productlist'),
    url(r'^product-lists-detail/(?P<pk>[0-9]+)/', views.ProductListDetail,name='productdetail' ),
    url(r'^signup/', views.SignUp.as_view(), name='signup' ),
    url(r'^signin/', views.SignIn.as_view(), name='signin' ),
    url(r'^logout/', views.LogOut.as_view(), name='logout' ),

    # url(r'^my-orders/', views.MyOrderList.as_view(), ),
    # url(r'^category-lists/', views.CategoryList.as_view(), ),
    # url(r'^category-product/', views.CatProductList.as_view(), ),
    # url(r'^search-product/', views.SearchProduct.as_view(), ),
]
