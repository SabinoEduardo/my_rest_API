import pymysql.cursors
from scraping import Dados
from datetime import datetime
from contextlib import contextmanager


@contextmanager
def conect_db():
    """
    Conectando ao banco de dados
    """
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='DB_product_scraping',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        yield conexao
    finally:
        conexao.close()


def insert_into(product):
    """
    Esta função serve para inserir os produtos no banco de dados.
    :param product: instância da classe Dados
    :return: função sem retorno
    """
    for id_product, product in product.products().items():
        try:
            sql = 'INSERT INTO open_food_produto (code, barcode, status, imported_t, url, product_name, ' \
                  'quantity, categories, packaging, brands, image_url) ' \
                  'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

            cursor.execute(
                            sql, (product['code'], product['barcode'], 'imported', f'{datetime.now()}',
                                  product['url'], product['product_name'], product['quantity'],
                                  product['categories'], product['packaging'], product['brands'],
                                  product['image_url'])
                        )

            con.commit()
        except pymysql.err.IntegrityError:
            pass


def select_all_and_compare(product, page):
    """
    Função para verificar se os produtos a serem sincronizados já existem no banco de dados. Se já existem, o sistema
    vai realizar nova raspagem do site.

    :param product: objeto da classe Dados
    :param page: o número da página do site openfood
    :return: Essa função tem retorno
    """
    list_key = list()
    cursor.execute('SELECT * FROM open_food_produto')
    for linha in cursor.fetchall():
        for key, value in product.products().items():
            if linha['code'] == value['code']:
                list_key.append(key)
    if list_key:
        for key in list_key:
            del product.products()[key]
        if not product.products():
            page += 1
            product = Dados(page)
            select_all_and_compare(product, page)
    insert_into(product)


with conect_db() as con:
    page_site = 1
    products = Dados(page_site)
    with con.cursor() as cursor:
        select_all_and_compare(products, page_site)
