from rest_framework.test import APITestCase
from open_food.models import Product
from rest_framework import status
from datetime import datetime
from open_food.scraping import Date


class ProductsTestCase(APITestCase):
    def setUp(self):
        self.products = Date(1, 10)
        # self.list_url = reverse('Products')
        for _, prod in self.products.products().items():
            self.product_1 = Product.objects.create(
                code=int(prod['code']),
                barcode=prod['barcode'],
                status='imported',
                imported_t=datetime.now(),
                url=prod['url'],
                product_name=prod['product_name'],
                quantity=prod['quantity'],
                categories=prod['categories'],
                packaging=prod['packaging'],
                brands=prod['brands'],
                image_url=prod['image_url'],
            )

    def test_get(self):
        response = self.client.get('http://127.0.0.1:8000/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_request_get_to_list_products(self):
        response = self.client.get('http://127.0.0.1:8000/products/')
        # response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_informations_of_one_product(self):
        code = 3017620422003
        response = self.client.get(f'http://127.0.0.1:8000/products/{code}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
