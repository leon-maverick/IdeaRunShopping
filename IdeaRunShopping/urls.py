from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.authtoken import views
from rest_framework.schemas import get_schema_view

app_name = 'Shopping'

schema_view = get_schema_view(title="Server Monitoring API",permission_classes=[])

urlpatterns = [


    url(r'^admin/', admin.site.urls),
    url(r'^shop/', include('Shopping.urls')),
    url(r'^api-auth/', views.obtain_auth_token),
    url('^$', schema_view),
]
