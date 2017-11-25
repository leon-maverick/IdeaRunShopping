from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.authtoken import views

# todo add api schema (read in django rest docs)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^shop/', include('Shopping.urls')),
    url(r'^api-auth/', views.obtain_auth_token)
]

