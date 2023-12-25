from django.contrib import admin
from django.urls import path, include 
from rest_framework import permissions 
from drf_yasg.views import  get_schema_view 
from drf_yasg import openapi
from rest_framework import urls as rest_framework_urls
from dj_rest_auth import urls as dj_rest_auth_urls
from dj_rest_auth.registration import urls as dj_rest_auth_registration_urls


schema_view =get_schema_view(
    openapi.Info(
        title ="Book List Api",
        default_version="1.0",
        description ="Library demo project ",
        terms_of_service="demo.com",
        contact = openapi.Contact(email='abdullachoriyev1321@gamil.com'),
        license = openapi.License(name="demo license")

    )
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('books.urls')),
    path('api-auth/', include(rest_framework_urls)),
    path('api/v1/dj-rest-auth/', include(dj_rest_auth_urls)),
    path('api/v1/dj-rest-auth/registration/', include(dj_rest_auth_registration_urls)),

    #swagger
    path('swagger/',schema_view.with_ui(
        'swagger', cache_timeout =0),
        name='swagger-swagger-ui'),
    path('redoc/',schema_view.with_ui(
        'redoc', cache_timeout =0),
        name='schema-redoc')
]
