from django.contrib import admin
from django.urls import path
from open_food.views import message, list_products, get_product
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

"""
    The urls.
    The main page will be the page of message.
"""

schema_view = get_schema_view(
   openapi.Info(
      title="Product Scraping",
      default_version='v1',
      description=" Esta API utiliza os dados do projeto Open Food Facts, um banco de dados aberto com informação "
                  "nutricional de diversos produtos alimentícios.",

      terms_of_service="#",
      contact=openapi.Contact(email="afonsos@yahoo.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('', message, name='Message'),
    path('products/', list_products, name='Products'),
    path('products/<int:code>', get_product, name='GET_Products'),
    path('admin/', admin.site.urls),
    path('documentation/', schema_view.with_ui('swagger', cache_timeout=0), name='scraping_documentation'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
