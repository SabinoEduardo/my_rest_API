import requests
from bs4 import BeautifulSoup
import request


class Date:
    """
        class with all methods to acess the data of products
        Apply recursivity, every time that to call the methods this class will be added a profuct in
        dictionário of products with the information:

            :Code : int
            :Barcode : str
            :quantity : str
            :name : str
            :categories : str
            :packaging : str
            :brands : str

        A funtion call other funtion to get all information of product.
        The funtions will be called until the system to get all products for page.

        Using a conditional structure, will set a limit of 100 products to been colected for page.

    """

    def __init__(self, page):
        self.urls = request.get_link_products(page)
        self.products_dict = dict()
        self.len_lista = len(self.products_dict)
        self.quantity = None
        self.content_html = None

    def products(self):
        """
        :return: a dictionary with 100 products
        """
        if self.len_lista < 100:
            self.products_dict[f'{self.len_lista}'] = {}
            url = self.urls[self.len_lista]
            self.products_dict[f'{self.len_lista}']['url'] = url
            page_html = requests.get(f'{url}')
            self.content_html = BeautifulSoup(page_html.content, 'html.parser')
            self.get_code()
        return self.products_dict

    def get_code(self):
        """
            Function to get the code value of product
            :return: without return
        """
        try:
            code = self.content_html.select_one('span#barcode')
            code = int(code.text)
            self.products_dict[f'{self.len_lista}']['code'] = code
        except AttributeError:
            self.products_dict[f'{self.len_lista}']['code'] = 0
        self.get_barcode()

    def get_barcode(self):
        """
            Function to get the barcode of product
            :return: without return
        """
        try:
            value_barcode = self.content_html.select_one('#barcode_paragraph')
            barcode = (str(value_barcode.text).replace('Barcode: ', '').strip()).replace(' ', '')
            self.products_dict[f'{self.len_lista}']['barcode'] = barcode
        except AttributeError:
            self.products_dict[f'{self.len_lista}']['barcode'] = "Null"
        self.get_quantity()

    def get_quantity(self):
        """
            Function to get the quantity of product.
            :return: without return
        """
        try:
            self.quantity = self.content_html.select_one('#field_quantity_value')
            self.products_dict[f'{self.len_lista}']['quantity'] = self.quantity.text
        except AttributeError:
            self.products_dict[f'{self.len_lista}']['quantity'] = "Null"
        self.config_name()

    def config_name(self):
        """
            Function to get the name of product.
            :return: without return
        """
        try:
            extense_name = self.content_html.select_one('[itemscope] h1')
            extense_name = str(extense_name.text)
            name = extense_name.replace(f'{self.quantity.text}', '')
            self.products_dict[f'{self.len_lista}']['product_name'] = name
        except AttributeError:
            self.products_dict[f'{self.len_lista}']['product_name'] = "Null"
        self.get_categories()

    def get_categories(self):
        """
            Function to get the categories of product.
            :return: without return
        """
        try:
            categories = self.content_html.select_one('.field_value#field_categories_value')
            self.products_dict[f'{self.len_lista}']['categories'] = categories.text
        except AttributeError:
            self.products_dict[f'{self.len_lista}']['categories'] = "Null"
        self.get_packaging()

    def get_packaging(self):
        """
            Function to get the packaging of product.
            :return: without return
        """
        try:
            packaging = self.content_html.select_one('.field_value#field_packaging_value')
            self.products_dict[f'{self.len_lista}']['packaging'] = packaging.text
        except AttributeError:
            self.products_dict[f'{self.len_lista}']['packaging'] = "Null"
        self.get_brands()

    def get_brands(self):
        """
            Function to get the brand of product.
            :return: without return

        """
        try:
            brands = self.content_html.select_one('#field_brands a')
            self.products_dict[f'{self.len_lista}']['brands'] = brands.text
        except AttributeError:
            self.products_dict[f'{self.len_lista}']['brands'] = "Null"
        self.get_image_url()

    def get_image_url(self):
        """
            Function to get the image url of product.
            :return: without return

        """
        try:
            url = 'https://world.openfoodfacts.org/'
            img_url = url + self.content_html.select_one('#og_image.hide-for-xlarge-up')['src']
            self.products_dict[f'{self.len_lista}']['image_url'] = img_url
        except TypeError:
            self.products_dict[f'{self.len_lista}']['image_url'] = "Null"
        self.len_lista += 1
        self.products()


# to test
if __name__ == '__main__':
    products = Date(1)
    for id_product, product in products.products().items():
        print(f'Produto {int(id_product) + 1}')
        for key, value in product.items():
            print(f'{key}: {value}')
        print()
