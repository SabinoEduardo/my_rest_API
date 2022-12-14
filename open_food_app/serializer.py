from rest_framework import serializers
from open_food_app.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
        Class Serializer to chance the date for Json.
    """
    class Meta:
        model = Product
        exclude = ('id',)
