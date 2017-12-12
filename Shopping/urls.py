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

    url(r'^home', views.Index, name='homepage', ),
    url(r'^product-lists/(?P<pk>[0-9]+)/', views.ProductList.as_view(), name='productlist', ),
    url(r'^product-lists-detail/(?P<pk>[0-9]+)/', views.ProductListDetail,name='productdetail', ),
    url(r'^category-detail/(?P<pk>[0-9]+)/', views.CategoryDetail,name='categorydetail', ),
    url(r'^signup/', views.SignUp.as_view(), name='signup', ),
    url(r'^signin/', views.SignIn.as_view(), name='signin', ),
    url(r'^logout/', views.LogOut, name='logout', ),
    url(r'^categories/', views.Categories, name='categories', ),
    url(r'^myorders/', views.Orders.as_view(), name='myorders', ),
    url(r'^search/', views.search.as_view(), name='search')

    # url(r'^search-product/', views.SearchProduct.as_view(), ),
]
