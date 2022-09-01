from rest_framework import serializers
from open_food.models import Produto


class ProdutoSerializer(serializers.ModelSerializer):
    """
        Class Serializer, pega todos os  campos do modelo do banco de dados exceto o id.
    """
    class Meta:
        model = Produto
        exclude = ['id']