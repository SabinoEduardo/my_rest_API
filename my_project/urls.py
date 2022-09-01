from django.contrib import admin
from django.urls import path
from open_food.views import mensagem, list_products, get_product

"""
    As urls de acordo com o que será solicitado.
    A página principal será a página de mensagem.
"""

urlpatterns = [
    path('', mensagem),
    path('admin/', admin.site.urls),
    path('products/<int:code>', get_product, name='get_product'),
    path('products/', list_products),
]
