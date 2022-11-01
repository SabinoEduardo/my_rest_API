# coding=utf-8
from django.contrib import admin
from open_food_app.models import Product

# Admin site


class Products(admin.ModelAdmin):
    list_display = (

                    "code", "barcode", "status", "imported_t", "url",
                    "product_name", "quantity", "categories",
                    "packaging", "brands", "image_url"

                )


admin.site.register(Product, Products)
