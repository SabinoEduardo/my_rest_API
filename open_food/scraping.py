import requests
from bs4 import BeautifulSoup
import request


class Dados:
    """
        Classe com todos o métodos para acessar as informações de cada produto na página.
        Aplicando recursividade, a cada chamada dos médotos será adicionado um produto na
        lista de produtos (dicionário) com as seguintes informações:

            :Código : int
            :Código de Barra : str
            :Quantidade : str
            :Nome : str
            :Categoria : str
            :Embalagem : str
            :Marca : str

        Uma função chama a outra até ser coletada todas as informações necessárias do produto.
        As funções serão chamadas até o sistema percorrer todas as páginas dos produtos.

        Usando uma estrutura condicional, deficiu-se o limite de 100 produtos a serem coletados na página.
        Significa que mesmo o sistema pegar mais de 100 prodtos, apenas 100 produtos serão sincronizados para
        o banco de dados.
    """

    def __init__(self, page):
        self.urls = request.get_link_products(page)
        self.products_dict = dict()
        self.len_lista = len(self.products_dict)
        self.quantity = None
        self.content_html = None

    def products(self):
        """
        :return: retorna um dicionário com 100 produtos resultados do scraping do site open food
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
            Função para pegar o valor do código do produto (Valor inteiro)
            :return: Sem retorno
        """
        try:
            code = self.content_html.select_one('span#barcode')
            code = int(code.text)
            self.products_dict[f'{self.len_lista}']['code'] = code
        except AttributeError:
            self.products_dict[f'{self.len_lista}']['code'] = "Null"
        self.get_barcode()

    def get_barcode(self):
        """
            Função para acessar o Código de Barras do Produto
            :return: Sem retorno
        """
        try:
            value_barcode = self.content_html.select_one('#barcode_paragraph')
            barcode = str(value_barcode.text).replace('Barcode: ', '').strip()
            self.products_dict[f'{self.len_lista}']['barcode'] = barcode
        except AttributeError:
            self.products_dict[f'{self.len_lista}']['barcode'] = "Null"
        self.get_quantity()

    def get_quantity(self):
        """
            Função para acessar a quantidade do produto, dependendo do produto poder massa ou volume.
            :return: Sem retorno
        """
        try:
            self.quantity = self.content_html.select_one('#field_quantity_value')
            self.products_dict[f'{self.len_lista}']['quantity'] = self.quantity.text
        except AttributeError:
            self.products_dict[f'{self.len_lista}']['quantity'] = "Null"
        self.config_name()

    def config_name(self):
        """
            Função para acessar o Nome do Produto
            :return: Sem retorno
        """
        try:
            extense_name = self.content_html.select_one('[itemscope] h1')
            extense_name = str(extense_name.text)
            name = extense_name.replace(f' - {self.quantity}', '')
            self.products_dict[f'{self.len_lista}']['product_name'] = name
        except AttributeError:
            self.products_dict[f'{self.len_lista}']['product_name'] = "Null"
        self.get_categories()

    def get_categories(self):
        """
            Função para acessar a Categoria  na qual o produto pertence
            :return: Sem retorno
        """
        try:
            categories = self.content_html.select_one('.field_value#field_categories_value')
            self.products_dict[f'{self.len_lista}']['categories'] = categories.text
        except AttributeError:
            self.products_dict[f'{self.len_lista}']['categories'] = "Null"
        self.get_packaging()

    def get_packaging(self):
        """
            Função para acessar as informações sobre a embalagem do produto
            :return: Sem retorno
        """
        try:
            packaging = self.content_html.select_one('.field_value#field_packaging_value')
            self.products_dict[f'{self.len_lista}']['packaging'] = packaging.text
        except AttributeError:
            self.products_dict[f'{self.len_lista}']['packaging'] = "Null"
        self.get_brands()

    def get_brands(self):
        """
            Função para acessar a Marca do Produto
            :return: Sem retorno

        """
        try:
            brands = self.content_html.select_one('#field_brands a')
            self.products_dict[f'{self.len_lista}']['brands'] = brands.text
        except AttributeError:
            self.products_dict[f'{self.len_lista}']['brands'] = "Null"
        self.get_image_url()

    def get_image_url(self):
        """
            Função para acessar a Marca do Produto
            :return: Sem retorno

        """
        try:
            url = 'https://world.openfoodfacts.org/'
            img_url = url + self.content_html.select_one('#og_image.hide-for-xlarge-up')['src']
            self.products_dict[f'{self.len_lista}']['image_url'] = img_url
        except TypeError:
            self.products_dict[f'{self.len_lista}']['image_url'] = "Null"
        print(self.len_lista + 1)
        print(self.products_dict[f'{self.len_lista}'])
        self.len_lista += 1


if __name__ == '__main__':
    products = Dados(1)
    for id_product, product in products.products().items():
        print(f'Produto {int(id_product) + 1}')
        for key, value in product.items():
            print(f'{key}: {value}')
        print()
