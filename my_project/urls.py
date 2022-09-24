from django.contrib import admin
from django.urls import path
from open_food.views import message, list_products, get_product

"""
    As urls de acordo com o que será solicitado.
    A página principal será a página de mensagem.
"""

urlpatterns = [
    path('', message),
    path('products/', list_products),
    path('products/<int:code>', get_product, name='get_product'),
    path('admin/', admin.site.urls),
]
