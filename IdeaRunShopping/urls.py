from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.authtoken import views

urlpatterns =[
    url(r'^admin/', admin.site.urls),
    url(r'^shop/', include('Shopping.urls') ),
]

urlpatterns += [
    url(r'^api-auth/', views.obtain_auth_token)
]









'''
urlpatterns += [
    url(r'^auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
'''