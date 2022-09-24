from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializer import ProductSerializer
from django.core.paginator import Paginator


@api_view()
def message(self):
    """
    :param self:
    :return: This funtion return the message "Fullstack Challenge 20201026" and status code 200
    """
    self.content = {'message': "Fullstack Challenge 20201026"}
    return Response(self.content["message"], status=status.HTTP_200_OK)


@api_view()
def list_products(request):
    """
     :return: 10 products of database for page.
    """
    products = Product.objects.all()
    if not len(products):
        return Response(status=status.HTTP_204_NO_CONTENT)
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    product_serializer = ProductSerializer(page_obj, many=True)
    return Response(product_serializer.data)


@api_view()
def get_product(self, code):
    """
    :param self:
    :param code: code of product to be seached in database
    :return: product referent the informed code that be in database
    """
    self.product = Product.objects.filter(code=code)
    if not len(self.product):
        return Response(status=status.HTTP_404_NOT_FOUND)
    product_serializer = ProductSerializer(self.product, many=True)
    return Response(product_serializer.data)
