from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi, generators
from rest_framework import permissions


class BothHttpAndHttpsSchemaGenerator(generators.OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ["http", "https"]
        return schema

schema_view = get_schema_view(
    openapi.Info(
        title="Ocserv API",
        default_version='v1.0.0',
        description="Ocserv API Docs",
        #   terms_of_service="http://www.google.com/",
        #   contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    generator_class=BothHttpAndHttpsSchemaGenerator,
    public=False,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('api/', include('rest_framework.urls')),
    re_path(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
