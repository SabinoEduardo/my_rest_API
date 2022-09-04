from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Produto
from .serializer import ProdutoSerializer
from django.core.paginator import Paginator


@api_view()
def mensagem(self):
    """

    :param self:
    :return: Esta função retorna uma mensagem
    """
    self.content = {'Mensagem': "Fullstack Challenge 20201026"}
    return Response(self.content["Mensagem"], status=status.HTTP_200_OK)


@api_view()
def list_products(request):
    """
     :return: retorna os produtos do banco de dados por páginas
    """
    products = Produto.objects.all()
    if not len(products):
        msg = {'Mensagem': 'Lista de Produtos está vazia'}
        return Response(msg['Mensagem'], status=status.HTTP_204_NO_CONTENT)
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    product_serializer = ProdutoSerializer(page_obj, many=True)
    return Response(product_serializer.data)


@api_view()
def get_product(self, code):
    """

    :param self:
    :param code: Código do produto a ser pesquisado no banco de dados
    :return: retorna um produto, cujo o código informado está no banco de dados.
    """
    self.product = Produto.objects.filter(code=code)
    if not len(self.product):
        msg = {'Mensagem': 'Produto não existe'}
        return Response(msg['Mensagem'], status=status.HTTP_404_NOT_FOUND)
    product_serializer = ProdutoSerializer(self.product, many=True)
    return Response(product_serializer.data)
