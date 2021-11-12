"""pm_tools URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.views.generic.base import RedirectView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from user.views import DecoratedTokenObtainPairView, DecoratedTokenRefreshView

schema_view = get_schema_view(
    openapi.Info(
        title='Snippets API',
        default_version='v1',
        description='Test description',
        contact=openapi.Contact(email='contact@snippets.local'),
        license=openapi.License(name='BSD License'),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


url_installed_apps = [
    path('api/token/', DecoratedTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', DecoratedTokenRefreshView.as_view(),
         name='token_refresh'),
]


urlpatterns_DOC = [
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),
]


defaults = [
    path('admin/', admin.site.urls),
    path(
        'favicon.ico',
        RedirectView.as_view(url=staticfiles_storage.url('favicon.ico')),
    ),

]


api = [
    path('api/', include('user.config.urls')),
    path('api/', include('board.config.urls')),
]


urlpatterns = url_installed_apps + urlpatterns_DOC + defaults + api
