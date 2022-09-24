from django.contrib import admin
from django.urls import path
from open_food.views import message, list_products, get_product

"""
    The urls.
    The main page will be the page of message.
"""

urlpatterns = [
    path('', message),
    path('products/', list_products),
    path('products/<int:code>', get_product, name='get_product'),
    path('admin/', admin.site.urls),
]
