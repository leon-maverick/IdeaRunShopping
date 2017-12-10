from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.authtoken import views
from rest_framework.schemas import get_schema_view
# from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Shopping'

schema_view = get_schema_view(title="Server Monitoring API",permission_classes=[])

urlpatterns = [
    # url(r'^(?P<filename>(robots.txt)|(humans.txt))$', home_files, name='home-files'),

    url(r'^api-auth/', views.obtain_auth_token),
    # url(r'^i18n/', include('django.conf.urls.i18n')),
    url('^$', schema_view),
    url(r'^admin/', admin.site.urls),
    url(r'^shop/', include('Shopping.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns += i18n_patterns(
#
# )

