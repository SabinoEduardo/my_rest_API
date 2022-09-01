from django.contrib import admin
from open_food.models import Produto

# Criando uma representação do meu modelo para a inteface de administração do Django
# O django possui por padrão um interface de administração


class Produtos(admin.ModelAdmin):
    list_display = (

                    "code", "barcode", "status", "imported_t", "url",
                    "product_name", "quantity", "categories",
                    "packaging", "brands", "image_url"

                )


admin.site.register(Produto, Produtos)
