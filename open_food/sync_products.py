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
        db='DB_product_Scraping',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        yield conexao
    finally:
        conexao.close()


def insert_into(products):
    """
    Esta função serve para inserir os produtos no banco de dados.
    :param products: instância da classe Dados
    :return: função sem retorno
    """
    for id_product, prod in products.items():
        try:
            sql = 'INSERT INTO open_food_produto (code, barcode, status, imported_t, url, product_name, ' \
                  'quantity, categories, packaging, brands, image_url) ' \
                  'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

            cursor.execute(
                            sql, (prod['code'], prod['barcode'], 'imported', f'{datetime.now()}',
                                  prod['url'], prod['product_name'], prod['quantity'],
                                  prod['categories'], prod['packaging'], prod['brands'],
                                  prod['image_url'])
                        )

            con.commit()
        except pymysql.err.IntegrityError:
            pass


with conect_db() as con:
    with con.cursor() as cursor:
        cursor.execute('SELECT * FROM open_food_produto')
        numbers_product = len(cursor.fetchall())
        page_site = int(numbers_product/100) + 1
        product = Dados(page_site)
        insert_into(product.products())
